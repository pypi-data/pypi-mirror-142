import os
import builtins
from io import BytesIO
from pathlib import Path
from json import load
from warnings import warn

from unittest import mock
import pytest
from PIL import Image, ImageCms, UnidentifiedImageError
from pillow_heif import (
    register_heif_opener,
    options,
    HeifBrand,
)


register_heif_opener()
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with builtins.open("images_info.json", "rb") as _:
    all_images = load(_)

if not options().avif:
    warn("Skipping tests for `AV1` format due to lack of codecs.")
    all_images = [e for e in all_images if not e["name"].endswith(".avif")]

invalid_images = [e for e in all_images if not e["valid"]]
heif_images = [e for e in all_images if e["valid"]]

heic_images = [e for e in heif_images if e["name"].endswith(".heic")]
hif_images = [e for e in heif_images if e["name"].endswith(".hif")]
avif_images = [e for e in heif_images if e["name"].endswith(".avif")]


@pytest.mark.parametrize("img_info", heif_images)
def test_open_images(img_info):
    try:
        options().strict = img_info["strict"]
        pillow_image = Image.open(Path(img_info["file"]))
        assert getattr(pillow_image, "fp") is None
        assert getattr(pillow_image, "heif_file") is not None
        assert pillow_image.info
        assert pillow_image.info["brand"] != HeifBrand.UNKNOWN.name
        if img_info["exif_length"] is not None:
            assert len(pillow_image.info["exif"]) == img_info["exif_length"]
        else:
            assert pillow_image.info["exif"] is None
        # Color profile is always present in `dump` and in `info`
        if img_info["color_profile"]:
            assert len(pillow_image.info["color_profile"])
        else:
            assert not len(pillow_image.info["color_profile"])
        # If icc profile is present, it's size can be zero.
        if img_info.get("icc_profile", None) is None:
            assert "icc_profile" not in pillow_image.info
        else:
            assert len(pillow_image.info["icc_profile"]) == img_info["icc_profile"]
            if len(pillow_image.info["icc_profile"]):
                ImageCms.getOpenProfile(BytesIO(pillow_image.info["icc_profile"]))
        # If nclx profile is present, it's size can not be zero.
        if img_info.get("nclx_profile", None):
            assert len(pillow_image.info["nclx_profile"]) == img_info["nclx_profile"]
        else:
            assert "nclx_profile" not in pillow_image.info
        # Compare number of metadata records
        assert len(pillow_image.info["metadata"]) == len(img_info["metadata"])
        # Verify image
        pillow_image.verify()
        # Here we must check verify, but currently verify do nothing.
    finally:
        options().reset()


@pytest.mark.parametrize("img_info", heic_images[:4] + hif_images[:4] + avif_images[:4])
def test_load_images(img_info):
    with builtins.open(Path(img_info["file"]), "rb") as f:
        bytes_io = BytesIO(f.read())
    fh = builtins.open(Path(img_info["file"]), "rb")
    for _as in (Path(img_info["file"]).as_posix(), bytes_io, fh):
        pillow_image = Image.open(_as)
        assert getattr(pillow_image, "heif_file") is not None
        pillow_image.load()
        assert getattr(pillow_image, "heif_file") is None


@pytest.mark.parametrize("img_info", invalid_images)
def test_invalid_data(img_info):
    with pytest.raises(UnidentifiedImageError):
        Image.open(Path(img_info["file"]).as_posix())
    with pytest.raises(UnidentifiedImageError):
        Image.open(Path(img_info["file"]))
    with pytest.raises(UnidentifiedImageError):
        with builtins.open(Path(img_info["file"]), "rb") as f:
            Image.open(BytesIO(f.read()))
    with pytest.raises(UnidentifiedImageError):
        with builtins.open(Path(img_info["file"]), "rb") as f:
            Image.open(f)


@pytest.mark.parametrize(
    "params",
    [
        {},
        {"avif": True},
        {"avif": False},
        {"avif": True, "xxx1": False},
        {"avif": False, "xxx1": True},
        {"xxx1": True, "xxx2": True},
    ],
)
@mock.patch.object(Image, "register_extensions")
@mock.patch.object(Image, "register_mime")
@mock.patch.object(Image, "register_open")
def test_register_heif_opener(register_open, register_mime, register_extensions, params):
    options().reset()
    asser_value = options().avif and params.get("avif", options().avif)
    register_heif_opener(**params)
    assert options().avif == asser_value
    mime_call_count = 2 if options().avif else 1
    register_open.assert_called_once()
    assert register_mime.call_count == mime_call_count
    register_extensions.assert_called_once()

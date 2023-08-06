from PIL import Image
import requests
import numpy as np
from typing import List, Union


def exif_transpose(image: Image.Image):
    """
    Transpose a PIL image accordingly if it has an EXIF Orientation tag.
    Inplace version of https://github.com/python-pillow/Pillow/blob/master/src/PIL/ImageOps.py exif_transpose()
    :param image: The image to transpose.
    :return: An image.
    """
    exif = image.getexif()
    orientation = exif.get(0x0112, 1)  # default 1
    if orientation > 1:
        method = {
            2: Image.FLIP_LEFT_RIGHT,
            3: Image.ROTATE_180,
            4: Image.FLIP_TOP_BOTTOM,
            5: Image.TRANSPOSE,
            6: Image.ROTATE_270,
            7: Image.TRANSVERSE,
            8: Image.ROTATE_90,
        }.get(orientation)
        if method is not None:
            image = image.transpose(method)
            del exif[0x0112]
            image.info["exif"] = exif.tobytes()
    return image


def read_image_as_pil(
    image: Union[Image.Image, str, np.ndarray], exif_fix: bool = False
):
    """
    Loads an image as PIL.Image.Image.

    Args:
        image : Can be image path or url (str), numpy image (np.ndarray) or PIL.Image
    """
    # https://stackoverflow.com/questions/56174099/how-to-load-images-larger-than-max-image-pixels-with-pil
    Image.MAX_IMAGE_PIXELS = None
    # read image if str image path is provided
    if isinstance(image, str):
        # read image as pil
        try:
            image_pil = Image.open(
                requests.get(image, stream=True).raw
                if str(image).startswith("http")
                else image
            ).convert("RGB")
            if exif_fix:
                image_pil = exif_transpose(image_pil)
        except:  # handle large/tiff image reading
            try:
                import skimage.io
            except ImportError:
                raise ImportError(
                    "Please run 'pip install -U scikit-image imagecodecs' for large image handling."
                )
            image_sk = skimage.io.imread(image).astype(np.uint8)
            if len(image_sk.shape) == 2:  # b&w
                image_pil = Image.fromarray(image_sk, mode="1")
            if image_sk.shape[2] == 4:  # rgba
                image_pil = Image.fromarray(image_sk, mode="RGBA")
            elif image_sk.shape[2] == 3:  # rgb
                image_pil = Image.fromarray(image_sk, mode="RGB")
            else:
                raise TypeError(
                    f"image with shape: {image_sk.shape[3]} is not supported."
                )
    elif isinstance(image, np.ndarray):
        if image.shape[0] < 5:  # image in CHW
            image = image[:, :, ::-1]
        image_pil = Image.fromarray(image)
    elif isinstance(image, Image.Image):
        image_pil = image
    else:
        TypeError("read image with 'pillow' using 'Image.open()'")
    return image_pil


def get_slice_bboxes(
    image_height: int,
    image_width: int,
    slice_height: int = 512,
    slice_width: int = 512,
    overlap_height_ratio: int = 0.2,
    overlap_width_ratio: int = 0.2,
) -> List[List[int]]:
    """Slices `image_pil` in crops.
    Corner values of each slice will be generated using the `slice_height`,
    `slice_width`, `overlap_height_ratio` and `overlap_width_ratio` arguments.

    Args:
        image_height (int): Height of the original image.
        image_width (int): Width of the original image.
        slice_height (int): Height of each slice. Default 512.
        slice_width (int): Width of each slice. Default 512.
        overlap_height_ratio(float): Fractional overlap in height of each
            slice (e.g. an overlap of 0.2 for a slice of size 100 yields an
            overlap of 20 pixels). Default 0.2.
        overlap_width_ratio(float): Fractional overlap in width of each
            slice (e.g. an overlap of 0.2 for a slice of size 100 yields an
            overlap of 20 pixels). Default 0.2.

    Returns:
        List[List[int]]: List of 4 corner coordinates for each N slices.
            [
                [slice_0_left, slice_0_top, slice_0_right, slice_0_bottom],
                ...
                [slice_N_left, slice_N_top, slice_N_right, slice_N_bottom]
            ]
    """
    slice_bboxes = []
    y_max = y_min = 0
    y_overlap = int(overlap_height_ratio * slice_height)
    x_overlap = int(overlap_width_ratio * slice_width)
    while y_max < image_height:
        x_min = x_max = 0
        y_max = y_min + slice_height
        while x_max < image_width:
            x_max = x_min + slice_width
            if y_max > image_height or x_max > image_width:
                xmax = min(image_width, x_max)
                ymax = min(image_height, y_max)
                xmin = max(0, xmax - slice_width)
                ymin = max(0, ymax - slice_height)
                slice_bboxes.append([xmin, ymin, xmax, ymax])
            else:
                slice_bboxes.append([x_min, y_min, x_max, y_max])
            x_min = x_max - x_overlap
        y_min = y_max - y_overlap
    return slice_bboxes

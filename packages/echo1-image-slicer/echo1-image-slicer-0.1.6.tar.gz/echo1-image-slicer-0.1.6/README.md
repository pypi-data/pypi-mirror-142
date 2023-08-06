# echo1-image-slicer

echo1-image-slicer provides a fast way to slice an image into smaller images

## Installation & Use

```shell
# Install echo1-image-slicer
pip install echo1-image-slicer

# Run the image-slicer
image-slicer \
    -f ./tests/test.jpg \
    -s ./output \
    -sp yolo- \
    -sw 500 \
    -sh 500 

2022-02-18 16:24:08.959 | INFO     | echo1_image_slicer.echo1_image_slicer:slice_image:17 - Loading the file ./tests/test.jpg
2022-02-18 16:24:09.015 | DEBUG    | echo1_image_slicer.echo1_image_slicer:slice_image:22 - The image shape is (1333, 1333)
2022-02-18 16:24:09.015 | DEBUG    | echo1_image_slicer.echo1_image_slicer:slice_image:29 - Calculating the slice box positions.
2022-02-18 16:24:09.068 | INFO     | echo1_image_slicer.echo1_image_slicer:slice_image:58 - Saved 16 image slices to ./output
```

## image-slicer help

```shell
usage: image-slicer [-h] -f FILE_NAME [-sp SAVE_TO_FILE_PREFIX] -s SAVE_TO_DIR -sw SLICE_WIDTH -sh SLICE_HEIGHT
                    [-ow OVERLAP_WIDTH_RATIO] [-oh OVERLAP_HEIGHT_RATIO]

Slices an image into smaller images.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE_NAME, --file_name FILE_NAME
                        The file name to slice.
  -sp SAVE_TO_FILE_PREFIX, --save_to_file_prefix SAVE_TO_FILE_PREFIX
                        The prefix for saved slice file names.
  -s SAVE_TO_DIR, --save_to_dir SAVE_TO_DIR
                        The directory to save the slices to.
  -sw SLICE_WIDTH, --slice_width SLICE_WIDTH
                        The width of each slice.
  -sh SLICE_HEIGHT, --slice_height SLICE_HEIGHT
                        The height of each slice.
  -ow OVERLAP_WIDTH_RATIO, --overlap_width_ratio OVERLAP_WIDTH_RATIO
                        The overlap width ratio.
  -oh OVERLAP_HEIGHT_RATIO, --overlap_height_ratio OVERLAP_HEIGHT_RATIO
                        The overlap height ratio.
```

## Thanks

Previous work done by:

* [GitHub - obss/sahi: A lightweight vision library for performing large scale object detection/ instance segmentation.](https://github.com/obss/sahi)

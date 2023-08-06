# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['echo1_image_slicer', 'echo1_image_slicer.helpers']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.0.1,<10.0.0', 'loguru>=0.6.0,<0.7.0', 'numpy>=1.22.2,<2.0.0']

entry_points = \
{'console_scripts': ['image-slicer = '
                     'echo1_image_slicer.echo1_image_slicer:app']}

setup_kwargs = {
    'name': 'echo1-image-slicer',
    'version': '0.1.6',
    'description': '',
    'long_description': '# echo1-image-slicer\n\necho1-image-slicer provides a fast way to slice an image into smaller images\n\n## Installation & Use\n\n```shell\n# Install echo1-image-slicer\npip install echo1-image-slicer\n\n# Run the image-slicer\nimage-slicer \\\n    -f ./tests/test.jpg \\\n    -s ./output \\\n    -sp yolo- \\\n    -sw 500 \\\n    -sh 500 \n\n2022-02-18 16:24:08.959 | INFO     | echo1_image_slicer.echo1_image_slicer:slice_image:17 - Loading the file ./tests/test.jpg\n2022-02-18 16:24:09.015 | DEBUG    | echo1_image_slicer.echo1_image_slicer:slice_image:22 - The image shape is (1333, 1333)\n2022-02-18 16:24:09.015 | DEBUG    | echo1_image_slicer.echo1_image_slicer:slice_image:29 - Calculating the slice box positions.\n2022-02-18 16:24:09.068 | INFO     | echo1_image_slicer.echo1_image_slicer:slice_image:58 - Saved 16 image slices to ./output\n```\n\n## image-slicer help\n\n```shell\nusage: image-slicer [-h] -f FILE_NAME [-sp SAVE_TO_FILE_PREFIX] -s SAVE_TO_DIR -sw SLICE_WIDTH -sh SLICE_HEIGHT\n                    [-ow OVERLAP_WIDTH_RATIO] [-oh OVERLAP_HEIGHT_RATIO]\n\nSlices an image into smaller images.\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -f FILE_NAME, --file_name FILE_NAME\n                        The file name to slice.\n  -sp SAVE_TO_FILE_PREFIX, --save_to_file_prefix SAVE_TO_FILE_PREFIX\n                        The prefix for saved slice file names.\n  -s SAVE_TO_DIR, --save_to_dir SAVE_TO_DIR\n                        The directory to save the slices to.\n  -sw SLICE_WIDTH, --slice_width SLICE_WIDTH\n                        The width of each slice.\n  -sh SLICE_HEIGHT, --slice_height SLICE_HEIGHT\n                        The height of each slice.\n  -ow OVERLAP_WIDTH_RATIO, --overlap_width_ratio OVERLAP_WIDTH_RATIO\n                        The overlap width ratio.\n  -oh OVERLAP_HEIGHT_RATIO, --overlap_height_ratio OVERLAP_HEIGHT_RATIO\n                        The overlap height ratio.\n```\n\n## Thanks\n\nPrevious work done by:\n\n* [GitHub - obss/sahi: A lightweight vision library for performing large scale object detection/ instance segmentation.](https://github.com/obss/sahi)\n',
    'author': 'Michael Mohamed',
    'author_email': 'michael.mohamed@echo1.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/e1-io/echo1-image-slicer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

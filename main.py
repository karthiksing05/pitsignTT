#!/usr/bin/env python
import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

import glob

# image1 = Image.open("1.png")
# image2 = Image.open("2.png")
# image3 = Image.open("3.png")
# image4 = Image.open("4.png")
# image5 = Image.open("5.png")
# image6 = Image.open("6.png")
# image7 = Image.open("7.png")
# image8 = Image.open("8.png")

def af(lst, idx):
    """factorial but you add instead of multiply"""
    val = 0
    for i, elem in enumerate(lst):
        if i <= idx:
            val += elem
        else:
            return val
    return val


filenames = [fn for fn in glob.glob("pic\\*.png")]

images = [Image.open(fn) for fn in filenames]

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 5
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options=options)

# Make image fit our screen.
# image1.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
# image2.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
# image3.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
# image4.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
# image5.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
# image6.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
# image7.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
# image8.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

images = [image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS) for image in images]

print("Press CTRL-C to stop.")
double_buffer = matrix.CreateFrameCanvas()
xpos = 0

widths = [image.size[0] for image in images]
cycleDelay = 0.01

while True:
    try:
        xpos += 1
        if xpos > widths[xpos - 1]:
            xpos = 0

        for i, image in enumerate(images):
            double_buffer.SetImage(image.convert('RGB'), -xpos + af(widths, xpos - 1))

        double_buffer = matrix.SwapOnVSync(double_buffer)
        time.sleep(cycleDelay)

    except KeyboardInterrupt:
        sys.exit(0)

#!/usr/bin/env python
import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

import glob

### Loading the images into variables in the two lines below

image = Image.open("pics\\1techno.png")

### Loading a transparent image (we will be using this later)
# transparent = Image.open('transparent.png')
# transparent = transparent.resize((32, 10))

### Configuration of the matrix (so it is rigged for our settings/hardware)
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 5
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options=options)

### Setting the image thumbnail so that when each image is displayed on the matrix screen it fits
image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

### The code below is the mainloop to cycle all the images. The way it works is as follows:
# 1.  A double_buffer (canvas) is created; this is what cycles through the matrix. 
#     We are putting each image on this virtual "canvas" at specific offsets to make the
#     pit sign look like it's scrolling.
# 2.  The mainloop iterates forever, and only stops when [CTRL] and the C key are pressed, 
#     this is the default keyboard break for python code and will always end it.
# 3.  There is a variable called xpos that changes by 1 interval, and when adding the pictures
#     to the canvas, this variable will be used to offset each addition; once the 
# 4.  There is also the add-factorial helper method being used, this is just an easy way to
#     offset every new image being added by the widths of the previous images so no images end
#     up being overlapped.
### Once again, please let me know on GitHub (open up an issue under the repository) if you have any
### questions, comments, concerns, etc.

print("Press CTRL + C to stop.")
double_buffer = matrix.CreateFrameCanvas()
xpos = 0

cycleDelay = 0.01

while True:

    double_buffer.SetImage(image.convert('RGB'), 160) # change that maybe?

    double_buffer = matrix.SwapOnVSync(double_buffer)
    time.sleep(cycleDelay)

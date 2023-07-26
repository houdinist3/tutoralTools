import imageUtils
import osutils
import sys
import os


def main(imageDir):
    if len(sys.argv) != 2:
        print("no dirctory provided")
        return

    images = osutils.getFileOfType(imageDir, "*exr")
    # imageUtils.convertToRat(images, 'exr', 'rat')
    imageUtils.convertToImaketx(images, 'exr', 'rat')
main(sys.argv[-1])
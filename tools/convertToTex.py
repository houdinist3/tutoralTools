import imageUtils
import osUtils
import sys
import os


def main(imageDir):
    if len(sys.argv) != 2:
        print("no dirctory provided")
        return

    images = osUtils.getFileOfType(imageDir, "*jpg")
    imageUtils.convertToRat(images)

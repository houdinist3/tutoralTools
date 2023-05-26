import os
from shutil import copyfile
from distutils.dir_util import copy_tree
import tarfile
import zipfile
import glob


def getFileOfType(destDir, fileType):
    files = []
    for x in os.walk(destDir):
        for y in glob.glob(os.path.join(x[0], "*.{}".format(fileType))):
            files.append(y)
    return files

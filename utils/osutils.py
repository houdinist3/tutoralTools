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


def rename(dir, text, mode, replaceText=''):
    for fil in os.listdir(dir):
        fil = os.path.join(dir, fil)
        fileName = os.path.basename(fil)

        if mode == 'prepend':
            newName = os.path.join(dir, fileName.replace(fileName, text + fileName))
        elif mode == 'replace':
            newName = os.path.join(dir, fileName.replace(text, replaceText))

        os.rename(fil, newName)
        

# eg 1

newDir = '/home/megatron/Documents/python/dir'
exportDir = '/home/megatron/Documents/python/export'
# if not os.path.exists(newDir):
#     os.makedirs(newDir)

# eg 2
# copy_tree(newDir, newDir.replace('dir', 'dirchanged'))


# eg 3
# fileObj = open(newDir + '/demo.txt', 'a')
# fileObj.write('fill this with text')
# fileObj.close()

# eg 4
# copyfile(newDir + '/demo.txt', newDir + '/demo2.txt')

# eg 5
# contents = [os.path.join(newDir,fil) for fil in os.listdir(newDir)]
# print(contents)

# eg 6
# with tarfile.open(exportDir + '/test.tar.gz', 'w:gz') as tar:
    # tar.add(newDir, arcname=os.path.basename(newDir))

# eg 7
# file = []
# for x in os.walk(newDir):
#     # print(x)
#     for y in glob.glob(os.path.join(x[0], '*.txt')):
#         file.append(y)
# if file:
#     if not os.path.exists(exportDir):
#         os.makedirs(exportDir)

#     with tarfile.open(exportDir + '/txts.tar.gz', 'w:gz') as tar:
#         for txt in file:
#             tar.add(txt, arcname=os.path.basename(txt))

#   git config --global user.email "you@example.com"
#   git config --global user.name "Your Name"
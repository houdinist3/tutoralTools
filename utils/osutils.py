import os
from shutil import copyfile
from distutils.dir_util import copy_tree
import tarfile
import zipfile
import glob

newDir = "D:/Git_Repo/tutoralTools/dir1/dir2"
exportDir = "D:/Git_Repo/tutoralTools/export"
usdDir = "D:/HOUDINI_RND/environment_USD/usd/usd_examples"
# eg1
# if not os.path.exists(newDir):
#     os.makedirs(newDir)
# if not os.path.exists(exportDIr):
#     os.makedirs(exportDIr)


# eg2
# copy_tree(newDir, newDir.replace("dir1", "dir1changed"))

# eg3
# fileObj = open(newDir + "/demo.txt", "a")
# fileObj.write("fill this with text")
# fileObj.close()

# eg4
# copyfile(newDir + "/demo.txt", newDir + "/demo2.txt")

# eg5
# contents = [os.path.join(newDir, file) for file in os.listdir(newDir)]
# print(contents)

# eg6 tar
# with tarfile.open(newDir + "/test.tar.gz", "w:gz") as tar:
#     tar.add(newDir, arcname=os.path.basename(newDir))
# tar.close()

# eg7 tar and glob
usd = []
for x in os.walk(usdDir):
    # print(x[0])
    for y in glob.glob(os.path.join(x[0], "*.usd*")):
        usd.append(y)
print(usd)

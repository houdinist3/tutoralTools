import os
import osUtils
import mayaUtils
import sys

def main(assetDir):
    
    scenes = osUtils.getFileOfType(assetDir, 'ma')
    for scene in scenes:
        abc = mayaUtils.exportMesh(scene)
        print(abc)
        

    
if __name__ == '__main__':
    main(sys.argv[-1])
    
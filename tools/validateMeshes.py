import os
import osUtils
import mayaUtils
import sys

def main(assetDir):
    fileObj = open(os.path.join(assetDir, 'report.txt'), 'a')
    
    scenes = osUtils.getFileOfType(assetDir, 'ma')
    for scene in scenes:
        validate = mayaUtils.validateMesh(scene)
        print(validate)
        
        fileObj.write(validate)
    fileObj.close()
    
if __name__ == '__main__':
    main(sys.argv[-1])
    
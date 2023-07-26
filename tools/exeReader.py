import osutils
import OpenEXR

exrDir = "/show/FX/BDP_HOUDINI_RND/FUR/lion/render/Lion_cam1"

exrs = osutils.getFileOfType(exrDir, 'exr')

exrObj = OpenEXR.InputFile(exrs[0])

for k, v in exrObj.header().iteritems():
    print(k, v)
import os
import argparse
import osUtils


# Fbx download link: https://www.mixamo.com/#/
# Ffmpeg download link: https://ffmpeg.org/
def main():
    """ Run fbx preview generation
    """
    parser = argparse.ArgumentParser(description='find assets and create preview movs')
    parser.add_argument('-d', '--dir', metavar='', default='', help='a dir to find assets')
    parser.add_argument('-a', '--amount', metavar='', default=50, help='set camera distance')
    args = parser.parse_args()

    assetDir = args.dir
    amount = args.amount

    # Check correct arguments are being passed in
    if not assetDir and amount:
        print('need to supply dir and camera distance')
        return

    for fbx in osUtils.getFileOfType(assetDir, 'fbx'):
        
        # Replace hython cmdLine
        command = 'hython -c "import sys; sys.path.append(\'D:/Git_Repo/tutoralTools/utils\');' 
        command += ' import houUtils; houUtils.captureFbx(\'%s\',\'%s\')"' % (fbx, amount)
        os.system(command)

        dirName = os.path.dirname(fbx)

        name = fbx.split('\\')[1].split('.')[0]
        result = name.replace(" ","")
        print(result)
        # jpeg path
        outputImages = dirName + '/tmp.%04d.jpeg'

        movDir = dirName + '/' + f'{result}'
        if not os.path.isdir(movDir):
            os.mkdir(movDir)

        # generate quicktime, replace ffmpeg cmdLine
        # outputMov = fbx.replace('.fbx', '.mov')
        outputMov = movDir + f'/{result}.mov'
        # outputMov.replace("/", "\\")
        print(outputMov)
        os.system('ffmpeg -r 24 -s 720x720 -i %s %s' % (outputImages, outputMov))

        # delete images
        contents = os.listdir(dirName)
        
 
        for item in contents:
            if item.endswith('.jpeg'):
                os.remove(os.path.join(dirName, item))

        # generate thumbnail, replace ffmpeg cmdLine 
        outputThumbnail = outputMov.replace('.mov', '.jpeg')
        os.system('ffmpeg -i %s -vframes 1 -s 360x360 -ss 0.1 %s' % (outputMov, outputThumbnail))


if __name__ == '__main__':
    main()

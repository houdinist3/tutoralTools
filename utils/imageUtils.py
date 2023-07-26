from PIL import Image
import binary
import osutils
import os

# import OpenImageIO as oiio
# import OpenEXR


def convertImage(images, convertFrom, convertTo):
    for image in images:
        im = Image.open(image)
        newImage = image.replace(convertFrom, convertTo)
        im.save(newImage)


def converToTex(images):
    """convert to tex"""
    for image in images:
        # txMakeStr = 
        pass


def convertToRat(images, origType, newType):
    for image in images:
        iconvert = binary.getBinary("iconvert")
        cmd = '{} {} {}'.format(iconvert, image, image.replace(origType, newType))
        os.system(cmd)

def convertToImaketx(images,origType,newType):

# imaketx -v -m ocio --format RAT `@directory`/`@filename``@extension` `@directory`/`@filename`.rat
    for image in images:
        imaketx = binary.getBinary("imaketx")
        cmd = '{} -v -m ocio --format RAT {} {}'.format(imaketx, image, image.replace(origType, newType))
        os.system(cmd)


def createProxy(inDir, destDir, fileType):
    for dr in os.listdir(inDir):
        currentDir = os.path.join(inDir, dr)
        if os.path.isdir(currentDir):
            newDir = os.path.join(destDir, os.path.basename(currentDir) + '_proxy')
            if not os.path.exists(newDir):
                os.mkdir(newDir)
                
            for img in osutils.getFileOfType(currentDir, fileType):
                image = Image.open(img)
                size = image.size
                image.thumbnail((size[0]/2, size[1]/2))
                image.save(img.replace(currentDir, newDir))
                
                

    
# imageDir = "D:/HOUDINI_RND/RND/xyz__batchtexconvert_examples/examples/example_images/example_image_batch_1"
# images = osUtils.getFileOfType(imageDir, "*jpg")
# print(images)
# convertToRat(images, "jpg", "rat")

# def convert_exr_to_jpg(exr_file, jpg_file):
#     input_image = oiio.ImageInput.open(exr_file)
#     spec = input_image.spec()
#     width = spec.width
#     height = spec.height

#     # Create a blank JPG image with the same resolution
#     output_image = oiio.ImageOutput.create(jpg_file)
#     output_image.open(jpg_file, width, height, 3, oiio.UINT8)

#     # Read EXR channels and write to the JPG image
#     image_buffer = oiio.ImageBuf(exr_file)
#     output_image.write_image(image_buffer)

#     input_image.close()
#     output_image.close()

# # Usage example
# exr_file = "input.exr"
# jpg_file = "output.jpg"
# convert_exr_to_jpg(exr_file, jpg_file)


# # EXR 파일을 읽어옴
# exr_path = 'input.exr'
# exr_file = OpenEXR.InputFile(exr_path)
# exr_header = exr_file.header()

# # 이미지 크기와 데이터 타입을 가져옴
# dw = exr_header['dataWindow']
# width = dw.max.x - dw.min.x + 1
# height = dw.max.y - dw.min.y + 1
# channel_format = exr_header['channels']['R'].type

# # EXR 데이터를 읽어옴
# exr_data = exr_file.channels('RGB', channel_format)

# # RGB 데이터를 이미지로 변환
# image_data = [Image.frombytes('F', (width, height), exr_data[c]) for c in ['R', 'G', 'B']]
# image = Image.merge('RGB', image_data)

# # PNG 파일로 저장
# output_path = 'output.png'
# image.save(output_path)

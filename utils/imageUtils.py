from PIL import Image
import binary
import osUtils
import os

# import OpenImageIO as oiio
# import OpenEXR


def convertImage(images, convertFrom, convertTo):
    for image in images:
        im = Image.open(image)
        newImage = image.replace(convertFrom, convertTo)
        im.save(newImage)


def convertToRat(images, origType, newType):
    for image in images:
        iconvert = binary.getBinary("iconvert")
        # cmd = "start {}".format(txMakeStr)
        cmd = '"{}" {} {}'.format(iconvert, image, image.replace(origType, newType))
        print(cmd)
        os.system(cmd)


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

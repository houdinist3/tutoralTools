import imageUtils
import osutils


imageDir = "D:/HOUDINI_RND/PYRO/tex/Volcanic"


def main(imageDir, fileType, convertTo):
    images = osutils.getFileOfType(imageDir, fileType)
    print(images)
    imageUtils.convertImage(images, fileType, convertTo)


if __name__ == "__main__":
    main(imageDir, "jpg", "png")

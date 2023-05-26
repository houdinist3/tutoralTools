import platform, os, os.path


houdini_binPath = "C:/Program Files/Side Effects Software/Houdini 19.5.368/bin"


def getBinary(binary):
    # Locate Houdini root path
    root = None
    binary_folder = None
    executable = None
    slash = None

    # Determine OS filepaths
    if platform.system() == "Linux":
        # root = hou.houdiniPath()[2]
        root = houdini_binPath
        slash = "/"
        binary_folder = slash + "bin" + slash
        executable = binary + " "

        # Linux houdini root path is /opt/hfs{version}/houdini
        # We need to slash /houdini
        root = root.rpartition(slash)[0]

    # Filepath for windows
    elif platform.system() == "Windows":
        # root = hou.houdiniPath()[3]
        root = houdini_binPath
        root.replace("/", "\\")
        slash = "/"
        binary_folder = slash
        executable = binary + ".exe"

    # Filepath for Mac untested
    elif platform.system() == "Darwin":
        print("mac")

    else:
        print("Unable to determine OS")

    # binary executable string
    binary_string = root + binary_folder + executable
    # print(binary_string)
    return binary_string


# getBinary("iconvert")

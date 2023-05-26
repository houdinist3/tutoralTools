import osUtils

help(osUtils)


usdDir = "D:/HOUDINI_RND/environment_USD/usd/usd_examples"

for data in osUtils.getFileOfType(usdDir, "usd"):
    print(data)

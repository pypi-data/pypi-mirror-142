# import zipfile as z
##with z.ZipFile("test.pylearner", "w", z.ZIP_DEFLATED) as zf:
#
##    zf.write("新建文本文档.txt","新建文本文档.txt")
# with z.ZipFile("test.pylearner") as zf:
#    zf.extractall()
import pylearner.loader as l
l.__loadZipFile("test")
print(l.__loadJson("test")["pylearner"]["title"])


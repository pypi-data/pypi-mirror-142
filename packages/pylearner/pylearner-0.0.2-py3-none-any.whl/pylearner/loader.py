import zipfile as zip
import json
import os
import pylearner.exception as ex


def __loadJson(jsonFile) -> str:
    try:
        text = open("packages\\temp\\%s\\%s.json" % (jsonFile,jsonFile), "r").read()
    except FileNotFoundError:
        raise ex.JsonNotFoundError("couldn't open packages\\temp\\%s\\%s.json file,"
                                   "please check your path" % (jsonFile,jsonFile))
    return json.loads(text)


def __loadZipFile(zipFile) -> str:
    loadedPath = "packages\\temp\\%s" % zipFile
    with zip.ZipFile("packages\\%s.pylearner" % zipFile) as zf:
        if (not os.path.isdir(loadedPath)) or (not os.path.isdir("packages\\temp")):
            os.makedirs(loadedPath)
        zf.extractall(path=loadedPath)


def load(package):
    pass

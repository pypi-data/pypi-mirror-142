"""
indi game engine
"""

import os.path
import subprocess as sp
import pkg_resources

from _igeEffekseer import *

textures = {}
def f_texture_loader(name, type):
    print('f_texture_loader - ' + name)
    tex = core.texture(name)
    textures[name] = tex
    return (tex.width, tex.height, tex.id, tex.numMips > 1)

try:
    dist = pkg_resources.get_distribution('igeCore')
    print('{} ({}) is installed'.format(dist.key, dist.version))
    import igeCore as core
    texture_loader(f_texture_loader)
except pkg_resources.DistributionNotFound:
    print('{} is NOT installed'.format('igeCore'))


def isHiddenFolder(path):
    if path.find('/.') != -1 or path.find('\\.') != -1 :
        return True
    return False

def findEfkfcFiles(path):
    list = []
    for root, dirs, files in os.walk(path):
        if isHiddenFolder(root): continue
        for fname in files:
            name, ext = os.path.splitext(fname)
            if ext == '.efkefc':
                list.append(os.path.join(root, fname))
    return list

def replaceExt(file, ext):
    name, extold = os.path.splitext(file)
    return name + ext

def openEditor():
    dirname = os.path.dirname(__file__)
    exePath = os.path.join(dirname, "Tool/Effekseer.exe")
    sp.run(exePath)

def exportEfk(inputFile, outputFile):
    dirname = os.path.dirname(__file__)
    exePath = os.path.join(dirname, "Tool/Effekseer.exe")
    cl = exePath + " -cui -in "+ inputFile  + " -e " + outputFile
    sp.run(cl)


def exportAllEfk(sourceDir, destDir):
    effList = findEfkfcFiles(sourceDir)

    for file in effList:
        print("convert : " + file)
        outfile = os.path.normpath(file.replace(sourceDir, destDir, 1))
        outfile = replaceExt(outfile, '.efk')
        exportEfk(file, outfile)

import rawpy
import imageio
import glob, os

path = "F/*.CR2"
fotos = glob.glob(path)

for file in fotos:
    raw = rawpy.imread(file)
    rgb = raw.postprocess(use_auto_wb=True)
    imageio.imsave(file+'.png', rgb)


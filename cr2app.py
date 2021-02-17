import rawpy
import imageio
import glob, os

path = "F/*.CR2" #rawfile #o seu arquivo direto da camera.
fotos = glob.glob(path)

for file in fotos:
    raw = rawpy.imread(file)
    rgb = raw.postprocess(use_auto_wb=True)
    imageio.imsave(file+'.png', rgb) #maybe same folder #ou voce pode mudar as pastas se quiser.


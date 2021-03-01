

""" cr2app++.py
    Credit: Rodrigo Sparrapan
    sparodrigo82@gmail.com """

import rawpy
import imageio
import glob, os
import cv2
import glob as glob



count = 1

path = "ToMinistery/drive/*CR2.jpg" 
path = "ToMinistery/drive/*.jpg" 
path = "ToMinistery/drive/*.JPG" 
filenames = glob.glob(path)

for filename in filenames:
        
        image = cv2.imread(filename)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #image = cv2.resize(image, (6000, 40000))
        #image = cv2.imread(image)
        #gray_img = cv2.resize(gray_img, (6000, 4000))
    
        cv2.imwrite("ToMinistery/drive/_gray_" +str(count) +".jpg", gray_img)
        cv2.imwrite("ToMinistery/drive/_color_" +str(count) +".jpg", image)
    
        count += 1

#maybe same folder #ou voce pode mudar as pastas se quiser.
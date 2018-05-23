"""
#Human
if np.array_equal(raw_image[y, x], [220, 20, 60]):
elif np.array_equal(raw_image[y, x], [1255, 0, 0]):
#Vehicle
elif raw_image[x, y] == [119, 11, 32]:
elif raw_image[x, y] == [0, 0, 142]:
elif raw_image[x, y] == [0, 60, 100]:
elif raw_image[x, y] == [0, 0, 90]:
elif raw_image[x, y] == [0, 0, 230]:
elif raw_image[x, y] == [0, 80, 100]:
elif raw_image[x, y] == [128, 64, 64]:
elif raw_image[x, y] == [0, 0, 110]:
elif raw_image[x, y] == [0, 0, 70]:
elif raw_image[x, y] == [0, 0, 192]:
"""
    
from PIL import Image
from os import listdir
import numpy as np
from keras.utils import to_categorical
import cv2

INPUT_FOLDER = "./vista/labels/"
OUTPUT_FOLDER = "./vista/CLEAN-labels/"

list = listdir(INPUT_FOLDER)

for file in list:
    #Open raw synthia class file
    #raw_image = cv2.imread(INPUT_FOLDER + file, cv2.IMREAD_UNCHANGED)
    raw_image = np.array(Image.open(INPUT_FOLDER + file))
    #Start a clean map
    #cleaned_map = np.zeros((raw_image.shape[0],raw_image.shape[1],1), np.uint8)
    
        
    expanded_image = to_categorical(raw_image, 66)
    #expanded_image = expanded_image.reshape(raw_image.shape[1], raw_image.shape[0], 23)
    
    human = expanded_image[:,:,19] + expanded_image[:,:,20] + expanded_image[:,:,21] + expanded_image[:,:,22]
    
    vehicle = (expanded_image[:,:,52] + expanded_image[:,:,53] + expanded_image[:,:,54] + expanded_image[:,:,55] + expanded_image[:,:,56] + expanded_image[:,:,57] + expanded_image[:,:,58] + expanded_image[:,:,59] + expanded_image[:,:,60] + expanded_image[:,:,61] + expanded_image[:,:,62]) * 2
              
    cleaned_map = human + vehicle

    
    #Save cleaned map
    cv2.imwrite(OUTPUT_FOLDER + file, cleaned_map)
    #cleaned_map.save(OUTPUT_FOLDER + '/' + file, "PNG", compress_level=0)
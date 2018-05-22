from os import listdir
import cv2
import numpy as np
from keras.utils import to_categorical

INPUT_FOLDER = "./synthia/train/labels"
OUTPUT_FOLDER = "./synthia/train/CLEAN-labels"

#List all files
list = listdir(INPUT_FOLDER)

for file in list:
    #Open raw synthia class file
    raw_image = cv2.imread(INPUT_FOLDER + '/' + file, cv2.IMREAD_UNCHANGED)[:,:,2]
    
    #Start a clean map
    #cleaned_map = np.zeros((raw_image.shape[0],raw_image.shape[1],1), np.uint8)
    
        
    expanded_image = to_categorical(raw_image, 23)
    #expanded_image = expanded_image.reshape(raw_image.shape[1], raw_image.shape[0], 23)
    
    human = expanded_image[:,:,10] + expanded_image[:,:,17]
    
    vehicle = (expanded_image[:,:,8] + expanded_image[:,:,11] + expanded_image[:,:,12] + expanded_image[:,:,18] + expanded_image[:,:,19] + expanded_image[:,:,20]) * 2
              
    cleaned_map = human + vehicle

    
    #Save cleaned map
    cv2.imwrite(OUTPUT_FOLDER + '/' + file, cleaned_map)
    #cleaned_map.save(OUTPUT_FOLDER + '/' + file, "PNG", compress_level=0)
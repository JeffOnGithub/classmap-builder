from PIL import Image
from os import listdir
import numpy as np
from keras.utils import to_categorical
import cv2

INPUT_FOLDER = "Z:/transfert_test/train_real/maps_resized/"
OUTPUT_FOLDER = "Z:/transfert_test/train_real/maps_resized_binary_roads/"

list = listdir(INPUT_FOLDER)

for file in list:
    #Open raw synthia class file
    #raw_image = cv2.imread(INPUT_FOLDER + file, cv2.IMREAD_UNCHANGED)
    raw_image = np.array(Image.open(INPUT_FOLDER + file))
    #Start a clean map
    #cleaned_map = np.zeros((raw_image.shape[0],raw_image.shape[1],1), np.uint8)
    
        
    expanded_image = to_categorical(raw_image, 66)
    #expanded_image = expanded_image.reshape(raw_image.shape[1], raw_image.shape[0], 23)
    
    #human = expanded_image[:,:,19] + expanded_image[:,:,20] + expanded_image[:,:,21] + expanded_image[:,:,22]
    
    #vehicle = (expanded_image[:,:,52] + expanded_image[:,:,53] + expanded_image[:,:,54] + expanded_image[:,:,55] + expanded_image[:,:,56] + expanded_image[:,:,57] + expanded_image[:,:,58] + expanded_image[:,:,59] + expanded_image[:,:,60] + expanded_image[:,:,61] + expanded_image[:,:,62]) * 2
     
    #7-Bike lanes, 8-Crosswalk - Plain, 10-Parking, 13-Road, 14-Service Lane, 23-Lane Marking - Crosswalk, 
    #24-Lane Marking - General, 43-Pothole, 12-Rail Track
    roads = expanded_image[:,:,7] + \
            expanded_image[:,:,8] + \
            expanded_image[:,:,10] + \
            expanded_image[:,:,12] + \
            expanded_image[:,:,13] + \
            expanded_image[:,:,14] + \
            expanded_image[:,:,23] + \
            expanded_image[:,:,24] + \
            expanded_image[:,:,43]         
    
    cleaned_map = roads

    
    #Save cleaned map
    cv2.imwrite(OUTPUT_FOLDER + file, cleaned_map)
    #cleaned_map.save(OUTPUT_FOLDER + '/' + file, "PNG", compress_level=0)
from PIL import Image
from os import listdir
import numpy as np
from keras.utils import to_categorical
import cv2
from os import environ

environ["CUDA_VISIBLE_DEVICES"] = '1'

INPUT_FOLDER = "Z:/transfert_test/test_real/maps_resized_binary_roads/"

list = listdir(INPUT_FOLDER)

total_of_files = 0
total_of_averages = 0

for file in list:
    #Open raw synthia class file
    #raw_image = cv2.imread(INPUT_FOLDER + file, cv2.IMREAD_UNCHANGED)
    raw_image = np.array(Image.open(INPUT_FOLDER + file))
    expanded_image = to_categorical(raw_image, 2)

    roads = np.sum(expanded_image[:,:,1])
    total_pixels = 1280 * 760
    
    total_of_files = total_of_files + 1
    total_of_averages = total_of_averages + (roads / total_pixels)
    
print(total_of_averages/total_of_files)
    
#Result with real roads test: 22.25%, 77.75% non-road sections
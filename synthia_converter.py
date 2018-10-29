from os import listdir
import cv2
import numpy as np
from keras.utils import to_categorical

INPUT_FOLDER = "Z:/transfert_test/train_syn/maps/"
OUTPUT_FOLDER = "Z:/transfert_test/train_syn/maps_binary_roads/"

#List all files
list = listdir(INPUT_FOLDER)

for file in list:
    #Open raw synthia class file
    raw_image = cv2.imread(INPUT_FOLDER + file, cv2.IMREAD_UNCHANGED)[:,:,2]
    
    #Start a clean map
    #cleaned_map = np.zeros((raw_image.shape[0],raw_image.shape[1],1), np.uint8)
    
        
    expanded_image = to_categorical(raw_image, 23)
    #expanded_image = expanded_image.reshape(raw_image.shape[1], raw_image.shape[0], 23)
    
    #human = expanded_image[:,:,10] + expanded_image[:,:,17]
    
    #vehicle = (expanded_image[:,:,8] + expanded_image[:,:,11] + expanded_image[:,:,12] + expanded_image[:,:,18] + expanded_image[:,:,19] + expanded_image[:,:,20]) * 2
              
    #Road, parking slots and lanemarking
    roads = expanded_image[:,:,3] + expanded_image[:,:,13] + expanded_image[:,:,22]
    
    cleaned_map = roads

    
    #Save cleaned map
    cv2.imwrite(OUTPUT_FOLDER + file, cleaned_map)
    print(OUTPUT_FOLDER + file)
    #cleaned_map.save(OUTPUT_FOLDER + '/' + file, "PNG")
    
#Class			R	G	B	ID
#void			0	0	0	0
#sky			70	130	180	1
#Building		70	70	70	2
#Road			128	64	128	3
#Sidewalk		244	35	232	4
#Fence			64	64	128	5
#Vegetation		107	142	35	6
#Pole			153	153	153	7
#Car			0	0	142	8
#Traffic sign	220	220	0	9
#Pedestrian		220	20	60	10
#Bicycle		119	11	32	11
#Motorcycle		0	0	230	12
#Parking-slot	250	170	160	13
#Road-work		128	64	64	14
#Traffic light	250	170	30	15
#Terrain		152	251	152	16
#Rider			255	0	0	17
#Truck			0	0	70	18
#Bus			0	60	100	19
#Train			0	80	100	20
#Wall			102	102	156	21
#Lanemarking	102	102	156	22
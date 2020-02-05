from PIL import Image
from os import listdir
import numpy as np
from keras.utils import to_categorical
import cv2

INPUT_FOLDER = "Z:/transfert_test/train_gta5/maps/"
OUTPUT_FOLDER = "Z:/transfert_test/train_gta5/maps_binary_roads/"

list = listdir(INPUT_FOLDER)

for file in list:
    #Open raw synthia class file
    #raw_image = cv2.imread(INPUT_FOLDER + file, cv2.IMREAD_UNCHANGED)
    raw_image = np.array(Image.open(INPUT_FOLDER + file))
    #Start a clean map
    #cleaned_map = np.zeros((raw_image.shape[0],raw_image.shape[1],1), np.uint8)
        
    expanded_image = to_categorical(raw_image, 51)
    #expanded_image = expanded_image.reshape(raw_image.shape[1], raw_image.shape[0], 23)

    roads = expanded_image[:,:,7]       
    
    cleaned_map = roads

    
    #Save cleaned map
    cv2.imwrite(OUTPUT_FOLDER + file, cleaned_map)
    #cleaned_map.save(OUTPUT_FOLDER + '/' + file, "PNG", compress_level=0)
    
"""
CamVid Classes

64 128 64	Animal
192 0 128	Archway
0 128 192	Bicyclist
0 128 64	Bridge
128 0 0		Building
64 0 128	Car
64 0 192	CartLuggagePram
192 128 64	Child
192 192 128	Column_Pole
64 64 128	Fence
128 0 192	LaneMkgsDriv
192 0 64	LaneMkgsNonDriv
128 128 64	Misc_Text
192 0 192	MotorcycleScooter
128 64 64	OtherMoving
64 192 128	ParkingBlock
64 64 0		Pedestrian
128 64 128	Road
128 128 192	RoadShoulder
0 0 192		Sidewalk
192 128 128	SignSymbol
128 128 128	Sky
64 128 192	SUVPickupTruck
0 0 64		TrafficCone
0 64 64		TrafficLight
192 64 128	Train
128 128 0	Tree
192 128 192	Truck_Bus
64 0 64		Tunnel
192 192 0	VegetationMisc
0 0 0		Void
64 192 0	Wall

Void		0 	0 	0
Building 	128 	0 	0
XXgrass		0 128 0
Tree		128 	128 	0
XXcow		0 0 128
XXhorse		128 0 128
XXsheep		0 128 128
Sky		128 	128 	128
XXmountain	64 0 0
XXaeroplane	192 0 0
XXwater		64 128 0
XXface		192 128 0
Car		64 	0 	128
Archway		192 	0 	128
XXflower	64 128 128
SignSymbol	192 	128 	128
XXbird		0 64 0
XXbook		128 64 0
XXchair		0 192 0
XXmotorbike	128 192 0
XXperson	0 64 128
Road		128 	64 	128
XXcat		0 192 128
XXdog		128 192 128
Pedestrian	64 	64 	0
XXboat		192 64 0
Wall		64 	192 	0
VegetationMisc	192 192 0
Fence		64 	64 	128
Train		192 64 128
ParkingBlock	64 192 128
Column_Pole	192 192 128
TrafficCone	0 0 64
XXunused	128 0 64
Bridge		0 128 64
Misc_Text	128 128 64
Sidewalk	0 0 192
LaneMkgsDriv	128 0 192
Bicyclist	0 128 192
RoadShoulder	128 128 192
Tunnel		64 0 64
LaneMkgsNonDriv	192 0 64
Animal		64 128 64
Child		192 128 64
CartLuggagePram	64 0 192
MotorcycleScooter	192 0 192
SUVPickupTruck	64 128 192
Truck_Bus	192 128 192
TrafficLight	0 64 64
OtherMoving	128 64 64
"""
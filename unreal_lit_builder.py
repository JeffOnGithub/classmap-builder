from PIL import Image
from os import listdir
import numpy as np
import multiprocessing

INPUT_FOLDER = "Z:/Unreal_Datasets/Meadow1/Labels/"
OUTPUT_FOLDER = "Z:/Unreal_Datasets/Meadow1/Labels_Categorical/"

INTENSITY_TRESHOLD = 50

def process(file):
    
    #Open raw map
    raw_map = Image.open(INPUT_FOLDER + file)
    pixdata_raw = raw_map.load()
    map_width, map_height = raw_map.size
    #raw_map.show()
    
    #Build a cleaned map
    cleaned_map = Image.new('L', (map_width, map_height), 255)
    pixdata_cleaned = cleaned_map.load()
    #cleaned_map.show()
    
    """
    
    Classes
    
    R,G,B
    1,0,1   Pink	Rocks
    0,1,0   Green	Trees
    0,1,1   Cyan	Groundwook
    1,0,0   Red	    Groundplants
    1,1,0   Yellow	BLUEBERRIES
    0,0,1   Blue	Water
    0,0,0   White	Ground
    1,1,1   Black	Sky
    
    """
    
    #Loop all pixels to establish correct class
    for y in range(map_height):
        for x in range(map_width):
            #White
            if pixdata_raw[x, y] == (255, 255, 255, 255):
                pixdata_cleaned[x, y] = 0
            #Black
            elif pixdata_raw[x, y] == (0, 0, 0, 255):
                pixdata_cleaned[x, y] = 1
            #Yellow
            elif pixdata_raw[x, y] == (255, 255, 0, 255):
                pixdata_cleaned[x, y] = 2
            #Cyan
            elif pixdata_raw[x, y] == (0, 255, 255, 255):
                pixdata_cleaned[x, y] = 3
            #Pink
            elif pixdata_raw[x, y] == (255, 0, 255, 255):
                pixdata_cleaned[x, y] = 4
            #Red
            elif pixdata_raw[x, y] == (255, 0, 0, 255):
                pixdata_cleaned[x, y] = 5
            #Green
            elif pixdata_raw[x, y] == (0, 255, 0, 255):
                pixdata_cleaned[x, y] = 6
            #Blue
            elif pixdata_raw[x, y] == (0, 0, 255, 255):
                pixdata_cleaned[x, y] = 7

    
    #Save cleaned map
    cleaned_map.save(OUTPUT_FOLDER + file, "PNG", compress_level=0)
    #cleaned_map.show()
    
    return file

if __name__ == '__main__':
    list = listdir(INPUT_FOLDER)
    with multiprocessing.Pool(16) as p:
        print(p.map(process, list) )
    
    

from PIL import Image
from os import listdir
import multiprocessing

INPUT_FOLDER = "Z:/Unreal_Datasets/unrealmeadow/Images_Categorical/"
OUTPUT_FOLDER = "Z:/Unreal_Datasets/unrealmeadow/Images_Categorical_PNG/"

INTENSITY_TRESHOLD = 50

def process(file):
    
    if file[-4:] == '.png':
        raw_map = Image.open(INPUT_FOLDER + file)    
        raw_map.save(OUTPUT_FOLDER + file, "PNG", compress_level=9)

    if file[-4:] == '.jpg':
        raw_map = Image.open(INPUT_FOLDER + file)    
        #raw_map.save(OUTPUT_FOLDER + file, "jpeg", quality=75)
        raw_map.save(OUTPUT_FOLDER + file, "PNG", compress_level=9)
        
    return file

if __name__ == '__main__':
    list = listdir(INPUT_FOLDER)
    with multiprocessing.Pool(16) as p:
        print(p.map(process, list) )
    
    

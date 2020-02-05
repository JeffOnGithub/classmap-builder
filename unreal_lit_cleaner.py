from PIL import Image
from os import listdir
import numpy as np
import multiprocessing

INPUT_FOLDER = "Z:/Unreal_Datasets/Meadow1/Labels_Originals/"
OUTPUT_FOLDER = "Z:/Unreal_Datasets/Meadow1/Labels/"

INTENSITY_TRESHOLD = 50

def process(file):
    
    #Open raw class file
    raw_image = np.array(Image.open(INPUT_FOLDER + file))
    
    raw_image = np.where(raw_image > 50, 255, 0)
    
    #Save image
    im = Image.fromarray(raw_image.astype('uint8'))
    im.save(OUTPUT_FOLDER + file)
    
    return file

if __name__ == '__main__':
    list = listdir(INPUT_FOLDER)
    with multiprocessing.Pool(16) as p:
        print(p.map(process, list) )


    
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


# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:10:21 2019

@author: Jeff
"""

from PIL import Image
from os import listdir
import os
import numpy as np
import multiprocessing

LABELS_FOLDER = "Z:/Unreal_Datasets/Meadow1/Labels_Categorical/"

INPUT_FOLDER = "Z:\\Unreal_Datasets\\Meadow1\\Images_Originals\\"
OUTPUT_FOLDER = "Z:\\Unreal_Datasets\\Meadow1\\Images_Categorical\\"


#files_list = listdir(INPUT_FOLDER)
labels_list = listdir(LABELS_FOLDER)

#os.system('cd ' + TYPE_OF_SET + ' && copy /Y ' + full_source_path + ' ' + '".' + full_dest_path + '"')

for label_file in labels_list:
    image_file = label_file[:-4] + '.jpg'
    command = 'cd ' + INPUT_FOLDER + ' && copy /Y ' + image_file + ' ' + OUTPUT_FOLDER
    #print(command)
    os.system(command)
    #break
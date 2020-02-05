# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:42:05 2019

@author: Jeff
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:10:21 2019

@author: Jeff
"""

from os import listdir
from sklearn.model_selection import train_test_split



LABELS_FOLDER = "Z:/Unreal_Datasets/Meadow1/Labels_Categorical/"
SAVE_TO_FOLDER = "Z:/Unreal_Datasets/Meadow1/"

labels_list = listdir(LABELS_FOLDER)

X_train, X_test = train_test_split(labels_list, test_size=0.1)

#Remove files extension when saving
#All files
with open(SAVE_TO_FOLDER + 'list.txt', 'a') as file:
    for value in labels_list:
        file.write(value[:-4] + '\n')
        
#Train set
with open(SAVE_TO_FOLDER + 'trainval.txt', 'a') as file:
    for value in X_train:
        file.write(value[:-4] + '\n')
        
#Test set
with open(SAVE_TO_FOLDER + 'test.txt', 'a') as file:
    for value in X_test:
        file.write(value[:-4] + '\n')
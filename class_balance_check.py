from PIL import Image

NUMBER_OF_IMGS = 305

INPUT_FOLDER = "./Maps/"
OUTPUT_IMGS_FOLDER = "./Output/Images/"
OUTPUT_MAPS_FOLDER = "./Output/Maps/" 
FILE_EXT = ".png"
IDS_FILE_PATH = "./Output/id.txt"

class_total = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, NUMBER_OF_IMGS):
    raw_map = Image.open(INPUT_FOLDER + str(i).zfill(5) + FILE_EXT)
    pixdata_raw = raw_map.load()
    map_width, map_height = raw_map.size
    #raw_map.show()
    
    #Build a cleaned map
    cleaned_map = Image.new('L', (map_width, map_height), 255)
    pixdata_cleaned = cleaned_map.load()
    #cleaned_map.show()
 
    #Loop all pixels to establish correct class
    for y in range(map_height):
        for x in range(map_width):
            class_total[pixdata_raw[x, y]] = class_total[pixdata_raw[x, y]] + 1
     
        
print(class_total)
for each_class in class_total:
    print(1 / (each_class / sum(class_total)))
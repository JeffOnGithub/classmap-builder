from PIL import Image
import os

NUMBER_OF_IMGS = 240

INPUT_FOLDER = "./Input/HighresScreenshot"
OUTPUT_IMGS_FOLDER = "./Output/Images/"
OUTPUT_MAPS_FOLDER = "./Output/Maps/" 
FILE_EXT = ".png"
IDS_FILE_PATH = "./Output/id.txt"

for i in range(0, NUMBER_OF_IMGS):
    
    if (i % 2 == 0):
    #Even numbers are images, copy them
        #All hacked up to work!
        full_source_path = "HighresScreenshot" + str(i).zfill(5) + FILE_EXT
        full_dest_path = OUTPUT_IMGS_FOLDER + str(int(i / 2)).zfill(5) + FILE_EXT
        os.system('cd Input && copy /Y ' + full_source_path + ' ' + '".' + full_dest_path + '"')
    else:
    #Odd numbers are maps, clean them and save them 
        #Open raw map
        raw_map = Image.open(INPUT_FOLDER + str(i).zfill(5) + FILE_EXT)
        pixdata_raw = raw_map.load()
        map_width, map_height = raw_map.size
        #raw_map.show()
        
        #Build a cleaned map
        cleaned_map = Image.new('L', (map_width, map_height), 255)
        pixdata_cleaned = cleaned_map.load()
        #cleaned_map.show()
        
        #0 White - Ground
        #1 Black - Rock
        #2 Yellow - Flower
        #3 Cyan - Fern
        #4 Pink - Tree
        #5 Red - Myrtle
        #6 Green - Grass
        #7 Blue - Bush
        #Loop all pixels to establish correct class
        for y in range(map_height):
            for x in range(map_width):
                #White
                if pixdata_raw[x, y][0] >= 200 and pixdata_raw[x, y][1] >= 100 and pixdata_raw[x, y][2] >= 100:
                    pixdata_cleaned[x, y] = 0
                #Black
                elif pixdata_raw[x, y][0] <= 100 and pixdata_raw[x, y][1] <= 100 and pixdata_raw[x, y][2] <= 100:
                    pixdata_cleaned[x, y] = 1 #31
                #Yellow
                elif pixdata_raw[x, y][0] >= 100 and pixdata_raw[x, y][1] >= 100 and pixdata_raw[x, y][2] <= 100:
                    pixdata_cleaned[x, y] = 2 #63
                #Cyan
                elif pixdata_raw[x, y][0] <= 200 and pixdata_raw[x, y][1] >= 100 and pixdata_raw[x, y][2] >= 100:
                    pixdata_cleaned[x, y] = 3 #95
                #Pink
                elif pixdata_raw[x, y][0] >= 100 and pixdata_raw[x, y][1] <= 100 and pixdata_raw[x, y][2] >= 100:
                    pixdata_cleaned[x, y] = 4 #127
                #Red
                elif pixdata_raw[x, y][0] >= 100 and pixdata_raw[x, y][1] <= 100 and pixdata_raw[x, y][2] <= 100:
                    pixdata_cleaned[x, y] = 5 #159
                #Green
                elif pixdata_raw[x, y][0] <= 100 and pixdata_raw[x, y][1] >= 100 and pixdata_raw[x, y][2] <= 100:
                    pixdata_cleaned[x, y] = 6 #223
                #Blue
                elif pixdata_raw[x, y][0] <= 100 and pixdata_raw[x, y][1] <= 100 and pixdata_raw[x, y][2] >= 100:
                    pixdata_cleaned[x, y] = 7 #191

        
        #Save cleaned map
        cleaned_map.save(OUTPUT_MAPS_FOLDER + str(int(i / 2)).zfill(5) + FILE_EXT, "PNG", compress_level=0)
        #cleaned_map.show()
        
#Generate id list
with open(IDS_FILE_PATH, "w") as text_file:
    for a in range(0, int(NUMBER_OF_IMGS / 2)): 
        print(str(a).zfill(5), file=text_file)
print("Program Started\nImporting Shit")
import random # random num generator
from time import sleep # timer to wait
#import colorama # will add late for some color just to make teminal nice to look at lol
import requests # request img from web
import shutil # save img locally
import os # basic commands
from PIL import Image # Imports PIL module  
timer = 30 # Wait time
repeat = 5 # amout of times it downloads itself lol
print("Import Complete")

#file_name = input('Save image as (string):') # prompt user for file name THIS IS TEMPERARY
# gunna make "file_name" = "gaysex-[random int 1-100000]"
# this will make the program be able to create(download) multiplle images of itself :)

#chooses Url to grab image from (USE IMAGE ADRESS)
#urlnum = (4)
#if urlnum == 1:
url = "https://steamuserimages-a.akamaihd.net/ugc/1824532753041605480/9A6C19AD80E2DBA6ECC00682A6FE692ED178247E/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false"
#elif urlnum == 2:
    #url = "https://media.discordapp.net/attachments/1136817826003435622/1166569824575561868/heart.png?ex=654af7cf&is=653882cf&hm=e2662cfe3898c45b541c04389e537d5bea025f9959b27382cbc3f5d4826b0ab3&="
#elif urlnum == 3:
    #url = "https://cdn.discordapp.com/attachments/1158233957326930040/1166510324489404528/v09044g40000c9o0ijbc77uac0nj7cvg.mov?ex=654ac066&is=65384b66&hm=cdc4ff128ad4c001b68a00aa7f2d1f5dfb7c314c339385a6fce85018b4981ad5&"
res = requests.get(url, stream = True)

print("Startup Complete")
def imagedownloader(imageurl):
    print("you called imagedownloader")
    imagenumber = (random.randint(1, 100000)) # Image Id number
    file_name = "testimage-" + str(imagenumber) + ".jpg" # Image namer thing
    #--------------
    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',file_name) #YIPEEE
    else:
        print('Image Couldn\'t be retrieved') #prints if the image adress is invalid
    #--------------
    # open method used to open different extension image file 
    print("pretest")
    filelocation = "D:\.D.Downloads\SomeDumbassProgram"# + file_name #CHANGE IT TO YOUR OWN DOWNLOAD'S SLOT OR PLACE YOU WANT IMAGES TO GO
    #im = Image.open(filelocation) # Not needed anymore but kept because I can
    im = Image.open(r"D:\.D.Downloads\SomeDumbassProgram\" + file_name) #set this to sumthin i forget its been 11 hours
    im.show()  #shows imgae that it downloaded
    #--------------
    print(x)
x = 1
for x in range(repeat):
    x = x + 1
    imagedownloader(url)


# Created by BobTheChickenPlzHelp on GitHub
# https://github.com/BobTheChickenPlzHelp/imageopener

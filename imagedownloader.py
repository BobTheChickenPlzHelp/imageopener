print("Program Started\nImporting Shit")
import random # random num generator
from time import sleep # timer to wait
#import colorama # will add late for some color just to make teminal nice to look at lol
import requests # request img from web
import shutil # save img locally
import os # basic commands
from PIL import Image # Imports PIL module  
timer = 30 #
repeat = 10
print("Import Complete")

#file_name = input('Save image as (string):') # prompt user for file name THIS IS TEMPERARY
# gunna make "file_name" = "gaysex-[random int 1-100000]"
# this will make the program be able to create(download) multiplle images of itself :)
url = "https://steamuserimages-a.akamaihd.net/ugc/1824532753041605480/9A6C19AD80E2DBA6ECC00682A6FE692ED178247E/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false"
res = requests.get(url, stream = True)

print("Startup Complete")
def imagedownloader(imageurl):
    print("you called imagedownloader")
    imagenumber = (random.randint(1, 100000))
    file_name = "testimage-" + str(imagenumber) + ".jpg"
    
    #--------------
    # WILL ADD CODE LATER FOR NOW THIS STAYS EMPTY CUZ IM FUCKING LAZY
    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')
    #--------------
    
    # open method used to open different extension image file 
    print("pretest")
    filelocation = "D:\.D.Downloads\SomeDumbassProgram" + file_name
    #im = Image.open(filelocation) 
    im = Image.open(r"D:\.D.Downloads\SomeDumbassProgram\imagetest.jpg")
    im.show()  

    
    #--------------
    
    
    #r = requests.get('https://steamuserimages-a.akamaihd.net/ugc/1824532753041605480/9A6C19AD80E2DBA6ECC00682A6FE692ED178247E/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false')
    #'Requests:' in r.text
x = 1
for x in range(repeat):
    x = x + 1
    imagedownloader(url)


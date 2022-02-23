from PIL import Image
import os

from jinja2 import FileSystemLoader

files = os.listdir(
    "C:\\Users\\USER\\Desktop\\PersonalFold\\nftstuff\\pixelPUP\\FinalNFTS")
n = 1
for i in range(0,len(sorted(files))):
    if i == 500:
        break
    else:
        bgimg = Image.open("C:\\Users\\USER\\Desktop\\PersonalFold\\nftstuff\\pixelPUP\\bg.png")
        path1 = "C:\\Users\\USER\\Desktop\\PersonalFold\\nftstuff\\pixelPUP\\FinalNFTS" + "\\"+files[i]
        img = Image.open(path1)
        bgimg.paste(img,(487,620))
        path2 = "C:\\Users\\USER\\Desktop\\PersonalFold\\nftstuff\\pixelPUP\\UnlockableContentcards"+"\\"+"MicroPuppiesNFTCARD#"+str(n)+".png"
        bgimg.save(path2)
        n+=1

        
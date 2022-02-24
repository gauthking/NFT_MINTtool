## NOT A Big Brain CODE XD, just a GUI Automator tool made using pyautogui python library.

## THIS CODE IS A PERSONAL PROJECT AND DO NOT USE IT AS IT HAS GUI COORDINATES SET TO SYNC WITH A PARTICULAR SCREEN RESOLUTION
import pyautogui
from time import sleep
import PIL.ImageGrab
import os
# make sure you reset the postion coordinates by using the postion checker tool (positionch.py file), run the file and note down the screen coordinates and update the below variables with it
## imp!!! THIS PROGRAM IS OPTIMIZED FOR SCREEN RESOLUTIONS OF 1920x1080 px.. AND SEVERAL PROPERTIES HAVE BEEN SET IN SUCH A WAY THAT IT MATCHES TO THE PROPERTY OF MY NFT COLLECTION

# Function to check for Background Color of the NFT
def bgchecker(k1):
    s = ''
    if k1 == (225, 143, 100):
        s += 'Cookie Brown'
    elif k1 == (136, 246, 143):
        s += 'Lime Green'
    elif k1 == (215, 90, 87):
        s += 'Mojito Red'
    elif k1 == (177, 12, 58):
        s += 'Wine Red'
    elif k1 == (242, 143, 136):
        s += 'Smoothie Pink'
    elif k1 == (0, 167, 15):
        s += 'Forest Green'
    else:
        s += "None"
    return s

# Function to check for Body Color of the NFT
def bodychecker(b1):
    s1 = ''
    if b1 == (46, 220, 80):
        s1 += 'Genie Green'
    elif b1 == (123, 102, 163):
        s1 += 'Berry Purple'
    elif b1 == (220, 138, 46):
        s1 += 'Caramel Brown'
    elif b1 == (21, 172, 245):
        s1 += 'Cloudy Blue'
    elif b1 == (163, 102, 128):
        s1 += 'Light Purple'
    elif b1 == (102, 163, 160):
        s1 += 'Cute Cyan'
    elif b1 == (245, 31, 21):
        s1 += 'Strawberry Red'
    elif b1 == (221, 221, 221):
        s1 += 'Pixel White'
    elif b1 == (245, 21, 194):
        s1 += 'Pixel Pink'
    else: 
        s1 += 'None'
    return s1

# Function to check for Hat Color of the NFT
def hatchecker(h1):
    s2 = ''
    if h1 == (85, 94, 142):
        s2 += 'Training Cap (Blue)'
    elif h1 == (65, 0, 128):
        s2 += 'Spooky Hat (Purple)'
    elif h1 == (88, 40, 40):
        s2 += 'Spooky Hat (Brown)'
    elif h1 == (88, 82, 40):
        s2 += 'Spooky Hat (LBrown)'
    elif h1 == (161, 67, 67):
        s2 += 'Training Cap (Brown)'
    elif h1 == (154, 67, 161):
        s2 += 'Training Cap (Purple)'
    elif h1 == (109, 161, 67):
        s2 += 'Training Cap (Green)'
    elif h1 == (31, 97, 61):
        s2 += 'Spooky Hat (Green)'
    elif h1 == (52, 48, 80):
        s2 += 'Spooky Hat (Grey Purple)'
    elif h1 == (117,85,31):
        s2 += 'Training Cap (Solid Brown)'
    else:
        s2 += 'None'
    return s2

# Function to check for Bow-Tie Color of the NFT
def bowtiechecker(t1):
    s3 = ''
    if t1 == (56, 177, 74):
        s3 += 'Green'
    elif t1 == (56, 92, 177):
        s3 += 'Blue'
    elif t1 == (158, 38, 38):
        s3 +='Red'
    elif t1 == (164, 55, 178):
        s3 += 'Purple'
    elif t1 == (214, 22, 90):
        s3 += 'Pink'
    else:
        s3 += 'None'
    return s3 

# Function to check for Glass Color of the NFT
def glasseschecker(g1):
    s4 = ''
    if g1 == (255, 255, 255):
        s4 += 'Thug Glasses (White)'
    elif g1 == (250, 250, 250):
        s4 += 'Wayfarer Classic'
    elif g1 == (253, 227, 247) or g1==(250, 241, 230) or g1==(117, 85, 31) or g1==(161, 67, 67) or g1==(236, 244, 243):
        s4 += 'Wayfarer Fancy'
    elif g1 == (0, 0, 0):
        s4 += 'Thug Glasses (Black)'
    elif g1 == (0, 176, 93):
        s4 += 'Funky Green'
    elif g1 == (196, 29, 66):
        s4 += 'Funky Pink'
    elif g1 == (0, 155, 176):
        s4 += 'Funky Blue'
    elif g1 == (171, 179, 46):
        s4 += 'Funky Yellow'
    else:
        s4 += 'Wayfarer'
    return s4

create_coorX = 1672
create_coorY = 129

uploadX = 585
uploadY = 683

bgX = 842
bgY = 560

bodyX = 758
bodyY = 553

hatX = 662  
hatY = 477

btX = 704
btY = 631

glX = 686
glY = 558

TextbX = 278
TextbY = 521

nft_num = 18
files = os.listdir(
    "C:\\Users\\USER\\Desktop\\PersonalFold\\nftstuff\\pixelPUP\\FinalNFTS")
index = 0
n = 483

##MAIN GUI PROGRAM
while nft_num != 0:
    sleep(5)
    pyautogui.click(create_coorX, create_coorY)
    sleep(5)
    pyautogui.click(uploadX, uploadY)
    sleep(3)
    pyautogui.click(TextbX, TextbY)
    pyautogui.write(files[index])
    pyautogui.press('enter')
    sleep(0.5)
    pyautogui.moveTo(988,553)
    pyautogui.click(988,553)
    sleep(2)
    index += 1
    sleep(4)
    k = PIL.ImageGrab.grab().load()[bgX,bgY]  # old coordinates (842, 560)
    # print('bg:',k)
    bg = bgchecker(k)  # checks for the bg color for updating the NFT Property
    b =  PIL.ImageGrab.grab().load()[bodyX,bodyY]
    # print('body:',b)
    body = bodychecker(b)
    h = PIL.ImageGrab.grab().load()[hatX,hatY] #checks for the type of hat and color
    hat = hatchecker(h)
    t = PIL.ImageGrab.grab().load()[btX,btY] #checks for the color of bow tie
    bt = bowtiechecker(t)  
    g = PIL.ImageGrab.grab().load()[glX,glY] #checks for the color of bow tie
    gl = glasseschecker(g)  
    sleep(0.5)
    pyautogui.press('tab', presses=3)
    name = 'MicroPuppiesNFT'+''+'#'+str(n)
    pyautogui.write(name)
    n += 1
    sleep(1)
    pyautogui.press('tab', presses=3)
    pyautogui.doubleClick(517, 712)
    pyautogui.write('MicroPuppiesNFT - Official Collection Item')
    sleep(1)
    pyautogui.press('tab', presses=4)
    pyautogui.press('Enter')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.write('Background')
    pyautogui.press('tab')
    pyautogui.write(bg)
    sleep(2)
    pyautogui.press('tab', presses=1)
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.5)
    pyautogui.press('tab', presses=7)
    pyautogui.write('Body')
    pyautogui.press('tab')
    pyautogui.write(body)
    sleep(0.5)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('tab',presses=10)
    pyautogui.write('Hat')
    pyautogui.press('tab')
    pyautogui.write(hat)
    sleep(0.5)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('tab',presses=13)
    pyautogui.write('BowTie')
    pyautogui.press('tab')
    pyautogui.write(bt)
    sleep(0.5)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('tab',presses=16)
    pyautogui.write('Glasses')
    pyautogui.press('tab')
    pyautogui.write(gl)
    sleep(3)
    pyautogui.press('tab',presses=2)
    pyautogui.press('enter')
    pyautogui.press('tab',presses=8)
    pyautogui.press('enter')
    pyautogui.press('tab')
    sleep(1)
    pyautogui.click(454,17)
    sleep(2)
    pyautogui.doubleClick(499,130)
    sleep(0.3)
    name1 = 'MicroPuppiesNFTCARD#' + str((n-1)) + ".png"
    pyautogui.write(name1)
    pyautogui.press('enter')
    sleep(9)
    pyautogui.click(1702,249)
    sleep(1)
    pyautogui.click(867,128)
    pyautogui.doubleClick(867,128)
    pyautogui.press('backspace')
    pyautogui.click(147,18)
    sleep(2)
    pyautogui.hotkey('ctrl','v')
    sleep(2)
    pyautogui.press('tab',presses=5)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.press('enter')
    sleep(20)
    pyautogui.press('tab',presses=6)
    pyautogui.press('enter')
    pyautogui.press('tab',presses=11)
    pyautogui.press('enter')
    sleep(12)
    pyautogui.write('0.01')
    sleep(2)
    pyautogui.press('tab',presses=10)
    sleep(1)
    pyautogui.write('07')
    sleep(0.5)
    pyautogui.click(1733,627)
    sleep(0.5)
    pyautogui.click(298,460)
    sleep(6)
    pyautogui.press('tab',presses=3)
    pyautogui.press('enter')
    sleep(8)
    pyautogui.press('tab',presses=2)
    pyautogui.press('enter')
    sleep(13)
    pyautogui.press('tab',presses=7)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.click(108, 67)
    sleep(10)

    ##PRINTS THE NFT MINT STATUS
    print("-----NFT UPLOADED TO OPENSEA!!------\nFile Info ::\nNFT File Original Name :",files[index-1],"\nMarket Name : ", 'MicroPuppiesNFT'+''+'#'+str(n-1), "\nProperties::","\nBackground Properties : ",bg,',',k,'\nBody Properties: ',body,',',b,"\nHat Properties : ",hat,',',h,"\nBowTie Properties : ",bt,',',t,"\nGlasses Properties : ",gl,',',g)
    nft_num -= 1                    





                                                                    


__author__ = 'Jake'

import Ebay_Functions
import Window_Functions
import time
import pyautogui
import pyperclip



################3 Configuration###########################
img_path = "C:\\Users\\Jake\\PycharmProjects\\webScrappingDK\\ebay pictures\\"
print(img_path)
url_list = []
newly_listed = False
ending_soonest = True
bid_num = 0 # number of bids on item - will bid .01 @ 0 bids and .06 @ 1 bid
search_list = ['video+games','codes','controller','battery','nes','snes','n64','storage','Playstation','holder','wire','figure','blocks','doll','character','toy','kit',
               'board','Hasboro','lego','mattel','crayola','fisher+price','ban+dai','sega',
               'vtech','leapfrog', 'duncan','tuffy', 'milton+bradley','playskool','jada+toys','spin+master','nintendo','flash','drives','Connector','lot','led',
               'dog+toy','lithium+battery','wireless', 'remote','bluetooth','Sony','konami','retro','Hobby','sd+card','xbox','cartridge','OEM']
pages = 10 # number of page downs per url
min = '.01'
max = '.01'
###############3end Configuration##############################
ending = 0

#tsting ===
time.sleep(3)
pos = pyautogui.position()
print(pyautogui.pixel(pos[0], pos[1]))
time.sleep(3)
time.sleep(3)
pyautogui.moveTo(908,401)
x,y = pyautogui.position()
print(pyautogui.pixel(x,y))
time.sleep(3)
#====end

Ebay_Functions.is_black_listed_item()
if(newly_listed == True):
    ending = 10
elif(ending_soonest == True):
    ending = 1
else:
    ending = 1

while(len(search_list) > 5):
    url, search_list = Ebay_Functions.create_Random_URL(search_list,min,max,ending)
    url_list.append(url)
    print(url)


ui = pyautogui
for url in url_list:
    print("printing url - items")
    things_on_ebay = Ebay_Functions.Items_On_Page(url)
    for item in things_on_ebay:
        print("--new item--")
        print(item['Title'])
        print(item['Price'])
        print(item['Position'])
        print(item['From'])
        print(item['Bids'])
    print("end of one URL")
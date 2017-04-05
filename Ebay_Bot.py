__author__ = 'Jake'
import Ebay_Functions
import Window_Functions
import time
import pyautogui
import pyperclip



################3 Configuration###########################
count = 5 #number of bids per search
img_path = "C:\\Users\\Jake\\PycharmProjects\\webScrappingDK\\ebay pictures\\"
print(img_path)
url_list = []
newly_listed = False
ending_soonest = True
bid_num = 0 # number of bids on item - will bid .01 @ 0 bids and .06 @ 1 bid
search_list = ['video+games','codes','controller','battery','nes','snes','n64','storage','Playstation','holder','wire','figure','blocks','doll','character','toy','kit',
               'board','Hasboro','lego','mattel','crayola','fisher+price','ban+dai','sega',
               'vtech','leapfrog', 'duncan','tuffy', 'milton+bradley','playskool','jada+toys','spin+master','nintendo','flash','drives','Connector','lot','led',
               'dog+toy','lithium+battery','wireless', 'remote','bluetooth','Sony','konami','retro','Hobby','sd+card','xbox','cartridge','OEM','Glass','plastic','plastic,cards','audio','part','travel','decal','flower','drill',
                'cat','poster','cute','elastic','tie','rubber','micro','macro','mini','mega','diy', 'fashion','set','switch','toggle','panel','lazer','sight','tactical','remote'
               ,'lure','rubber','hook','band','clip','taylormade','iron','vintage','classic','orb','pendant','carving','collectible','baseball','basketball','football','lol','twist']
pages = 8 # number of page downs per url
min = '.01'
max = '.01'
###############3end Configuration##############################
ending = 0
if(newly_listed == True):
    ending = 10
elif(ending_soonest == True):
    ending = 1
else:
    ending = 1

while(len(search_list) > 9):
    url, search_list = Ebay_Functions.create_Random_URL(search_list,min,max,ending)
    url_list.append(url)
    print(url)

ui = pyautogui
time.sleep(5)
status = '' # if something happened along way status = failed
#Window_Functions.TypeString("he../]][\llo")
#Window_Functions.leftClick()

RestrictionFlag = 0

for url in url_list:
    #use beautifulsoup4 to find all links on page + title + bid
    Ebay_Functions.Items_On_Page(url)
    if(RestrictionFlag == 0):
        Ebay_Functions.Enter_URL(url)
        #search page for 0bid items if none page down.
        for t in range(0,pages):
            if(RestrictionFlag == 0):
                success = Ebay_Functions.on_SearchPage(bid_num)
                if(success == 0):
                    #find the bid box to enter price
                    success = Ebay_Functions.find_bidBox(bid_num)
                    if(success == 0):
                        success = Ebay_Functions.enter_bid()
                        if(success == 0):
                            RestrictionFlag = Ebay_Functions.Did_I_Hit_Restriction()
                            if(RestrictionFlag == 3):
                                print("bid to low")
                                pyautogui.hotkey('escape')
                                time.sleep(1)
                                RestrictionFlag = 0
                            elif(RestrictionFlag == 2):
                                print("restriction 2 hit, Proceeding to browser back 1/2")
                                Ebay_Functions.back_Browser()
                                RestrictionFlag = 0
                            print("brower back hit")
                            Ebay_Functions.back_Browser()
                    else:
                        status = 'failed'
                        print('Failure at bid_button')
                else:
                    print("no 0 bids were found on this screen")
                    ui.hotkey('pagedown')
                    ui.hotkey('pagedown')
                    time.sleep(.3)
            else:
                 print('Restriction Hit')
    else:
        print('Restriction Hit....Trying to exit')
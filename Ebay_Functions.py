__author__ = 'Jake'
import random
import pyautogui
import pyperclip
import time
from bs4 import BeautifulSoup
import urllib.request
import re
import win32clipboard




ui = pyautogui
img_path = "C:\\Users\\Jake\\PycharmProjects\\webScrappingDK\\ebay pictures\\"

def create_Random_URL(list,min,max,ending):
    sop = str(ending)
    minPrice = min
    maxPrice = max
    freeShipping = '1'
    Auction = True # code is
    All_Listings = True
    Buy_it_Now = True
    item1 = list[random.randint(0,len(list)-1)]
    list.remove(item1)
    item2 = list[random.randint(0,len(list)-1)]
    list.remove(item2)
    item3 = list[random.randint(0,len(list)-1)]
    list.remove(item3)
    item4 = list[random.randint(0,len(list)-1)]
    list.remove(item4)
    item5 = list[random.randint(0,len(list)-1)]
    list.remove(item5)
    item6 = list[random.randint(0,len(list)-1)]
    list.remove(item6)
    item7 = list[random.randint(0,len(list)-1)]
    list.remove(item7)
    item8 = list[random.randint(0,len(list)-1)]
    list.remove(item8)
    item9 = list[random.randint(0,len(list)-1)]
    list.remove(item9)
    item10 = list[random.randint(0,len(list)-1)]
    list.remove(item10)
    url = 'http://www.ebay.com/sch/i.html?_udlo=' + minPrice + '&_sop=1&_udhi='+ maxPrice +'&LH_FS=1&LH_Auction=1&_from=R40&_sacat=0&_nkw=%28'+item10+'%2C' + item1+'%2C' + item2 +'%2C'+ item3 + '%2C' + item4 + '%2C' + item5 +'%2C' + item6+ '%2C' +item7 +'%2C'+ item8 +'%2C'+ item9 + '%29&LH_PrefLoc=98&_ipg=200&_sop=' + sop
    return url, list


def Enter_URL(url):
    #enters the url into the box
    pyautogui.moveTo(555,47)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.hotkey('delete')
    #uses pyperclip lib to copy to the clipboard
    pyperclip.copy(url)
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')
    pyautogui.hotkey('enter')
    time.sleep(5) # wait for site to load


#searches the ebay search Page for 0bids returns failed if x[1]-45 < 93 returns 0 if everything is fine; returns 1 if out of bounds
def on_SearchPage(bid_num):
     if(bid_num == 0):
        x = pyautogui.locateCenterOnScreen(img_path + '0bid.PNG')
     elif(bid_num == 1):
        x = pyautogui.locateCenterOnScreen(img_path + '1bid.PNG')
     elif(bid_num == 2):
         x = pyautogui.locateCenterOnScreen(img_path + '2bid.PNG')
     if(str(x) != 'None'):
        bounds = x[1] - 45
        if(int(bounds) < 93):
            print('Error: out of bounds')
            return 1
        else:
            pyautogui.moveTo(x[0]+60,x[1]) #add 300 pixles to place mouse towards middle of link to grab color as it moves up
            if(move_Mouse_till_color_hit(6,84,186)):
                return 1
            if(is_black_listed_item()):
                return 1
            else:
                ui.click()
            time.sleep(3) # wait for site to load
            return 0


#uses two images to find the box. - uses price of object being 1cent and the box itself
def find_bidBox(bid_num):
    price = ''
    if(bid_num==0):
        price = '.01'
    elif(bid_num == 1):
        price = '.06'
    price_box = pyautogui.locateCenterOnScreen(img_path + 'price_box.PNG')
    centProof = ui.locateCenterOnScreen(img_path + '1centProof.PNG')
    if(str(price_box) != 'None'):
        pyautogui.moveTo(price_box[0],price_box[1])
        time.sleep(.5)
        ui.click()
        time.sleep(1)
        ui.typewrite(price)
        return 0
    elif(str(centProof) != 'None'):
        ui.moveTo(centProof[0],centProof[1]+25)
        time.sleep(.2)
        ui.click()
        ui.typewrite('.01')
        return 0
    else:
        print('failure at price box')
        return 1

def enter_bid():
    bid_button = pyautogui.locateCenterOnScreen(img_path + 'Place Bid.PNG')
    if(str(bid_button)!= 'None'):
        pyautogui.moveTo(bid_button[0],bid_button[1],.5)
        pyautogui.click()
        time.sleep(3)
        confirm = ui.locateCenterOnScreen(img_path + 'confirm.PNG')
        warning_bid = ui.locateCenterOnScreen(img_path + 'warning_confirm.PNG')
        if(str(confirm) != 'None'):
            ui.moveTo(confirm[0],confirm[1],.5)
            ui.click()
            print("bid success! ")
            time.sleep(3)
            return 0
        elif(str(warning_bid) != 'None'):
            print("warning message found")
            ui.moveTo((warning_bid[0],warning_bid[1]))
            ui.click()
            print("bid success! ")
            time.sleep(3)
            return 0
        else:
            print('confirm button not found')
            return 1
    else:
        print('bid_button not found')
        return 1

def back_Browser():
    back = ui.locateCenterOnScreen(img_path + 'Back.PNG')
    if(str(back) != 'None'):
        ui.moveTo(back[0],back[1])
        ui.click()
        time.sleep(3)
        ui.hotkey('pagedown')
        ui.hotkey('pagedown')
        return 0
    else:
        return 1

def Did_I_Hit_Restriction():

    bid_error = ui.locateCenterOnScreen(img_path + 'bid_to_low_error.PNG')
    seller_wont_sell = ui.locateCenterOnScreen(img_path + 'item_restriction.PNG')
    temp_buyer_restriction = ui.locateCenterOnScreen(img_path + 'seller_restriction.PNG')
    if(str(seller_wont_sell) !='None'):
        print('restriction...multiple items form seller hit')
        return 2
    elif(str(temp_buyer_restriction) != 'None'):
        print('restriction Screen Hit')
        return 1
    elif(str(bid_error) !='None'):
        return 3
    else:
        return 0

def strip_tag(string):
    temp = string
    temp = temp.strip('[<span class="bold">')
    temp = temp.strip('</span>]')
    return temp

def Items_On_Page(url):
    #add to a dictionary then add to a list and return
    list_of_items = []
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    Items = soup.find_all(class_='sresult lvresult clearfix li')
    for i in range(0,len(Items)):
        listed_good = {}
        listed_good['Position'] = i
        listed_good['Title'] = ''
        listed_good['Price'] = ''
        listed_good['Bids'] = ''
        listed_good['Shipping'] = ''
        listed_good['From'] = ''
        list_x =(Items[i].get_text().splitlines())
        list_x = filter(None, list_x)
        count = 0
        for item in list_x:
            item = item.strip('\t')
            if(count == 4):
                #print("added from")
                listed_good['From'] = item
            elif(count == 3):
                #print("added shipping")
                listed_good['Shipping'] = item
            elif(count == 2):
                #print("added bids")
                listed_good['Bids'] = item
            elif(count == 1):
                #print("added price")
                listed_good['Price'] = item
            elif(count==0):
                #print("added title")
                listed_good['Title'] = item
            #print(count)
            count = count + 1
        list_of_items.append(listed_good)
    return list_of_items

def is_black_listed_item():
    #right mouse click down 5 enter
    black_list_ = ['picture','recipe','email','penny']
    pyautogui.click(button='right')
    time.sleep(.3)
    pyautogui.hotkey('down')
    time.sleep(.1)
    pyautogui.hotkey('down')
    time.sleep(.1)
    pyautogui.hotkey('down')
    time.sleep(.1)
    pyautogui.hotkey('down')
    time.sleep(.1)
    pyautogui.hotkey('down')
    time.sleep(.3)
    pyautogui.press('enter')
    print('copied to clip board')
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    print(data)
    if any(word in data.lower() for word in black_list_):
        print("blacklisted item: moving on...")
        return True
    else:
        print('item passed screening')
        return False

def move_Mouse_till_color_hit(red,green,blue):
    for z in range(0,100):
        x,y = pyautogui.position()
        if(pyautogui.pixelMatchesColor(x, y, (red, green, blue))):
            print('Link found')
            return 0
        pyautogui.moveRel(0,-1)
        x,y = pyautogui.position()
        print(pyautogui.pixel(x, y))
        print ("moving mouse " + str(z))
    return 1

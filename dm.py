from __future__ import absolute_import, unicode_literals

#mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
import os
#scraper
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from urllib.request import urlopen
from datetime import datetime, timedelta
import http.client
from pathlib import Path
import pandas as pd
import numpy as np
from celery import Celery
from celery import app, shared_task
from celery.schedules import crontab # scheduler
import json
import time 
import lxml
import pytz
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800,1080))  
display.start()



tmstmp = time.strftime("%d-%m-%Y %H%M%S")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument('--headless')
chrome_options.headless = True
driver = webdriver.Chrome(options=chrome_options)
driver.create_options()


dm_list_allMEGA = []




#CHECKING PAISIOS
#30_60


driver.get("https://www.dailymotion.com/search/%CF%80%CE%B1%CE%B9%CF%83%CE%B9%CE%BF%CF%82/videos?duration=mins_30_60&sortBy=most_recent")

 


#FIRSTONE#FIRSTONE#FIRSTONE#FIRSTONE#FIRSTONE 

try:
    button = driver.find_element_by_xpath('//*[@id="portal-root"]/div/div/div[2]/div/div[4]/button[2]').click() 
except:
    pass 
    print ("nocookiesbutton")

#FIRSTONE#FIRSTONE#FIRSTONE#FIRSTONE#FIRSTONE



try:    
    
    time.sleep(10)

    titlesearch_caps = driver.find_elements_by_partial_link_text('Άγιος Παΐσιος')
    titlesearch_normal = driver.find_elements_by_partial_link_text('PAISIOS')
    titlesearch_small = driver.find_elements_by_partial_link_text('ΠΑΙΣΙΟΣ')
    titlesearch_smaller = driver.find_elements_by_partial_link_text('παισιος')
    titlesearch_smaller_eng = driver.find_elements_by_partial_link_text('paisios')


    titlesearch =  titlesearch_smaller_eng+titlesearch_caps+titlesearch_normal+titlesearch_small+titlesearch_smaller

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    
      
except:

    pass



""" #CHECKING MAESTRO +60

driver.get("https://www.dailymotion.com/search/maestro/videos?duration=more_than_1h&sortBy=most_recent") 
 



try:    
    
    time.sleep(4)

    titlesearch_capsS = driver.find_elements_by_partial_link_text('MAESTRO Σ')
    titlesearch_normalS = driver.find_elements_by_partial_link_text('Maestro Σ')
    titlesearch_smallS = driver.find_elements_by_partial_link_text('MAESTRO Σ')
    titlesearch_capsE = driver.find_elements_by_partial_link_text('MAESTRO ΕΠ')
    titlesearch_normalE = driver.find_elements_by_partial_link_text('Maestro Επ')
    titlesearch_smallE = driver.find_elements_by_partial_link_text('Maestro Επ')
    titlesearch_normalSnot = driver.find_elements_by_partial_link_text('MAESTRO Σ')
    titlesearch_smallSnot = driver.find_elements_by_partial_link_text('MAESTRO Σ')
    titlesearch_normalEnot = driver.find_elements_by_partial_link_text('MAESTRO Επ')
    titlesearch_smallEnot = driver.find_elements_by_partial_link_text('MAESTRO Επ')
    titlesearch_smallEnotokk= driver.find_elements_by_partial_link_text('Maestro Επ1')      
    titlesearch_capsSq = driver.find_elements_by_partial_link_text('ΜΑΕSTRO Σ')
    titlesearch_normalSq = driver.find_elements_by_partial_link_text('maestro Σ')
    titlesearch_smallSq = driver.find_elements_by_partial_link_text('maestros Σ')
    titlesearch_capsEq = driver.find_elements_by_partial_link_text('papakaliatis ΕΠ')
    titlesearch_normalEq = driver.find_elements_by_partial_link_text('Papakaliatis Επ')
    titlesearch_smallEq = driver.find_elements_by_partial_link_text('ΠΑΠΑΚΑΛΙΑΤΗΣ Επ')
    titlesearch_normalSnotq = driver.find_elements_by_partial_link_text('maeστro Σ')
    titlesearch_smallSnotq = driver.find_elements_by_partial_link_text('maestro Σ')
    titlesearch_normalEnotq = driver.find_elements_by_partial_link_text('Maestro - Επ')
    titlesearch_smallEnotq = driver.find_elements_by_partial_link_text('παpakaliatis Επ')


    titlesearch_capsSp = driver.find_elements_by_partial_link_text('MAESTRO - Σ')
    titlesearch_normalSp = driver.find_elements_by_partial_link_text('Maestro - Σ')
    titlesearch_smallSp = driver.find_elements_by_partial_link_text('Maestro - Σ')
    titlesearch_capsEp = driver.find_elements_by_partial_link_text('MAESTRO - ΕΠ')
    titlesearch_normalEp = driver.find_elements_by_partial_link_text('Maestro - Επ')
    titlesearch_smallEp = driver.find_elements_by_partial_link_text('Maestro - Επ')
    titlesearch_normalSnotp = driver.find_elements_by_partial_link_text('Maestro - Σ')
    titlesearch_smallSnotp = driver.find_elements_by_partial_link_text('παπακαλιατης - Σ')
    titlesearch_normalEnotp = driver.find_elements_by_partial_link_text('Maestro - Επ')
    titlesearch_smallEnotp = driver.find_elements_by_partial_link_text('παπακαλιάτης - Επ')
    

    titlesearch_capsSpky = driver.find_elements_by_partial_link_text('MAESTRO - Kύκλος')
    titlesearch_normalSpky = driver.find_elements_by_partial_link_text('Maestro - Kύκλος')
    titlesearch_smallSpky = driver.find_elements_by_partial_link_text('Maestro - Kύκλος')
    titlesearch_capsEpky = driver.find_elements_by_partial_link_text('MAESTRO - ΚΥΚΛΟΣ')
    titlesearch_normalEpky = driver.find_elements_by_partial_link_text('Maestro - Κυκλος')
    titlesearch_smallEpky = driver.find_elements_by_partial_link_text('Maestro - κυκλος')
    titlesearch_smallSnotpky = driver.find_elements_by_partial_link_text('Maestro - κύκλος')
    titlesearch_normalEnotpky = driver.find_elements_by_partial_link_text('Maestro - ΚΥΚΛΟΣ')
    titlesearch_smallEnotpky = driver.find_elements_by_partial_link_text('MAESTRO - ΚΥΚΛΟΣ')

    titlesearch_capsSpkys = driver.find_elements_by_partial_link_text('MAESTRO S')
    titlesearch_normalSpkys = driver.find_elements_by_partial_link_text('Maestro S')
    titlesearch_smallSpkys = driver.find_elements_by_partial_link_text('Maestro S')
    titlesearch_capsEpkys = driver.find_elements_by_partial_link_text('MAESTRO s')
    titlesearch_normalEpkys = driver.find_elements_by_partial_link_text('Maestro s')
    titlesearch_smallEpkys = driver.find_elements_by_partial_link_text('Maestro s')


    titlesearch_capsSpkyspr = driver.find_elements_by_partial_link_text('MAESTRO ΠΡΕΜΙΕΡΑ')
    titlesearch_normalSpkyspr = driver.find_elements_by_partial_link_text('Maestro Πρεμιέρα')
    titlesearch_smallSpkyspr = driver.find_elements_by_partial_link_text('Maestro πρεμιέρα')
    titlesearch_capsEpkyspr = driver.find_elements_by_partial_link_text('maestro')
    titlesearch_normalEpkyspr = driver.find_elements_by_partial_link_text('MAESTRO')
    titlesearch_smallEpkyspr = driver.find_elements_by_partial_link_text('Maestro')




    titlesearch = titlesearch_smallEnotokk+titlesearch_capsSpkyspr+titlesearch_normalSpkyspr+titlesearch_smallSpkyspr+titlesearch_capsEpkyspr+titlesearch_normalEpkyspr+titlesearch_smallEpkyspr+titlesearch_capsSq+titlesearch_normalSq+titlesearch_smallSq+titlesearch_capsEq+titlesearch_normalEq+titlesearch_smallEq +titlesearch_normalSnotq+titlesearch_smallSnotq+ titlesearch_normalEnotq+titlesearch_smallEnotq+titlesearch_smallEpkys+titlesearch_normalEpkys+titlesearch_capsEpkys+titlesearch_smallSpkys+titlesearch_normalSpkys+titlesearch_capsSpkys+titlesearch_smallEnotp+titlesearch_normalEnotp+titlesearch_smallSnotp+titlesearch_normalSnotp+titlesearch_capsSp+titlesearch_normalSp+titlesearch_smallSp+titlesearch_capsEp+titlesearch_normalEp+titlesearch_smallEp+titlesearch_smallEnot+titlesearch_normalEnot+titlesearch_smallSnot+titlesearch_normalSnot+titlesearch_capsS+titlesearch_normalS+titlesearch_smallS+titlesearch_capsE+titlesearch_normalE+titlesearch_smallE+titlesearch_capsSpky+titlesearch_normalSpky+titlesearch_smallSpky+titlesearch_capsEpky+titlesearch_normalEpky+titlesearch_smallEpky+titlesearch_smallSnotpky+titlesearch_normalEnotpky+titlesearch_smallEnotpky

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    
    

    
except:

    pass




#CHECKING MAESTRO Greek +60

driver.get("https://www.dailymotion.com/search/%CE%BC%CE%B1%CE%B5%CF%83%CF%84%CF%81%CE%BF/videos?duration=more_than_1h&sortBy=most_recent") 
 



try:    
    
    time.sleep(4)

    titlesearch_capsSgr1= driver.find_elements_by_partial_link_text('ΜΑΕΣΤΡΟ') 
    titlesearch_capsSgr2= driver.find_elements_by_partial_link_text('Μαέστρο') 
    titlesearch_capsSgr3= driver.find_elements_by_partial_link_text('Μαεστρο') 
    titlesearch_capsSgr4= driver.find_elements_by_partial_link_text('Mαεστρο') 
    titlesearch_capsSgr5= driver.find_elements_by_partial_link_text('μαεστρο') 

   
    

    titlesearch_capsS = driver.find_elements_by_partial_link_text('MAESTRO Σ')
    titlesearch_normalS = driver.find_elements_by_partial_link_text('Maestro Σ')
    titlesearch_smallS = driver.find_elements_by_partial_link_text('MAESTRO Σ')
    titlesearch_capsE = driver.find_elements_by_partial_link_text('MAESTRO ΕΠ')
    titlesearch_normalE = driver.find_elements_by_partial_link_text('Maestro Επ')
    titlesearch_smallE = driver.find_elements_by_partial_link_text('Maestro Επ')
    titlesearch_normalSnot = driver.find_elements_by_partial_link_text('MAESTRO Σ')
    titlesearch_smallSnot = driver.find_elements_by_partial_link_text('MAESTRO Σ')
    titlesearch_normalEnot = driver.find_elements_by_partial_link_text('MAESTRO Επ')
    titlesearch_smallEnot = driver.find_elements_by_partial_link_text('MAESTRO Επ')
    titlesearch_smallEnotokk= driver.find_elements_by_partial_link_text('Maestro Επ1')      

    titlesearch_capsSq = driver.find_elements_by_partial_link_text('ΜΑΕSTRO Σ')
    titlesearch_normalSq = driver.find_elements_by_partial_link_text('maestro Σ')
    titlesearch_smallSq = driver.find_elements_by_partial_link_text('maestros Σ')
    titlesearch_capsEq = driver.find_elements_by_partial_link_text('papakaliatis ΕΠ')
    titlesearch_normalEq = driver.find_elements_by_partial_link_text('Papakaliatis Επ')
    titlesearch_smallEq = driver.find_elements_by_partial_link_text('ΠΑΠΑΚΑΛΙΑΤΗΣ Επ')
    titlesearch_normalSnotq = driver.find_elements_by_partial_link_text('maeστro Σ')
    titlesearch_smallSnotq = driver.find_elements_by_partial_link_text('maestro Σ')
    titlesearch_normalEnotq = driver.find_elements_by_partial_link_text('Maestro - Επ')
    titlesearch_smallEnotq = driver.find_elements_by_partial_link_text('παpakaliatis Επ')


    titlesearch_capsSp = driver.find_elements_by_partial_link_text('MAESTRO - Σ')
    titlesearch_normalSp = driver.find_elements_by_partial_link_text('Maestro - Σ')
    titlesearch_smallSp = driver.find_elements_by_partial_link_text('Maestro - Σ')
    titlesearch_capsEp = driver.find_elements_by_partial_link_text('MAESTRO - ΕΠ')
    titlesearch_normalEp = driver.find_elements_by_partial_link_text('Maestro - Επ')
    titlesearch_smallEp = driver.find_elements_by_partial_link_text('Maestro - Επ')
    titlesearch_normalSnotp = driver.find_elements_by_partial_link_text('Maestro - Σ')
    titlesearch_smallSnotp = driver.find_elements_by_partial_link_text('παπακαλιατης - Σ')
    titlesearch_normalEnotp = driver.find_elements_by_partial_link_text('Maestro - Επ')
    titlesearch_smallEnotp = driver.find_elements_by_partial_link_text('παπακαλιάτης - Επ')
    

    titlesearch_capsSpky = driver.find_elements_by_partial_link_text('MAESTRO - Kύκλος')
    titlesearch_normalSpky = driver.find_elements_by_partial_link_text('Maestro - Kύκλος')
    titlesearch_smallSpky = driver.find_elements_by_partial_link_text('Maestro - Kύκλος')
    titlesearch_capsEpky = driver.find_elements_by_partial_link_text('MAESTRO - ΚΥΚΛΟΣ')
    titlesearch_normalEpky = driver.find_elements_by_partial_link_text('Maestro - Κυκλος')
    titlesearch_smallEpky = driver.find_elements_by_partial_link_text('Maestro - κυκλος')
    titlesearch_smallSnotpky = driver.find_elements_by_partial_link_text('Maestro - κύκλος')
    titlesearch_normalEnotpky = driver.find_elements_by_partial_link_text('Maestro - ΚΥΚΛΟΣ')
    titlesearch_smallEnotpky = driver.find_elements_by_partial_link_text('MAESTRO - ΚΥΚΛΟΣ')

    titlesearch_capsSpkys = driver.find_elements_by_partial_link_text('MAESTRO S')
    titlesearch_normalSpkys = driver.find_elements_by_partial_link_text('Maestro S')
    titlesearch_smallSpkys = driver.find_elements_by_partial_link_text('Maestro S')
    titlesearch_capsEpkys = driver.find_elements_by_partial_link_text('MAESTRO s')
    titlesearch_normalEpkys = driver.find_elements_by_partial_link_text('Maestro s')
    titlesearch_smallEpkys = driver.find_elements_by_partial_link_text('Maestro s')


    titlesearch_capsSpkyspr = driver.find_elements_by_partial_link_text('MAESTRO ΠΡΕΜΙΕΡΑ')
    titlesearch_normalSpkyspr = driver.find_elements_by_partial_link_text('Maestro Πρεμιέρα')
    titlesearch_smallSpkyspr = driver.find_elements_by_partial_link_text('Maestro πρεμιέρα')
    titlesearch_capsEpkyspr = driver.find_elements_by_partial_link_text('MAESTRO ΠΡΩΤΟ')
    titlesearch_normalEpkyspr = driver.find_elements_by_partial_link_text('MAESTRO')
    titlesearch_smallEpkyspr = driver.find_elements_by_partial_link_text('Maestro')
    titlesearch_smallEnotqdash1 = driver.find_elements_by_partial_link_text('Maestro -')
    titlesearch_smallEnotqdash2 = driver.find_elements_by_partial_link_text('MAESTRO -')
    titlesearch_smallEnotqdash3 = driver.find_elements_by_partial_link_text('MAESTRO -')
    titlesearch_smallEnotqdash4 = driver.find_elements_by_partial_link_text('Maestro -')



    titlesearch = titlesearch_capsSgr1+titlesearch_capsSgr2+titlesearch_capsSgr3+titlesearch_capsSgr4+titlesearch_capsSgr5+titlesearch_smallEnotokk+titlesearch_smallEnotqdash1+titlesearch_smallEnotqdash2+titlesearch_smallEnotqdash3+titlesearch_smallEnotqdash4+titlesearch_capsSpkyspr+titlesearch_normalSpkyspr+titlesearch_smallSpkyspr+titlesearch_capsEpkyspr+titlesearch_normalEpkyspr+titlesearch_smallEpkyspr+titlesearch_capsSq+titlesearch_normalSq+titlesearch_smallSq+titlesearch_capsEq+titlesearch_normalEq+titlesearch_smallEq +titlesearch_normalSnotq+titlesearch_smallSnotq+ titlesearch_normalEnotq+titlesearch_smallEnotq+titlesearch_smallEpkys+titlesearch_normalEpkys+titlesearch_capsEpkys+titlesearch_smallSpkys+titlesearch_normalSpkys+titlesearch_capsSpkys+titlesearch_smallEnotp+titlesearch_normalEnotp+titlesearch_smallSnotp+titlesearch_normalSnotp+titlesearch_capsSp+titlesearch_normalSp+titlesearch_smallSp+titlesearch_capsEp+titlesearch_normalEp+titlesearch_smallEp+titlesearch_smallEnot+titlesearch_normalEnot+titlesearch_smallSnot+titlesearch_normalSnot+titlesearch_capsS+titlesearch_normalS+titlesearch_smallS+titlesearch_capsE+titlesearch_normalE+titlesearch_smallE+titlesearch_capsSpky+titlesearch_normalSpky+titlesearch_smallSpky+titlesearch_capsEpky+titlesearch_normalEpky+titlesearch_smallEpky+titlesearch_smallSnotpky+titlesearch_normalEnotpky+titlesearch_smallEnotpky

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    
    

    
except:

    pass



#CHECKING MAESTRO Greek 30-60

driver.get("https://www.dailymotion.com/search/%CE%BC%CE%B1%CE%B5%CF%83%CF%84%CF%81%CE%BF/videos?duration=mins_30_60&sortBy=most_recent") 
 



try:    
    
    time.sleep(4)

    titlesearch_capsSgr1= driver.find_elements_by_partial_link_text('ΜΑΕΣΤΡΟ') 
    titlesearch_capsSgr2= driver.find_elements_by_partial_link_text('Μαέστρο') 
    titlesearch_capsSgr3= driver.find_elements_by_partial_link_text('Μαεστρο') 
    titlesearch_capsSgr4= driver.find_elements_by_partial_link_text('Mαεστρο') 
    titlesearch_capsSgr5= driver.find_elements_by_partial_link_text('μαεστρο') 

   
    
    
    titlesearch_capsS = driver.find_elements_by_partial_link_text('MAESTRO Σ')
    titlesearch_normalS = driver.find_elements_by_partial_link_text('Maestro Σ')
    titlesearch_smallS = driver.find_elements_by_partial_link_text('MAESTRO Σ')
    titlesearch_capsE = driver.find_elements_by_partial_link_text('MAESTRO ΕΠ')
    titlesearch_normalE = driver.find_elements_by_partial_link_text('Maestro Επ')
    titlesearch_smallE = driver.find_elements_by_partial_link_text('Maestro Επ')
    titlesearch_normalSnot = driver.find_elements_by_partial_link_text('MAESTRO Σ')
    titlesearch_smallSnot = driver.find_elements_by_partial_link_text('MAESTRO Σ')
    titlesearch_normalEnot = driver.find_elements_by_partial_link_text('MAESTRO Επ')
    titlesearch_smallEnot = driver.find_elements_by_partial_link_text('MAESTRO Επ')

    titlesearch_capsSq = driver.find_elements_by_partial_link_text('ΜΑΕSTRO Σ')
    titlesearch_normalSq = driver.find_elements_by_partial_link_text('maestro Σ')
    titlesearch_smallSq = driver.find_elements_by_partial_link_text('maestros Σ')
    titlesearch_capsEq = driver.find_elements_by_partial_link_text('papakaliatis ΕΠ')
    titlesearch_normalEq = driver.find_elements_by_partial_link_text('Papakaliatis Επ')
    titlesearch_smallEq = driver.find_elements_by_partial_link_text('ΠΑΠΑΚΑΛΙΑΤΗΣ Επ')
    titlesearch_normalSnotq = driver.find_elements_by_partial_link_text('maeστro Σ')
    titlesearch_smallSnotq = driver.find_elements_by_partial_link_text('maestro Σ')
    titlesearch_normalEnotq = driver.find_elements_by_partial_link_text('Maestro - Επ')
    titlesearch_smallEnotq = driver.find_elements_by_partial_link_text('παpakaliatis Επ')

    titlesearch_smallEnotokk= driver.find_elements_by_partial_link_text('Maestro Επ1')      

    titlesearch_capsSp = driver.find_elements_by_partial_link_text('MAESTRO - Σ')
    titlesearch_normalSp = driver.find_elements_by_partial_link_text('Maestro - Σ')
    titlesearch_smallSp = driver.find_elements_by_partial_link_text('Maestro - Σ')
    titlesearch_capsEp = driver.find_elements_by_partial_link_text('MAESTRO - ΕΠ')
    titlesearch_normalEp = driver.find_elements_by_partial_link_text('Maestro - Επ')
    titlesearch_smallEp = driver.find_elements_by_partial_link_text('Maestro - Επ')
    titlesearch_normalSnotp = driver.find_elements_by_partial_link_text('Maestro - Σ')
    titlesearch_smallSnotp = driver.find_elements_by_partial_link_text('παπακαλιατης - Σ')
    titlesearch_normalEnotp = driver.find_elements_by_partial_link_text('Maestro - Επ')
    titlesearch_smallEnotp = driver.find_elements_by_partial_link_text('παπακαλιάτης - Επ')
    

    titlesearch_capsSpky = driver.find_elements_by_partial_link_text('MAESTRO - Kύκλος')
    titlesearch_normalSpky = driver.find_elements_by_partial_link_text('Maestro - Kύκλος')
    titlesearch_smallSpky = driver.find_elements_by_partial_link_text('Maestro - Kύκλος')
    titlesearch_capsEpky = driver.find_elements_by_partial_link_text('MAESTRO - ΚΥΚΛΟΣ')
    titlesearch_normalEpky = driver.find_elements_by_partial_link_text('Maestro - Κυκλος')
    titlesearch_smallEpky = driver.find_elements_by_partial_link_text('Maestro - κυκλος')
    titlesearch_smallSnotpky = driver.find_elements_by_partial_link_text('Maestro - κύκλος')
    titlesearch_normalEnotpky = driver.find_elements_by_partial_link_text('Maestro - ΚΥΚΛΟΣ')
    titlesearch_smallEnotpky = driver.find_elements_by_partial_link_text('MAESTRO - ΚΥΚΛΟΣ')

    titlesearch_capsSpkys = driver.find_elements_by_partial_link_text('MAESTRO S')
    titlesearch_normalSpkys = driver.find_elements_by_partial_link_text('Maestro S')
    titlesearch_smallSpkys = driver.find_elements_by_partial_link_text('Maestro S')
    titlesearch_capsEpkys = driver.find_elements_by_partial_link_text('MAESTRO s')
    titlesearch_normalEpkys = driver.find_elements_by_partial_link_text('Maestro s')
    titlesearch_smallEpkys = driver.find_elements_by_partial_link_text('Maestro s')


    titlesearch_capsSpkyspr = driver.find_elements_by_partial_link_text('MAESTRO ΠΡΕΜΙΕΡΑ')
    titlesearch_normalSpkyspr = driver.find_elements_by_partial_link_text('Maestro Πρεμιέρα')
    titlesearch_smallSpkyspr = driver.find_elements_by_partial_link_text('Maestro πρεμιέρα')
    titlesearch_capsEpkyspr = driver.find_elements_by_partial_link_text('MAESTRO ΠΡΩΤΟ')
    titlesearch_normalEpkyspr = driver.find_elements_by_partial_link_text('MAESTRO')
    titlesearch_smallEpkyspr = driver.find_elements_by_partial_link_text('Maestro')
    titlesearch_smallEnotqdash1 = driver.find_elements_by_partial_link_text('Maestro -')
    titlesearch_smallEnotqdash2 = driver.find_elements_by_partial_link_text('MAESTRO -')
    titlesearch_smallEnotqdash3 = driver.find_elements_by_partial_link_text('MAESTRO -')
    titlesearch_smallEnotqdash4 = driver.find_elements_by_partial_link_text('Maestro -')



    titlesearch = titlesearch_capsSgr1+titlesearch_capsSgr2+titlesearch_capsSgr3+titlesearch_capsSgr4+titlesearch_capsSgr5+titlesearch_smallEnotokk+titlesearch_smallEnotqdash1+titlesearch_smallEnotqdash2+titlesearch_smallEnotqdash3+titlesearch_smallEnotqdash4+titlesearch_capsSpkyspr+titlesearch_normalSpkyspr+titlesearch_smallSpkyspr+titlesearch_capsEpkyspr+titlesearch_normalEpkyspr+titlesearch_smallEpkyspr+titlesearch_capsSq+titlesearch_normalSq+titlesearch_smallSq+titlesearch_capsEq+titlesearch_normalEq+titlesearch_smallEq +titlesearch_normalSnotq+titlesearch_smallSnotq+ titlesearch_normalEnotq+titlesearch_smallEnotq+titlesearch_smallEpkys+titlesearch_normalEpkys+titlesearch_capsEpkys+titlesearch_smallSpkys+titlesearch_normalSpkys+titlesearch_capsSpkys+titlesearch_smallEnotp+titlesearch_normalEnotp+titlesearch_smallSnotp+titlesearch_normalSnotp+titlesearch_capsSp+titlesearch_normalSp+titlesearch_smallSp+titlesearch_capsEp+titlesearch_normalEp+titlesearch_smallEp+titlesearch_smallEnot+titlesearch_normalEnot+titlesearch_smallSnot+titlesearch_normalSnot+titlesearch_capsS+titlesearch_normalS+titlesearch_smallS+titlesearch_capsE+titlesearch_normalE+titlesearch_smallE+titlesearch_capsSpky+titlesearch_normalSpky+titlesearch_smallSpky+titlesearch_capsEpky+titlesearch_normalEpky+titlesearch_smallEpky+titlesearch_smallSnotpky+titlesearch_normalEnotpky+titlesearch_smallEnotpky

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    
    

    
except:

    pass




#CHECKING MAESTRO 30-60

driver.get("https://www.dailymotion.com/search/maestro/videos?duration=mins_30_60&sortBy=most_recent") 
 



try:    
    
    time.sleep(4)

    titlesearch_capsS = driver.find_elements_by_partial_link_text('MAESTRO Σ')
    titlesearch_normalS = driver.find_elements_by_partial_link_text('Maestro Σ')
    titlesearch_smallS = driver.find_elements_by_partial_link_text('MAESTRO Σ')
    titlesearch_capsE = driver.find_elements_by_partial_link_text('MAESTRO ΕΠ')
    titlesearch_normalE = driver.find_elements_by_partial_link_text('Maestro Επ')
    titlesearch_smallE = driver.find_elements_by_partial_link_text('Maestro Επ')
    titlesearch_normalSnot = driver.find_elements_by_partial_link_text('MAESTRO Σ')
    titlesearch_smallSnot = driver.find_elements_by_partial_link_text('MAESTRO Σ')
    titlesearch_normalEnot = driver.find_elements_by_partial_link_text('MAESTRO Επ')
    titlesearch_smallEnot = driver.find_elements_by_partial_link_text('MAESTRO Επ')
    titlesearch_smallEnotokk= driver.find_elements_by_partial_link_text('Maestro Επ1')      

    titlesearch_capsSq = driver.find_elements_by_partial_link_text('ΜΑΕSTRO Σ')
    titlesearch_normalSq = driver.find_elements_by_partial_link_text('maestro Σ')
    titlesearch_smallSq = driver.find_elements_by_partial_link_text('maestros Σ')
    titlesearch_capsEq = driver.find_elements_by_partial_link_text('papakaliatis ΕΠ')
    titlesearch_normalEq = driver.find_elements_by_partial_link_text('Papakaliatis Επ')
    titlesearch_smallEq = driver.find_elements_by_partial_link_text('ΠΑΠΑΚΑΛΙΑΤΗΣ Επ')
    titlesearch_normalSnotq = driver.find_elements_by_partial_link_text('maeστro Σ')
    titlesearch_smallSnotq = driver.find_elements_by_partial_link_text('maestro Σ')
    titlesearch_normalEnotq = driver.find_elements_by_partial_link_text('Maestro - Επ')
    titlesearch_smallEnotq = driver.find_elements_by_partial_link_text('παpakaliatis Επ')


    titlesearch_capsSp = driver.find_elements_by_partial_link_text('MAESTRO - Σ')
    titlesearch_normalSp = driver.find_elements_by_partial_link_text('Maestro - Σ')
    titlesearch_smallSp = driver.find_elements_by_partial_link_text('Maestro - Σ')
    titlesearch_capsEp = driver.find_elements_by_partial_link_text('MAESTRO - ΕΠ')
    titlesearch_normalEp = driver.find_elements_by_partial_link_text('Maestro - Επ')
    titlesearch_smallEp = driver.find_elements_by_partial_link_text('Maestro - Επ')
    titlesearch_normalSnotp = driver.find_elements_by_partial_link_text('Maestro - Σ')
    titlesearch_smallSnotp = driver.find_elements_by_partial_link_text('παπακαλιατης - Σ')
    titlesearch_normalEnotp = driver.find_elements_by_partial_link_text('Maestro - Επ')
    titlesearch_smallEnotp = driver.find_elements_by_partial_link_text('παπακαλιάτης - Επ')
    

    titlesearch_capsSpky = driver.find_elements_by_partial_link_text('MAESTRO - Kύκλος')
    titlesearch_normalSpky = driver.find_elements_by_partial_link_text('Maestro - Kύκλος')
    titlesearch_smallSpky = driver.find_elements_by_partial_link_text('Maestro - Kύκλος')
    titlesearch_capsEpky = driver.find_elements_by_partial_link_text('MAESTRO - ΚΥΚΛΟΣ')
    titlesearch_normalEpky = driver.find_elements_by_partial_link_text('Maestro - Κυκλος')
    titlesearch_smallEpky = driver.find_elements_by_partial_link_text('Maestro - κυκλος')
    titlesearch_smallSnotpky = driver.find_elements_by_partial_link_text('Maestro - κύκλος')
    titlesearch_normalEnotpky = driver.find_elements_by_partial_link_text('Maestro - ΚΥΚΛΟΣ')
    titlesearch_smallEnotpky = driver.find_elements_by_partial_link_text('MAESTRO - ΚΥΚΛΟΣ')

    titlesearch_capsSpkys = driver.find_elements_by_partial_link_text('MAESTRO S')
    titlesearch_normalSpkys = driver.find_elements_by_partial_link_text('Maestro S')
    titlesearch_smallSpkys = driver.find_elements_by_partial_link_text('Maestro S')
    titlesearch_capsEpkys = driver.find_elements_by_partial_link_text('MAESTRO s')
    titlesearch_normalEpkys = driver.find_elements_by_partial_link_text('Maestro s')
    titlesearch_smallEpkys = driver.find_elements_by_partial_link_text('Maestro s')


    titlesearch_capsSpkyspr = driver.find_elements_by_partial_link_text('MAESTRO ΠΡΕΜΙΕΡΑ')
    titlesearch_normalSpkyspr = driver.find_elements_by_partial_link_text('Maestro Πρεμιέρα')
    titlesearch_smallSpkyspr = driver.find_elements_by_partial_link_text('Maestro πρεμιέρα')
    titlesearch_capsEpkyspr = driver.find_elements_by_partial_link_text('MAESTRO ΠΡΩΤΟ')
    titlesearch_normalEpkyspr = driver.find_elements_by_partial_link_text('MAESTRO')
    titlesearch_smallEpkyspr = driver.find_elements_by_partial_link_text('Maestro')
    titlesearch_smallEnotqdash1 = driver.find_elements_by_partial_link_text('Maestro -')
    titlesearch_smallEnotqdash2 = driver.find_elements_by_partial_link_text('MAESTRO -')
    titlesearch_smallEnotqdash3 = driver.find_elements_by_partial_link_text('MAESTRO -')
    titlesearch_smallEnotqdash4 = driver.find_elements_by_partial_link_text('Maestro -')
    titlesearch_smallEnotqdash5 = driver.find_elements_by_partial_link_text('maestro-')
    titlesearch_smallEnotqdash6 = driver.find_elements_by_partial_link_text('MAESTRO-')
    titlesearch_smallEnotqdash7 = driver.find_elements_by_partial_link_text('Maestro-')




    titlesearch =    titlesearch_smallEnotqdash7+titlesearch_smallEnotqdash6+titlesearch_smallEnotqdash5+titlesearch_smallEnotokk+titlesearch_smallEnotqdash1+titlesearch_smallEnotqdash2+titlesearch_smallEnotqdash3+titlesearch_smallEnotqdash4+titlesearch_capsSpkyspr+titlesearch_normalSpkyspr+titlesearch_smallSpkyspr+titlesearch_capsEpkyspr+titlesearch_normalEpkyspr+titlesearch_smallEpkyspr+titlesearch_capsSq+titlesearch_normalSq+titlesearch_smallSq+titlesearch_capsEq+titlesearch_normalEq+titlesearch_smallEq +titlesearch_normalSnotq+titlesearch_smallSnotq+ titlesearch_normalEnotq+titlesearch_smallEnotq+titlesearch_smallEpkys+titlesearch_normalEpkys+titlesearch_capsEpkys+titlesearch_smallSpkys+titlesearch_normalSpkys+titlesearch_capsSpkys+titlesearch_smallEnotp+titlesearch_normalEnotp+titlesearch_smallSnotp+titlesearch_normalSnotp+titlesearch_capsSp+titlesearch_normalSp+titlesearch_smallSp+titlesearch_capsEp+titlesearch_normalEp+titlesearch_smallEp+titlesearch_smallEnot+titlesearch_normalEnot+titlesearch_smallSnot+titlesearch_normalSnot+titlesearch_capsS+titlesearch_normalS+titlesearch_smallS+titlesearch_capsE+titlesearch_normalE+titlesearch_smallE+titlesearch_capsSpky+titlesearch_normalSpky+titlesearch_smallSpky+titlesearch_capsEpky+titlesearch_normalEpky+titlesearch_smallEpky+titlesearch_smallSnotpky+titlesearch_normalEnotpky+titlesearch_smallEnotpky

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    
    

    
except:

    pass

 """

#CHECKING PAISIOSENG
#30_60


driver.get("https://www.dailymotion.com/search/agios%20paisios/videos?duration=mins_30_60&sortBy=most_recent")

 


try:    
    
    time.sleep(10)

    titlesearch_caps = driver.find_elements_by_partial_link_text('Άγιος Παΐσιος')
    titlesearch_normal = driver.find_elements_by_partial_link_text('PAISIOS')
    titlesearch_small = driver.find_elements_by_partial_link_text('ΠΑΙΣΙΟΣ')
    titlesearch_smaller = driver.find_elements_by_partial_link_text('παισιος')
    titlesearch_smaller_eng = driver.find_elements_by_partial_link_text('paisios')


    titlesearch =  titlesearch_smaller_eng+titlesearch_caps+titlesearch_normal+titlesearch_small+titlesearch_smaller

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    
      
except:

    pass




#CHECKING Aparadektoi
#5_30


driver.get("https://www.dailymotion.com/search/%CE%91%CF%80%CE%B1%CF%81%CE%AC%CE%B4%CE%B5%CE%BA%CF%84%CE%BF%CE%B9/videos?duration=mins_5_30")



try:    
    
    time.sleep(10)

    titlesearch_caps = driver.find_elements_by_partial_link_text('Οι Απαράδεκτοι')
    titlesearch_normal = driver.find_elements_by_partial_link_text('Οι Απαραδεκτοι')
    titlesearch_small = driver.find_elements_by_partial_link_text('ΟΙ ΑΠΑΡΑΔΕΚΤΟΙ')
    titlesearch_smaller = driver.find_elements_by_partial_link_text('OI APARADEKTOI')


    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #driver.execute_script("window.scrollTo(0, 1080)") 

    #titlesearch2 = driver.find_elements_by_partial_link_text('ΣΙΩΠΗΛΟΣ ΔΡΟΜΟΣ')
    #titlesearch = titlesearch1+titlesearch2
    titlesearch = titlesearch_caps+titlesearch_normal+titlesearch_small+titlesearch_smaller

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    
      
except:

    pass





#CHECKING SiopilosDromos

driver.get("https://www.dailymotion.com/search/%CE%A3%CE%99%CE%A9%CE%A0%CE%97%CE%9B%CE%9F%CE%A3%20%CE%94%CE%A1%CE%9F%CE%9C%CE%9F%CE%A3/videos?duration=mins_30_60") 


try:    
    
    time.sleep(4)

    titlesearch_caps = driver.find_elements_by_partial_link_text('ΣΙΩΠΗΛΟΣ ΔΡΟΜΟΣ')
    titlesearch_normal = driver.find_elements_by_partial_link_text('Σιωπηλός Δρόμος')
    titlesearch_small = driver.find_elements_by_partial_link_text('Σιωπηλός δρόμος')
    titlesearch_smaller = driver.find_elements_by_partial_link_text('σιωπηλος δρομος')


    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #driver.execute_script("window.scrollTo(0, 1080)") 

    #titlesearch2 = driver.find_elements_by_partial_link_text('ΣΙΩΠΗΛΟΣ ΔΡΟΜΟΣ')
    #titlesearch = titlesearch1+titlesearch2
    titlesearch = titlesearch_caps+titlesearch_normal+titlesearch_small+titlesearch_smaller

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    
       
    
except:

    pass

     
#CHECKING IGitiselias
#30-60

driver.get("https://www.dailymotion.com/search/%CE%93%CE%B7%20%20%CF%84%CE%B7%CF%82%20%CE%95%CE%BB%CE%B9%CE%B1%CF%82/videos?duration=mins_30_60") 


try:    
    
    time.sleep(5)

    titlesearch_caps = driver.find_elements_by_partial_link_text('ΓΗ ΤΗΣ ΕΛΙΑΣ')
    titlesearch_normal = driver.find_elements_by_partial_link_text('Γη της Ελιάς')
    titlesearch_small = driver.find_elements_by_partial_link_text('Γη της ελιάς')
    titlesearch_smaller = driver.find_elements_by_partial_link_text('γη της ελιάς')
    titlesearch_smallerP = driver.find_elements_by_partial_link_text('Η Γη της Ελιάς-')
    titlesearch_capsall = driver.find_elements_by_partial_link_text('ΓΗ ΤΗΣ ΕΛΙΑΣ')


    titlesearch = titlesearch_capsall+titlesearch_smallerP+titlesearch_caps+titlesearch_normal+titlesearch_small+titlesearch_smaller

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    
      
    
except:

    pass

   


#CHECKING IGitiselias
#morethan1h

driver.get("https://www.dailymotion.com/search/%CE%93%CE%B7%20%20%CF%84%CE%B7%CF%82%20%CE%95%CE%BB%CE%B9%CE%B1%CF%82/videos?duration=more_than_1h")

 


try:    
    
    time.sleep(5)

    titlesearch_caps = driver.find_elements_by_partial_link_text('ΓΗ ΤΗΣ ΕΛΙΑΣ')
    titlesearch_normal = driver.find_elements_by_partial_link_text('Γη της Ελιάς')
    titlesearch_small = driver.find_elements_by_partial_link_text('Γη της ελιάς')
    titlesearch_smaller = driver.find_elements_by_partial_link_text('γη της ελιάς')
    titlesearch_smallerP = driver.find_elements_by_partial_link_text('Η Γη της Ελιάς-')
    titlesearch_capsall = driver.find_elements_by_partial_link_text('ΓΗ ΤΗΣ ΕΛΙΑΣ')


    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #driver.execute_script("window.scrollTo(0, 1080)") 

    #titlesearch2 = driver.find_elements_by_partial_link_text('ΣΙΩΠΗΛΟΣ ΔΡΟΜΟΣ')
    #titlesearch = titlesearch1+titlesearch2
    titlesearch = titlesearch_capsall+titlesearch_caps+titlesearch_normal+titlesearch_small+titlesearch_smaller

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    
      
except:

    pass



#CHECKING IGitiselias
#less30m

driver.get("https://www.dailymotion.com/search/%CE%93%CE%B7%20%20%CF%84%CE%B7%CF%82%20%CE%95%CE%BB%CE%B9%CE%B1%CF%82/videos?duration=mins_5_30")

 


try:    
    
    time.sleep(10)

    titlesearch_caps = driver.find_elements_by_partial_link_text('ΓΗ ΤΗΣ ΕΛΙΑΣ ΕΠΕΙΣΟΔΙΟ')
    titlesearch_normal = driver.find_elements_by_partial_link_text('Γη της Ελιάς Επεισόδιο')
    titlesearch_small = driver.find_elements_by_partial_link_text('Γη της ελιάς Επεισόδιο')
    titlesearch_smaller = driver.find_elements_by_partial_link_text('γη της ελιάς επεισόδιο')
    titlesearch_smallerP = driver.find_elements_by_partial_link_text('Η Γη της Ελιάς-Επ')
    titlesearch_smallerP2 = driver.find_elements_by_partial_link_text('Η Γη της Ελιάς- Επεισόδιο')

    titlesearch = titlesearch_caps+titlesearch_normal+titlesearch_small+titlesearch_smaller+titlesearch_smallerP+titlesearch_smallerP2
    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #driver.execute_script("window.scrollTo(0, 1080)") 

    #titlesearch2 = driver.find_elements_by_partial_link_text('ΣΙΩΠΗΛΟΣ ΔΡΟΜΟΣ')
    #titlesearch = titlesearch1+titlesearch2

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    
       
except:

    pass


#CHECKING KOMANTA
#30-60

driver.get("https://www.dailymotion.com/search/%CE%BA%CE%BF%CE%BC%CE%B1%CE%BD%CF%84%CE%B1%20%CE%BA%CE%B1%CE%B9%20%CE%B4%CF%81%CE%B1%CE%BA%CE%BF%CE%B9/videos?duration=mins_30_60") 
 


try:    
    
    time.sleep(10)

    titlesearch_caps = driver.find_elements_by_partial_link_text('Κομάντα και δράκοι')
    titlesearch_normal = driver.find_elements_by_partial_link_text('κομαντα και δρακοι')
    titlesearch_small = driver.find_elements_by_partial_link_text('ΚΟΜΑΝΤΑ ΚΑΙ ΔΡΑΚΟΙ')
    titlesearch_smaller = driver.find_elements_by_partial_link_text('Κομάντα Και Δράκοι')
    titlesearch_small2 = driver.find_elements_by_partial_link_text('ΚΟΜΑΝΤΑ ΚΑΙ ΔΡΑΚΟΙ')


    titlesearch = titlesearch_caps+titlesearch_normal+titlesearch_small+titlesearch_smaller+titlesearch_small2

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    
      
    
except:

    pass

 

#CHECKING SKOTEINITHALASSA
#30-60

driver.get("https://www.dailymotion.com/search/%CF%83%CE%BA%CE%BF%CF%84%CE%B5%CE%B9%CE%BD%CE%B7%20%CE%B8%CE%B1%CE%BB%CE%B1%CF%83%CF%83%CE%B1/videos?duration=mins_30_60&sortBy=most_recent") 
 


try:    
    
    time.sleep(10)

    titlesearch_caps = driver.find_elements_by_partial_link_text('Σκοτεινή θάλασσα')
    titlesearch_normal = driver.find_elements_by_partial_link_text('ΣΚΟΤΕΙΝΗ ΘΑΛΑΣΣΑ')
    titlesearch_small = driver.find_elements_by_partial_link_text('σκοτεινη θαλασσα')
    titlesearch_smaller = driver.find_elements_by_partial_link_text('Σκοτεινη Θαλασσα')
    titlesearch_small2 = driver.find_elements_by_partial_link_text('Skoteini Thalassa')
    titlesearch_caps2 = driver.find_elements_by_partial_link_text('Σκοτεινή Θάλασσα')
    titlesearch_caps3 = driver.find_elements_by_partial_link_text('σκοτεινή Θάλασσα')

    titlesearch = titlesearch_caps2+titlesearch_caps3+titlesearch_caps+titlesearch_normal+titlesearch_small+titlesearch_smaller+titlesearch_small2

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    
      
    
except:

    pass

""" #CHECKING ΡΟΔΟ
#30-60
  
driver.get("https://www.dailymotion.com/search/%CE%9C%CE%B1%CF%85%CF%81%CE%BF%20%CF%81%CE%BF%CE%B4%CE%BF/videos?duration=mins_30_60&sortBy=most_recent")
    
    

time.sleep(5)


try:    
    
    time.sleep(10)

    titlesearch_caps = driver.find_elements_by_partial_link_text('RODO EP')
    titlesearch_normal = driver.find_elements_by_partial_link_text('Ρόδο Επ')
    titlesearch_small = driver.find_elements_by_partial_link_text('ροδο Επ')
    titlesearch_smaller = driver.find_elements_by_partial_link_text('Ροδο Επ')
    titlesearch_smallerP = driver.find_elements_by_partial_link_text('ΡΟΔΟ ΕΠ')
    titlesearch_eng = driver.find_elements_by_partial_link_text('ΡΟΔΟ Επ')
    titlesearch_eng2 = driver.find_elements_by_partial_link_text('ρόδο επ')
    titlesearch_engpavla = driver.find_elements_by_partial_link_text('Μαύρο Ρόδο -')
    titlesearch_engpavla1 = driver.find_elements_by_partial_link_text('Μαυρο Ροδο -')
    titlesearch_engpavla2 = driver.find_elements_by_partial_link_text('ΡΟΔΟ -')
    titlesearch_engpavla3 = driver.find_elements_by_partial_link_text('ροδο -')
    titlesearch_engpavla4 = driver.find_elements_by_partial_link_text('Rοδο -')
    
    titlesearch_engpavlan5 = driver.find_elements_by_partial_link_text('Μαύρο ρόδο')
    titlesearch_engpavlan6 = driver.find_elements_by_partial_link_text('Μαυρο ρόδο')
    titlesearch_engpavlan7 = driver.find_elements_by_partial_link_text('Μαύρο ροδο')
    titlesearch_engpavlan8 = driver.find_elements_by_partial_link_text('ΜΑΥΡΟ ΡΟΔΟ')
    titlesearch_engpavlan9 = driver.find_elements_by_partial_link_text('μαύρο ρόδο')
    titlesearch_engpavlan10 = driver.find_elements_by_partial_link_text('μαυρο ροδο')
    titlesearch_engpavlan11 = driver.find_elements_by_partial_link_text('μαυροροδο')
    titlesearch_engpavlan12 = driver.find_elements_by_partial_link_text('Μαύρο Ρόδο')
    titlesearch_engpavlan13 = driver.find_elements_by_partial_link_text('Μαύρο Ρόδο-')
    titlesearch_engpavlan14 = driver.find_elements_by_partial_link_text('Μαύρο Ροδο-')
    titlesearch_engpavlan15 = driver.find_elements_by_partial_link_text('ΡΟΔΟ-')
    titlesearch_engpavlan16 = driver.find_elements_by_partial_link_text('ροδο-')



    titlesearch_engpavla4 = driver.find_elements_by_partial_link_text('Μαύρο Ρόδο S')
    titlesearch_engpavla5 = driver.find_elements_by_partial_link_text('Μαυρο Ροδο S')
    titlesearch_engpavla6 = driver.find_elements_by_partial_link_text('ΡΟΔΟ S')
    
    titlesearch_engpavla7 = driver.find_elements_by_partial_link_text('ροδο S ')


    titlesearch =  titlesearch_engpavlan16+titlesearch_engpavlan13+titlesearch_engpavlan14+titlesearch_engpavlan15+titlesearch_engpavlan12+titlesearch_engpavlan5+titlesearch_engpavlan11+titlesearch_engpavlan6+titlesearch_engpavlan7+titlesearch_engpavlan8+titlesearch_engpavlan10+titlesearch_engpavlan9+titlesearch_engpavla5+titlesearch_engpavla7+ titlesearch_engpavla6+ titlesearch_engpavla5+ titlesearch_engpavla4+ titlesearch_engpavla3+ titlesearch_engpavla2+ titlesearch_engpavla1+ titlesearch_engpavla+titlesearch_eng2+titlesearch_eng+titlesearch_smallerP+titlesearch_caps+titlesearch_normal+titlesearch_small+titlesearch_smaller

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    

    

    
except:

    pass




#CHECKING RODO ENGLISH
#all

driver.get("https://www.dailymotion.com/search/MAYRO%20RODO/videos")


time.sleep(10)


try:    
    
    time.sleep(10)

    titlesearch_caps = driver.find_elements_by_partial_link_text('RODO')
    titlesearch_normal = driver.find_elements_by_partial_link_text('Rodo')
    titlesearch_small = driver.find_elements_by_partial_link_text('rodo')
   



    titlesearch = titlesearch_caps+titlesearch_normal+titlesearch_small

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    

    

    
except:

    pass


#CHECKING ΡΟΔΟ
#morethan1h
  
driver.get("https://www.dailymotion.com/search/%CE%BC%CE%B1%CF%85%CF%81%CE%BF%20%CF%81%CE%BF%CE%B4%CE%BF/videos?duration=more_than_1h&sortBy=most_recent")
    
    

time.sleep(5)


try:    
    
    time.sleep(10)

    titlesearch_caps = driver.find_elements_by_partial_link_text('RODO EP')
    titlesearch_normal = driver.find_elements_by_partial_link_text('Ρόδο Επ')
    titlesearch_small = driver.find_elements_by_partial_link_text('ροδο Επ')
    titlesearch_smaller = driver.find_elements_by_partial_link_text('Ροδο Επ')
    titlesearch_smallerP = driver.find_elements_by_partial_link_text('ΡΟΔΟ ΕΠ')
    titlesearch_eng = driver.find_elements_by_partial_link_text('ΡΟΔΟ Επ')
    titlesearch_eng2 = driver.find_elements_by_partial_link_text('ρόδο επ')
    titlesearch_engpavla = driver.find_elements_by_partial_link_text('Μαύρο Ρόδο -')
    titlesearch_engpavla1 = driver.find_elements_by_partial_link_text('Μαυρο Ροδο -')
    titlesearch_engpavla2 = driver.find_elements_by_partial_link_text('ΡΟΔΟ -')
    titlesearch_engpavla3 = driver.find_elements_by_partial_link_text('ροδο -')
    titlesearch_engpavla4 = driver.find_elements_by_partial_link_text('Rοδο -')
    
    titlesearch_engpavlan5 = driver.find_elements_by_partial_link_text('Μαύρο ρόδο')
    titlesearch_engpavlan6 = driver.find_elements_by_partial_link_text('Μαυρο ρόδο')
    titlesearch_engpavlan7 = driver.find_elements_by_partial_link_text('Μαύρο ροδο')
    titlesearch_engpavlan8 = driver.find_elements_by_partial_link_text('ΜΑΥΡΟ ΡΟΔΟ')
    titlesearch_engpavlan9 = driver.find_elements_by_partial_link_text('μαύρο ρόδο')
    titlesearch_engpavlan10 = driver.find_elements_by_partial_link_text('μαυρο ροδο')
    titlesearch_engpavlan11 = driver.find_elements_by_partial_link_text('μαυροροδο')
    titlesearch_engpavlan12 = driver.find_elements_by_partial_link_text('Μαύρο Ρόδο')
    titlesearch_engpavlan13 = driver.find_elements_by_partial_link_text('Μαύρο Ρόδο-')
    titlesearch_engpavlan14 = driver.find_elements_by_partial_link_text('Μαύρο Ροδο-')
    titlesearch_engpavlan15 = driver.find_elements_by_partial_link_text('ΡΟΔΟ-')
    titlesearch_engpavlan16 = driver.find_elements_by_partial_link_text('ροδο-')



    titlesearch_engpavla4 = driver.find_elements_by_partial_link_text('Μαύρο Ρόδο S')
    titlesearch_engpavla5 = driver.find_elements_by_partial_link_text('Μαυρο Ροδο S')
    titlesearch_engpavla6 = driver.find_elements_by_partial_link_text('ΡΟΔΟ S')
    
    titlesearch_engpavla7 = driver.find_elements_by_partial_link_text('ροδο S ')


    titlesearch =  titlesearch_engpavlan16+titlesearch_engpavlan13+titlesearch_engpavlan14+titlesearch_engpavlan15+titlesearch_engpavlan12+titlesearch_engpavlan5+titlesearch_engpavlan11+titlesearch_engpavlan6+titlesearch_engpavlan7+titlesearch_engpavlan8+titlesearch_engpavlan10+titlesearch_engpavlan9+titlesearch_engpavla5+titlesearch_engpavla7+ titlesearch_engpavla6+ titlesearch_engpavla5+ titlesearch_engpavla4+ titlesearch_engpavla3+ titlesearch_engpavla2+ titlesearch_engpavla1+ titlesearch_engpavla+titlesearch_eng2+titlesearch_eng+titlesearch_smallerP+titlesearch_caps+titlesearch_normal+titlesearch_small+titlesearch_smaller

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    

    

    
except:

    pass






#CHECKING SYMPETHEROI APO
#30-60
  
driver.get("https://www.dailymotion.com/search/%CE%A4%CE%B9%CF%81%CE%B1%CE%BD%CE%B1/videos?duration=mins_30_60&sortBy=most_recent")
    
    

time.sleep(5)


try:    
    
    time.sleep(10)

    titlesearch_caps = driver.find_elements_by_partial_link_text('ΤΙΡΑΝΑ')
    titlesearch_normal = driver.find_elements_by_partial_link_text('Τιρανα')
    titlesearch_small = driver.find_elements_by_partial_link_text('τιρανα')
    titlesearch_smaller = driver.find_elements_by_partial_link_text('Τίρανα')
    titlesearch_smallerP = driver.find_elements_by_partial_link_text('TIPANA')
    titlesearch_eng = driver.find_elements_by_partial_link_text('SIMPETHERI APO TA TIRANA')
    titlesearch_eng2 = driver.find_elements_by_partial_link_text('SIMPETHEROI')



    titlesearch = titlesearch_eng2+titlesearch_eng+titlesearch_smallerP+titlesearch_caps+titlesearch_normal+titlesearch_small+titlesearch_smaller

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    

    

    
except:

    pass


 """


#CHECKING FAMAGUSTA
#60+


driver.get("https://www.dailymotion.com/search/famagusta/videos?duration=more_than_1h&sortBy=most_recent")

 


try:    
    
    time.sleep(5)

    titlesearch_caps = driver.find_elements_by_partial_link_text('Famagusta')
    titlesearch_normal = driver.find_elements_by_partial_link_text('FAMAGUSTA')
    titlesearch_small = driver.find_elements_by_partial_link_text('Fama Gusta')
    titlesearch_smaller = driver.find_elements_by_partial_link_text('famagusta')
    titlesearch_smaller_eng = driver.find_elements_by_partial_link_text('FAMA GUSTA')
    titlesearch_smaller_gr6 = driver.find_elements_by_partial_link_text('Famagousta')
    titlesearch_smaller_gr7 = driver.find_elements_by_partial_link_text('FAMAGOUSTA')
    titlesearch_smaller_gr8 = driver.find_elements_by_partial_link_text('famagousta')


    titlesearch_smaller_gr = driver.find_elements_by_partial_link_text('φαμαγκουστα')



    titlesearch =  titlesearch_smaller_gr6+titlesearch_smaller_gr7+titlesearch_smaller_gr8+titlesearch_smaller_gr+titlesearch_smaller_eng+titlesearch_caps+titlesearch_normal+titlesearch_small+titlesearch_smaller

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    
      
except:

    pass



#CHECKING FAMAGUSTAGR
#60+


driver.get("https://www.dailymotion.com/search/%CF%86%CE%B1%CE%BC%CE%B1%CE%B3%CE%BA%CE%BF%CF%85%CF%83%CF%84%CE%B1/videos?duration=more_than_1h&sortBy=most_recent")

 


try:    
    
    time.sleep(5)

    titlesearch_caps = driver.find_elements_by_partial_link_text('Φαμαγκουστα')
    titlesearch_normal = driver.find_elements_by_partial_link_text('φαμαγκούστα')
    titlesearch_small = driver.find_elements_by_partial_link_text('ΦΑΜΑΓΚΟΥΣΤΑ')
    titlesearch_smaller = driver.find_elements_by_partial_link_text('Φαμαγκούστα')
    titlesearch_smaller_eng = driver.find_elements_by_partial_link_text('Φαμαγκουστα')

    titlesearch_smaller_gr = driver.find_elements_by_partial_link_text('φαμαγκουστα')
    titlesearch_smaller_gr1 = driver.find_elements_by_partial_link_text('φαμαγουστα')
    titlesearch_smaller_gr2 = driver.find_elements_by_partial_link_text('Φαμαγουστα')
    titlesearch_smaller_gr3 = driver.find_elements_by_partial_link_text('Φαμαγούστα')
    titlesearch_smaller_gr4 = driver.find_elements_by_partial_link_text('ΦΑΜΑΓΟΥΣΤΑ')

    titlesearch_smaller_gr5 = driver.find_elements_by_partial_link_text('Famagusta')







    titlesearch =  titlesearch_smaller_gr1+titlesearch_smaller_gr2+titlesearch_smaller_gr3+titlesearch_smaller_gr4+titlesearch_smaller_gr+titlesearch_smaller_eng+titlesearch_caps+titlesearch_normal+titlesearch_small+titlesearch_smaller

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    
      
except:

    pass


#CHECKING DJK
driver.get("https://www.dailymotion.com/djkchannel3/videos")


try: 

    titlesearch2 = driver.find_elements_by_partial_link_text('Ν')
    titlesearch1 = driver.find_elements_by_partial_link_text('Γη')
    titlesearch3 = driver.find_elements_by_partial_link_text('ΓH')
    titlesearch4 = driver.find_elements_by_partial_link_text('G')
    titlesearch5 = driver.find_elements_by_partial_link_text('.')
    titlesearch6 = driver.find_elements_by_partial_link_text('Mil')




    titlesearch=titlesearch1+titlesearch2+titlesearch3+titlesearch4+titlesearch5+titlesearch6

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    


except:

    pass


#CHECKING wise
driver.get("https://www.dailymotion.com/WildsSurvival")


try: 

    titlesearch2 = driver.find_elements_by_partial_link_text('Ν')
    titlesearch1 = driver.find_elements_by_partial_link_text('Γη')
    titlesearch3 = driver.find_elements_by_partial_link_text('ΓH')
    titlesearch4 = driver.find_elements_by_partial_link_text('G')
    titlesearch5 = driver.find_elements_by_partial_link_text('.')
    titlesearch6 = driver.find_elements_by_partial_link_text('Mil')




    titlesearch=titlesearch1+titlesearch2+titlesearch3+titlesearch4+titlesearch5+titlesearch6

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    


except:

    pass



#CHECKING Aparadektoi
#5_30


driver.get("https://www.dailymotion.com/search/%CE%91%CF%80%CE%B1%CF%81%CE%AC%CE%B4%CE%B5%CE%BA%CF%84%CE%BF%CE%B9/videos?duration=mins_5_30")



try:    
    
    time.sleep(10)

    titlesearch_caps = driver.find_elements_by_partial_link_text('Οι Απαράδεκτοι')
    titlesearch_normal = driver.find_elements_by_partial_link_text('Οι Απαραδεκτοι')
    titlesearch_small = driver.find_elements_by_partial_link_text('ΟΙ ΑΠΑΡΑΔΕΚΤΟΙ')
    titlesearch_smaller = driver.find_elements_by_partial_link_text('OI APARADEKTOI')


    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #driver.execute_script("window.scrollTo(0, 1080)") 

    #titlesearch2 = driver.find_elements_by_partial_link_text('ΣΙΩΠΗΛΟΣ ΔΡΟΜΟΣ')
    #titlesearch = titlesearch1+titlesearch2
    titlesearch = titlesearch_caps+titlesearch_normal+titlesearch_small+titlesearch_smaller

    for video in titlesearch:
        title = video.text
        url = video.get_attribute("href")
        dm_list_allMEGA.append(url)    
      
except:

    pass






if len (dm_list_allMEGA) > 0:
    #open 
    if Path("/home/nickospi/dm_list_allMEGA.csv").is_file():
        with open('/home/nickospi/dm_list_allMEGA.csv', 'r') as f:
            old_dm_list_allMEGA = f.read().splitlines()
            #compare dm_list_allMEGA with old_dm_list_allMEG and remove duplicates
            dm_list_allMEGA = list(set(dm_list_allMEGA) - set(old_dm_list_allMEGA))
            toremove = ['https://www.dailymotion.com/legal/consent#dailymotion', 'https://www.dailymotion.com/legal/consent#specialFeatures-section']
            dm_list_allMEGA = [x for x in dm_list_allMEGA if x not in toremove]


            if len (dm_list_allMEGA) > 0:

                        
                smtp = smtplib.SMTP()
                smtp.connect('localhost')
                msgRoot = MIMEMultipart("alternative")
                msgRoot['Subject'] = Header("DMCA Notice_request for immediate removal of content", "utf-8")
                msgRoot['From'] = "npitsiladis@megatv.com"
                msgRoot['To']  =  "feedback@dailymotion.com"
                
                html ='Dear Sir/Madam, some new links of our series have been found on your website. MEGA TV, a national TV broadcaster and producer from Greece, is the sole owner of the copyrighted material found on your website and has never granted any license to the uploader. The whole uploaded video (100%) is infringing as it is a whole episode.Thus, we demand immediate removal of this content:\n'+"\n"','.join([str(i) for i in dm_list_allMEGA])+'\n I state that upon a good faith belief the disputed use of the material or activity is not authorized by the copyright or intellectual property owner, its agent or the law and under penalty of perjury, MEGA TV is the copyright or intellectual property owner or is authorized to act on behalf of the copyright or intellectual property owner and that the information provided in the notice is accurate.Also (i) I have good faith belief that use of the material in the manner complained of is not authorized by the copyright owner, its agent, or the law.(ii) I swear under penalty of perjury, that the information in this notification is accurate and I am the copyright owner or am authorized to act on behalf of the owner of an exclusive right that is allegedly infringed.(iii) I accept that my private data will only be used by Dailymotion in the context of its copyright notification process which include sharing a copy of this claim with the user(s) who uploaded the allegedly infringing material.(iv) I recognize that I may be liable for damages if I knowingly materially misrepresent that the material or activity infringes on my copyright.'+'\n Nikos Pitsiladis Digital Manager \nSyggrou Ave 35, 17565, Athens-GREECE\nThank you'

                part1 = MIMEText(html, 'html')
                msgRoot.attach(part1)
                smtp.sendmail("npitsiladis@megatv.com","feedback@dailymotion.com", msgRoot.as_string())


                #save the new list to a csv file
                with open('dm_list_allMEGA.csv', 'w') as f:
                    for item in dm_list_allMEGA:
                        f.write("%s\n" % item)
            
                print('reported dm'+"\n"','.join([str(i) for i in dm_list_allMEGA]))


            else:
                print('no new links on dm')
    else:
        print ('no old file')







else:
    print('did not report any dm')



driver.quit()
driver.quit()
driver.quit()
driver.quit()
driver.quit()



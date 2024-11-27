from __future__ import absolute_import, unicode_literals

#mail
import smtplib, ssl
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
#from selenium.webdriver.common.action_chains import ActionChains
from urllib.request import urlopen
import requests
import re
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
display = Display(visible=0, size=(2400, 2400))  
display.start()

gmail_user = 'dmcagreektv@gmail.com'
gmail_password = 'nbqtgzvlsrjgxlzc'


tmstmp = time.strftime("%d-%m-%Y %H%M%S")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--start-maximized")
chrome_options.headless = True
driver = webdriver.Chrome(options=chrome_options)
driver.create_options()

#LISTS

dm_list=[]
mixdrop_list=[]
tune_list = []
streamzz_list=[]
streamtape_list=[]
voe_list=[]
redload_list=[]
vtube_list=[]
rumble_list=[]
wolfstream_list=[]
strmhd_list=[]
youtube_list=[]
streamruby_list=[]
filelions_list=[]
dropload_list=[]


#ΜΑΕΣΤΟΡ
driver.get("https://greek-movies.com/series.php?s=1151") 
time.sleep(3)
try: 
    cookies = driver.find_element_by_xpath ('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()

except:
    pass


url_list=[]

  
try:
    for no in range(1, 9):
        time.sleep(2)
        latest = driver.find_element_by_xpath ('/html/body/div[2]/div[2]/div[2]/div[4]/div[1]/button['+str(no)+']').click()
        time.sleep(3)
        urls = driver.find_elements_by_tag_name("a")
        for u in urls:
            url = u.get_attribute("href")
            url_list.append(url)
            
        x = driver.find_element_by_xpath ('//*[@id="mw"]/div/div/div/div/div/button')
        x.click()

except:
    pass

df_ΜΑΕ = pd.DataFrame(url_list,columns =['url'])



df_ΜΑΕ=df_ΜΑΕ[df_ΜΑΕ.url.str.contains('greek-movies.com/view.php')==True]


for item in df_ΜΑΕ:
    def get_url(row):
        driver.get(row['url'])       
        act_url = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[3]/a")
        return pd.Series({
            'actual_url': act_url.get_attribute('href')
        })


f_df_ΜΑΕ = df_ΜΑΕ.apply(get_url, axis=1).join(df_ΜΑΕ)

#save to csv 
f_df_ΜΑΕ.to_csv('MAESTRO.csv', index=None)
   
    
if f_df_ΜΑΕ.empty:

    pass
        

else: 
    for item in f_df_ΜΑΕ.actual_url:
        
        if 'tune.pk' in item:
            tune_list.append(item)
        if 'streamtape' in item:
            streamtape_list.append(item)
        if 'voe.sx' in item:
            voe_list.append(item)  
        if 'vtube' in item:
            vtube_list.append(item)
        if 'redload' in item:
            redload_list.append(item)
        if 'mixdrop' in item:
            mixdrop_list.append(item)
        if 'wolfstream' in item: 
            wolfstream_list.append(item)
        if 'streamhide' in item:
            strmhd_list.append(item)
        if 'dailymotion' in item:
            dm_list.append(item)
        if 'youtube' in item:
            youtube_list.append(item)
        if 'streamruby' in item:
            streamruby_list.append(item)
        if 'filelions' in item:
            filelions_list.append(item)
        if 'dropload' in item:
            dropload_list.append(item)




#FAMAGUSTA
driver.get("https://greek-movies.com/series.php?s=1204") 
time.sleep(3)
try: 
    cookies = driver.find_element_by_xpath ('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()

except:
    pass

url_list=[]


time.sleep(2)
try:
    latest = driver.find_element_by_xpath ('/html/body/div[2]/div[2]/div[2]/div[4]/div[1]/button').click() #button [1][2] etc.    
    time.sleep(3)
    urls = driver.find_elements_by_tag_name("a")
    for u in urls:
        url = u.get_attribute("href")
        url_list.append(url)
        
    x = driver.find_element_by_xpath ('//*[@id="mw"]/div/div/div/div/div/button')
    x.click()
except:
    pass

df_FAMA = pd.DataFrame(url_list,columns =['url'])



df_FAMA=df_FAMA[df_FAMA.url.str.contains('greek-movies.com/view.php')==True]


for item in df_FAMA:
    def get_url(row):
        driver.get(row['url'])       
        act_url = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[3]/a")
            
        return pd.Series({
            'actual_url': act_url.get_attribute('href')
        })


f_df_FAMA = df_FAMA.apply(get_url, axis=1).join(df_FAMA)

#save to csv 
#f_df_FAMA.to_csv('FAM.csv', index=None) 
    
if f_df_FAMA.empty:

    pass
        

else: 
    print ('FAMA OK')
    for item in f_df_FAMA.actual_url:
        
          
        if 'tune.pk' in item:
            tune_list.append(item)
        if 'streamtape' in item:
            streamtape_list.append(item)
        if 'voe.sx' in item:
            voe_list.append(item)  
        if 'vtube' in item:
            vtube_list.append(item)
        if 'redload' in item:
            redload_list.append(item)
        if 'mixdrop' in item:
            mixdrop_list.append(item)
        if 'wolfstream' in item: 
            wolfstream_list.append(item)
        if 'streamhide' in item:
            strmhd_list.append(item)
        if 'dailymotion' in item:
            dm_list.append(item)
        if 'youtube' in item:
            youtube_list.append(item)
        if 'streamruby' in item:
            streamruby_list.append(item)
        if 'filelions' in item:
            filelions_list.append(item)
        if 'dropload' in item:
            dropload_list.append(item)






#SD
driver.get("https://greek-movies.com/series.php?s=1081") 
time.sleep(3)
try: 
    cookies = driver.find_element_by_xpath ('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()

except:
    pass

url_list=[]

for no in range(1, 14):
    time.sleep(2)
    try:
        latest = driver.find_element_by_xpath ('/html/body/div[2]/div[2]/div[2]/div[4]/div[1]/button['+str(no)+']').click() #button [1][2] etc.    
        time.sleep(3)
        urls = driver.find_elements_by_tag_name("a")
        for u in urls:
            url = u.get_attribute("href")
            url_list.append(url)
            
        x = driver.find_element_by_xpath ('//*[@id="mw"]/div/div/div/div/div/button')
        x.click()
    except:
        pass

df_SD = pd.DataFrame(url_list,columns =['url'])



df_SD=df_SD[df_SD.url.str.contains('greek-movies.com/view.php')==True]


for item in df_SD:
    def get_url(row):
        driver.get(row['url'])       
        act_url = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[3]/a")
            
        return pd.Series({
            'actual_url': act_url.get_attribute('href')
        })


f_df_SD = df_SD.apply(get_url, axis=1).join(df_SD)

#save to csv 
f_df_SD.to_csv('SD.csv', index=None) 
    
if f_df_SD.empty:

    pass
        

else: 
    for item in f_df_SD.actual_url:
        
              
        if 'tune.pk' in item:
            tune_list.append(item)
        if 'streamtape' in item:
            streamtape_list.append(item)
        if 'voe.sx' in item:
            voe_list.append(item)  
        if 'vtube' in item:
            vtube_list.append(item)
        if 'redload' in item:
            redload_list.append(item)
        if 'mixdrop' in item:
            mixdrop_list.append(item)
        if 'wolfstream' in item: 
            wolfstream_list.append(item)
        if 'streamhide' in item:
            strmhd_list.append(item)
        if 'dailymotion' in item:
            dm_list.append(item)
        if 'youtube' in item:
            youtube_list.append(item)
        if 'streamruby' in item:
            streamruby_list.append(item)
        if 'filelions' in item:
            filelions_list.append(item)
        if 'dropload' in item:
            dropload_list.append(item)









#NAVAGOP


driver.get("https://greek-movies.com/series.php?s=1192") 
time.sleep(3)
try: 
    cookies = driver.find_element_by_xpath ('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()
except:
    pass

url_list=[]

time.sleep(2)
for no in range(1,30): 
    time.sleep(2)
    try:
        latest = driver.find_element_by_xpath ('/html/body/div[2]/div[2]/div[2]/div[4]/div[1]/button['+str(no)+']').click()
        time.sleep(2)
        urls = driver.find_elements_by_tag_name("a")
        for u in urls:
            
            try:
                url = u.get_attribute("href")
                url_list.append(url)
            except:
                pass    

        x = driver.find_element_by_xpath ('//*[@id="mw"]/div/div/div/div/div/button')
        x.click()
    except:
        pass

df_NAV = pd.DataFrame(url_list,columns =['url'])
df_NAV=df_NAV[df_NAV.url.str.contains('greek-movies.com/view.php')==True]


for item in df_NAV:
    def get_url(row):
        driver.get(row['url'])       
        act_url = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[3]/a")
            
        return pd.Series({
            'actual_url': act_url.get_attribute('href')
        })


f_df_NAV = df_NAV.apply(get_url, axis=1).join(df_NAV)
#save to csv 
f_df_NAV.to_csv('RODO.csv', index=None)
   
if f_df_NAV.empty:

    pass
    

        

else: 

    for item in f_df_NAV.actual_url:
    
    
              
        if 'tune.pk' in item:
            tune_list.append(item)
        if 'streamtape' in item:
            streamtape_list.append(item)
        if 'voe.sx' in item:
            voe_list.append(item)  
        if 'vtube' in item:
            vtube_list.append(item)
        if 'redload' in item:
            redload_list.append(item)
        if 'mixdrop' in item:
            mixdrop_list.append(item)
        if 'wolfstream' in item: 
            wolfstream_list.append(item)
        if 'streamhide' in item:
            strmhd_list.append(item)
        if 'dailymotion' in item:
            dm_list.append(item)
        if 'youtube' in item:
            youtube_list.append(item)
        if 'streamruby' in item:
            streamruby_list.append(item)
        if 'filelions' in item:
            filelions_list.append(item)
        if 'dropload' in item:
            dropload_list.append(item)



#MILKYWAY


driver.get("https://greek-movies.com/series.php?s=1200") 
time.sleep(3)
try: 
    cookies = driver.find_element_by_xpath ('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()
except:
    pass

url_list=[]

time.sleep(2)
for no in range(1,9): 
    time.sleep(2)
    try:
        latest = driver.find_element_by_xpath ('/html/body/div[2]/div[2]/div[2]/div[4]/div[1]/button['+str(no)+']').click()
        time.sleep(2)
        urls = driver.find_elements_by_tag_name("a")
        for u in urls:
            
            try:
                url = u.get_attribute("href")
                url_list.append(url)
            except:
                pass    

        x = driver.find_element_by_xpath ('//*[@id="mw"]/div/div/div/div/div/button')
        x.click()
    except:
        pass

df_MW = pd.DataFrame(url_list,columns =['url'])
df_MW=df_MW[df_MW.url.str.contains('greek-movies.com/view.php')==True]


for item in df_MW:
    def get_url(row):
        driver.get(row['url'])       
        act_url = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[3]/a")
            
        return pd.Series({
            'actual_url': act_url.get_attribute('href')
        })


f_df_MW = df_MW.apply(get_url, axis=1).join(df_MW)
#save to csv 
f_df_MW.to_csv('RODO.csv', index=None)
   
if f_df_MW.empty:

    pass
    

        

else: 

    for item in f_df_MW.actual_url:
    
    
          
        if 'tune.pk' in item:
            tune_list.append(item)
        if 'streamtape' in item:
            streamtape_list.append(item)
        if 'voe.sx' in item:
            voe_list.append(item)  
        if 'vtube' in item:
            vtube_list.append(item)
        if 'redload' in item:
            redload_list.append(item)
        if 'mixdrop' in item:
            mixdrop_list.append(item)
        if 'wolfstream' in item: 
            wolfstream_list.append(item)
        if 'streamhide' in item:
            strmhd_list.append(item)
        if 'dailymotion' in item:
            dm_list.append(item)
        if 'youtube' in item:
            youtube_list.append(item)
        if 'streamruby' in item:
            streamruby_list.append(item)
        if 'filelions' in item:
            filelions_list.append(item)
        if 'dropload' in item:
            dropload_list.append(item)










#PAISIOS
driver.get("https://greek-movies.com/series.php?s=1121") 
time.sleep(3)


url_list=[]

for no in range(1, 10):
    time.sleep(2)
    try:
        latest = driver.find_element_by_xpath ('/html/body/div[2]/div[2]/div[2]/div[4]/div[1]/button['+str(no)+']').click()
        time.sleep(3)
        urls = driver.find_elements_by_tag_name("a")
        for u in urls:
            url = u.get_attribute("href")
            url_list.append(url)
            
        x = driver.find_element_by_xpath ('//*[@id="mw"]/div/div/div/div/div/button')
        x.click()
    except:
        pass

df_PAIS = pd.DataFrame(url_list,columns =['url'])



df_PAIS=df_PAIS[df_PAIS.url.str.contains('greek-movies.com/view.php')==True]


for item in df_PAIS:
    def get_url(row):
        driver.get(row['url'])       
        act_url = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[3]/a")
            
        return pd.Series({
            'actual_url': act_url.get_attribute('href')
        })


f_df_PAIS = df_PAIS.apply(get_url, axis=1).join(df_PAIS)
#save to csv 
f_df_PAIS.to_csv('PAISIOS.csv', index=None)
if f_df_PAIS.empty:

    pass
else:   

    for item in f_df_PAIS.actual_url:
        
             
        if 'tune.pk' in item:
            tune_list.append(item)
        if 'streamtape' in item:
            streamtape_list.append(item)
        if 'voe.sx' in item:
            voe_list.append(item)  
        if 'vtube' in item:
            vtube_list.append(item)
        if 'redload' in item:
            redload_list.append(item)
        if 'mixdrop' in item:
            mixdrop_list.append(item)
        if 'wolfstream' in item: 
            wolfstream_list.append(item)
        if 'streamhide' in item:
            strmhd_list.append(item)
        if 'dailymotion' in item:
            dm_list.append(item)
        if 'youtube' in item:
            youtube_list.append(item)
        if 'streamruby' in item:
            streamruby_list.append(item)
        if 'filelions' in item:
            filelions_list.append(item)
        if 'dropload' in item:
            dropload_list.append(item)


        


#MYREPORT

sent_from = gmail_user
to = ['dmcagreektv@gmail.com']
subject = 'DMCA Notice_request for immediate removal of content'
body = "MEGA DMCAs sent at"+tmstmp+" "+" YOUTUBE "+"\n".join(youtube_list)+" Dailymotion "+"\n".join(dm_list)+" Streamhide "+"\n".join(strmhd_list)+" Rumble "+"\n".join(rumble_list)+" redload "+"\n".join(redload_list)+" Vtube "+"\n".join(vtube_list)+" Voe "+"\n".join(voe_list)+" Streamtape "+"\n".join(streamtape_list)+" Streamzz "+"\n".join(streamzz_list) + " Mixdrop " + "\n".join(mixdrop_list) + "See you later aligator"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!sent general report')
except:
    print ('Something went wrong with gmail sending general report')



#PROVIDERS


if len (wolfstream_list) > 0:

    smtp = smtplib.SMTP()
    smtp.connect('localhost')

    msgRoot = MIMEMultipart("alternative")
    msgRoot['Subject'] = Header("DMCA Notice_request for immediate removal of content", "utf-8")
    msgRoot['From'] = "npitsiladis@megatv.com"

    recipients = ["abuse@namecheap.com","info@WolfStream.tv", "abuse@ipconnect.services", "abuse@colocrossing.com"]
    recipients_str = ','.join(recipients)
    msgRoot['To']  =  recipients_str
    html ='Dear Sir/Madam, some new links have been found on your website. MEGA TV, a national TV broadcaster and producer from Greece, is the sole owner of the copyrighted material found on your website and has never granted any license to the uploader. The whole uploaded video (100%) is infringing as it is a whole episode.Thus, we demand immediate removal of this content:\n'+"\n".join(wolfstream_list)+'\nI state that upon a good faith belief the disputed use of the material or activity is not authorized by the copyright or intellectual property owner, its agent or the law and under penalty of perjury, MEGA TV is the copyright or intellectual property owner or is authorized to act on behalf of the copyright or intellectual property owner and that the information provided in the notice is accurate.Also (i) I have good faith belief that use of the material in the manner complained of is not authorized by the copyright owner, its agent, or the law.(ii) I swear under penalty of perjury, that the information in this notification is accurate and I am the copyright owner or am authorized to act on behalf of the owner of an exclusive right that is allegedly infringed.(iii) I accept that my private data will only be used by you in the context of its copyright notification process which include sharing a copy of this claim with the user(s) who uploaded the allegedly infringing material.(iv) I recognize that I may be liable for damages if I knowingly materially misrepresent that the material or activity infringes on my copyright.'+'\n Nikos Pitsiladis Digital Manager \nSyggrou Ave 35, 17565, Athens-GREECE\nThank you'
    part1 = MIMEText(html, 'html')
    msgRoot.attach(part1)
    smtp.sendmail("npitsiladis@megatv.com",recipients_str, msgRoot.as_string())
    print ('wolfstream reported ')



if len (strmhd_list) > 0:

    smtp = smtplib.SMTP()
    smtp.connect('localhost')

    msgRoot = MIMEMultipart("alternative")
    msgRoot['Subject'] = Header("DMCA Notice_request for immediate removal of content on streamhide.to", "utf-8")
    msgRoot['From'] = "npitsiladis@megatv.com"

    msgRoot['To'] = "abuse@ipconnect.services"
    html ='Dear Sir/Madam, some new links have been found on streamhide.to to which you are the hosting provider. MEGA TV, a national TV broadcaster and producer from Greece, is the sole owner of the copyrighted material found on streamhide.to which you host and has never granted any license to the uploader. The whole uploaded video (100%) is infringing as it is a whole episode.Thus, we demand immediate removal of this content:\n'+"\n".join(strmhd_list)+'\nI state that upon a good faith belief the disputed use of the material or activity is not authorized by the copyright or intellectual property owner, its agent or the law and under penalty of perjury, MEGA TV is the copyright or intellectual property owner or is authorized to act on behalf of the copyright or intellectual property owner and that the information provided in the notice is accurate.Also (i) I have good faith belief that use of the material in the manner complained of is not authorized by the copyright owner, its agent, or the law.(ii) I swear under penalty of perjury, that the information in this notification is accurate and I am the copyright owner or am authorized to act on behalf of the owner of an exclusive right that is allegedly infringed.(iii) I accept that my private data will only be used by you in the context of its copyright notification process which include sharing a copy of this claim with the user(s) who uploaded the allegedly infringing material.(iv) I recognize that I may be liable for damages if I knowingly materially misrepresent that the material or activity infringes on my copyright.'+'\n Nikos Pitsiladis Digital Manager \nSyggrou Ave 35, 17565, Athens-GREECE\nThank you'
    part1 = MIMEText(html, 'html')
    msgRoot.attach(part1)
    smtp.sendmail("npitsiladis@megatv.com", "abuse@ipconnect.services", msgRoot.as_string())
    print ('strmhd reported ')



if len (tune_list) > 0:

    smtp = smtplib.SMTP()
    smtp.connect('localhost')

    msgRoot = MIMEMultipart("alternative")
    msgRoot['Subject'] = Header("DMCA Notice_request for immediate removal of content", "utf-8")
    msgRoot['From'] = "npitsiladis@megatv.com"

    msgRoot['To'] = "contact@tune.pk"
    html ='Dear Sir/Madam, some new links have been found on your website. MEGA TV, a national TV broadcaster and producer from Greece, is the sole owner of the copyrighted material found on your website and has never granted any license to the uploader. The whole uploaded video (100%) is infringing as it is a whole episode.Thus, we demand immediate removal of this content:\n'+"\n".join(tune_list)+'\nI state that upon a good faith belief the disputed use of the material or activity is not authorized by the copyright or intellectual property owner, its agent or the law and under penalty of perjury, MEGA TV is the copyright or intellectual property owner or is authorized to act on behalf of the copyright or intellectual property owner and that the information provided in the notice is accurate.Also (i) I have good faith belief that use of the material in the manner complained of is not authorized by the copyright owner, its agent, or the law.(ii) I swear under penalty of perjury, that the information in this notification is accurate and I am the copyright owner or am authorized to act on behalf of the owner of an exclusive right that is allegedly infringed.(iii) I accept that my private data will only be used by you in the context of its copyright notification process which include sharing a copy of this claim with the user(s) who uploaded the allegedly infringing material.(iv) I recognize that I may be liable for damages if I knowingly materially misrepresent that the material or activity infringes on my copyright.'+'\n Nikos Pitsiladis Digital Manager \nSyggrou Ave 35, 17565, Athens-GREECE\nThank you'
    part1 = MIMEText(html, 'html')
    msgRoot.attach(part1)
    smtp.sendmail("npitsiladis@megatv.com", "contact@tune.pk", msgRoot.as_string())
    print ('tune.pk reported ')



if len (rumble_list) > 0:

    smtp = smtplib.SMTP()
    smtp.connect('localhost')

    msgRoot = MIMEMultipart("alternative")
    msgRoot['Subject'] = Header("DMCA Notice_request for immediate removal of content", "utf-8")
    msgRoot['From'] = "npitsiladis@megatv.com"

    msgRoot['To'] = "dmca@rumble.com"
    html ='Dear Sir/Madam, some new links have been found on your website. MEGA TV, a national TV broadcaster and producer from Greece, is the sole owner of the copyrighted material found on your website and has never granted any license to the uploader. The whole uploaded video (100%) is infringing as it is a whole episode.Thus, we demand immediate removal of this content:\n'+"\n".join(rumble_list)+'\nI state that upon a good faith belief the disputed use of the material or activity is not authorized by the copyright or intellectual property owner, its agent or the law and under penalty of perjury, MEGA TV is the copyright or intellectual property owner or is authorized to act on behalf of the copyright or intellectual property owner and that the information provided in the notice is accurate.Also (i) I have good faith belief that use of the material in the manner complained of is not authorized by the copyright owner, its agent, or the law.(ii) I swear under penalty of perjury, that the information in this notification is accurate and I am the copyright owner or am authorized to act on behalf of the owner of an exclusive right that is allegedly infringed.(iii) I accept that my private data will only be used by you in the context of its copyright notification process which include sharing a copy of this claim with the user(s) who uploaded the allegedly infringing material.(iv) I recognize that I may be liable for damages if I knowingly materially misrepresent that the material or activity infringes on my copyright.'+'\n Nikos Pitsiladis Digital Manager \nSyggrou Ave 35, 17565, Athens-GREECE\nThank you'
    part1 = MIMEText(html, 'html')
    msgRoot.attach(part1)
    smtp.sendmail("npitsiladis@megatv.com", "dmca@rumble.com", msgRoot.as_string())
    print ('rumble.com reported ')


if len (streamtape_list) > 0:
    
    smtp = smtplib.SMTP()
    smtp.connect('localhost')
    msgRoot = MIMEMultipart("alternative")
    msgRoot['Subject'] = Header("DMCA Notice_request for immediate removal of content", "utf-8")
    msgRoot['From'] = "npitsiladis@megatv.com"
    msgRoot['To']  =  "dmca@streamtape.com"
    html ='Dear Sir/Madam, some new links have been found on your website. MEGA TV, a national TV broadcaster and producer from Greece, is the sole owner of the copyrighted material found on your website and has never granted any license to the uploader. The whole uploaded video (100%) is infringing as it is a whole episode.Thus, we demand immediate removal of this content:\n'+"\n".join(streamtape_list)+'\nI state that upon a good faith belief the disputed use of the material or activity is not authorized by the copyright or intellectual property owner, its agent or the law and under penalty of perjury, MEGA TV is the copyright or intellectual property owner or is authorized to act on behalf of the copyright or intellectual property owner and that the information provided in the notice is accurate.Also (i) I have good faith belief that use of the material in the manner complained of is not authorized by the copyright owner, its agent, or the law.(ii) I swear under penalty of perjury, that the information in this notification is accurate and I am the copyright owner or am authorized to act on behalf of the owner of an exclusive right that is allegedly infringed.(iii) I accept that my private data will only be used by you in the context of its copyright notification process which include sharing a copy of this claim with the user(s) who uploaded the allegedly infringing material.(iv) I recognize that I may be liable for damages if I knowingly materially misrepresent that the material or activity infringes on my copyright. If you require anything more to process as soon as possible this request do not hesitate to respond to npitsiladis@megatv.com'+'\n Nikos Pitsiladis Digital Manager \nSyggrou Ave 35, 17565, Athens-GREECE\nThank you'
    
    part1 = MIMEText(html, 'html')
    msgRoot.attach(part1)
    smtp.sendmail("npitsiladis@megatv.com", "dmca@streamtape.com", msgRoot.as_string())
    print ('streamtape reported ')


if len (streamzz_list) > 0:


    sent_from = gmail_user
    to = ['aman.razain@streamzz.to']
    subject = 'DMCA Notice_request for immediate removal of content'
    body = 'URGENT DMCA Notice.ACE and MPA will be contacted. Dear Sir/Madam, some new links have been found on your website. MEGA TV, a national TV broadcaster and producer from Greece, is the sole owner of the copyrighted material found on your website and has never granted any license to the uploader. Thus, we demand immediate removal of this content:\n'+"\n".join(streamzz_list)+'\nI state that upon a good faith belief the disputed use of the material or activity is not authorized by the copyright or intellectual property owner, its agent or the law and under penalty of perjury, MEGA TV is the copyright or intellectual property owner or is authorized to act on behalf of the copyright or intellectual property owner and that the information provided in the notice is accurate.'+'\n Nikos Pitsiladis Digital Manager \nSyggrou Ave 35, 17565, Athens-GREECE\nThank you'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!streamzz reported')
    except:
        print ('Something went wrong with gmail')

  

if len (voe_list) > 0:


    smtp = smtplib.SMTP()
    smtp.connect('localhost')
    msgRoot = MIMEMultipart("alternative")
    msgRoot['Subject'] = Header("DMCA Notice_request for immediate removal of content", "utf-8")
    msgRoot['From'] = "npitsiladis@megatv.com"
    msgRoot['To']  =  "abuse@voe.sx"
    
    html ='Dear Sir/Madam, some new links have been found on your website. MEGA TV, a national TV broadcaster and producer from Greece, is the sole owner of the copyrighted material found on your website and has never granted any license to the uploader. Thus, we demand immediate removal of this content:\n'+"\n".join(voe_list)+'\nI state that upon a good faith belief the disputed use of the material or activity is not authorized by the copyright or intellectual property owner, its agent or the law and under penalty of perjury, MEGA TV is the copyright or intellectual property owner or is authorized to act on behalf of the copyright or intellectual property owner and that the information provided in the notice is accurate.'+'\n Nikos Pitsiladis Digital Manager \nSyggrou Ave 35, 17565, Athens-GREECE\nThank you'

    part1 = MIMEText(html, 'html')
    msgRoot.attach(part1)
    smtp.sendmail("npitsiladis@megatv.com","abuse@voe.sx", msgRoot.as_string())
    print ('voe reported ')


    

if len (streamruby_list) > 0:
   
    smtp = smtplib.SMTP()
    smtp.connect('localhost')
    msgRoot = MIMEMultipart("alternative")
    msgRoot['Subject'] = Header("DMCA Notice_request for immediate removal of content", "utf-8")
    msgRoot['From'] = "npitsiladis@megatv.com"
    msgRoot['To']  =  "abuse@streamruby.com"
    
    html ='Dear Sir/Madam, some new links have been found on your site . MEGA TV, a national TV broadcaster and producer from Greece, is the sole owner of the copyrighted material found on this website and has never granted any license to the uploader. Thus, we demand immediate removal of this content:\n'+"\n".join(streamruby_list)+'\nI state that upon a good faith belief the disputed use of the material or activity is not authorized by the copyright or intellectual property owner, its agent or the law and under penalty of perjury, MEGA TV is the copyright or intellectual property owner or is authorized to act on behalf of the copyright or intellectual property owner and that the information provided in the notice is accurate.'+'\n Nikos Pitsiladis Digital Manager \nSyggrou Ave 35, 17565, Athens-GREECE\nThank you'

    part1 = MIMEText(html, 'html')
    msgRoot.attach(part1)
    smtp.sendmail("npitsiladis@megatv.com","abuse@streamruby.com", msgRoot.as_string())
    print ('streamruby reported ')


if len (filelions_list) > 0:
   
    smtp = smtplib.SMTP()
    smtp.connect('localhost')
    msgRoot = MIMEMultipart("alternative")
    msgRoot['Subject'] = Header("DMCA Notice_request for immediate removal of content", "utf-8")
    msgRoot['From'] = "npitsiladis@megatv.com"
    msgRoot['To']  =  "abuse@ipconnect.services"
    
    html ='Dear Sir/Madam, some new links have been found on filelions.to to which you provide hosting services according to information we have received from Cloudflare . MEGA TV, a national TV broadcaster and producer from Greece, is the sole owner of the copyrighted material found on this website and has never granted any license to the uploader. Thus, we demand immediate removal of this content:\n'+"\n".join(filelions_list)+'\nI state that upon a good faith belief the disputed use of the material or activity is not authorized by the copyright or intellectual property owner, its agent or the law and under penalty of perjury, MEGA TV is the copyright or intellectual property owner or is authorized to act on behalf of the copyright or intellectual property owner and that the information provided in the notice is accurate.'+'\n Nikos Pitsiladis Digital Manager \nSyggrou Ave 35, 17565, Athens-GREECE\nThank you'

    part1 = MIMEText(html, 'html')
    msgRoot.attach(part1)
    smtp.sendmail("npitsiladis@megatv.com","abuse@ipconnect.services", msgRoot.as_string())
    print ('filelions reported ')



if len (dropload_list) > 0:
   
    smtp = smtplib.SMTP()
    smtp.connect('localhost')
    msgRoot = MIMEMultipart("alternative")
    msgRoot['Subject'] = Header("DMCA Notice_request for immediate removal of content", "utf-8")
    msgRoot['From'] = "npitsiladis@megatv.com"
    msgRoot['To']  =  "abuse@dropload.io"
    
    html ='Dear Sir/Madam, some new links have been found on filelions.to to which you provide hosting services according to information we have received from Cloudflare . MEGA TV, a national TV broadcaster and producer from Greece, is the sole owner of the copyrighted material found on this website and has never granted any license to the uploader. Thus, we demand immediate removal of this content:\n'+"\n".join(dropload_list)+'\nI state that upon a good faith belief the disputed use of the material or activity is not authorized by the copyright or intellectual property owner, its agent or the law and under penalty of perjury, MEGA TV is the copyright or intellectual property owner or is authorized to act on behalf of the copyright or intellectual property owner and that the information provided in the notice is accurate.'+'\n Nikos Pitsiladis Digital Manager \nSyggrou Ave 35, 17565, Athens-GREECE\nThank you'

    part1 = MIMEText(html, 'html')
    msgRoot.attach(part1)
    smtp.sendmail("npitsiladis@megatv.com","abuse@dropload.io", msgRoot.as_string())
    print ('dropload reported ')





if len (dm_list) > 0:
   

    smtp = smtplib.SMTP()
    smtp.connect('localhost')
    msgRoot = MIMEMultipart("alternative")
    msgRoot['Subject'] = Header("DMCA Notice_request for immediate removal of content", "utf-8")
    msgRoot['From'] = "npitsiladis@megatv.com"
    msgRoot['To']  =  "feedback@dailymotion.com"
    
    html ='Dear Sir/Madam, some new links of our series "Siopilos Dromos" have been found on your website. MEGA TV, a national TV broadcaster and producer from Greece, is the sole owner of the copyrighted material found on your website and has never granted any license to the uploader. The whole uploaded video (100%) is infringing as it is a whole episode.Thus, we demand immediate removal of this content:\n'+"\n"','.join([str(i) for i in dm_list])+'\n I state that upon a good faith belief the disputed use of the material or activity is not authorized by the copyright or intellectual property owner, its agent or the law and under penalty of perjury, MEGA TV is the copyright or intellectual property owner or is authorized to act on behalf of the copyright or intellectual property owner and that the information provided in the notice is accurate.Also (i) I have good faith belief that use of the material in the manner complained of is not authorized by the copyright owner, its agent, or the law.(ii) I swear under penalty of perjury, that the information in this notification is accurate and I am the copyright owner or am authorized to act on behalf of the owner of an exclusive right that is allegedly infringed.(iii) I accept that my private data will only be used by Dailymotion in the context of its copyright notification process which include sharing a copy of this claim with the user(s) who uploaded the allegedly infringing material.(iv) I recognize that I may be liable for damages if I knowingly materially misrepresent that the material or activity infringes on my copyright.'+'\n Nikos Pitsiladis Digital Manager \nSyggrou Ave 35, 17565, Athens-GREECE\nThank you'

    part1 = MIMEText(html, 'html')
    msgRoot.attach(part1)
    smtp.sendmail("npitsiladis@megatv.com","feedback@dailymotion.com", msgRoot.as_string())


    print('reported dm')

     



driver.quit()

print('endofstory')

driver.quit()
driver.quit()
driver.quit()
driver.quit()
driver.quit()
driver.quit()


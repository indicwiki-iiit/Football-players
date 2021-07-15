# -*- coding: utf-8 -*-
"""
Created on Mon May 31 12:25:50 2021

@author: nallu
"""


from selenium import webdriver
import pandas as pd
import math as m
import time
#import numpy as np
#path of chromedriver.exe
PATH=r"C:\Users\nallu\Dropbox\My PC (LAPTOP-1C2T7QTM)\Downloads\chromedriver.exe"
driver=webdriver.Chrome(PATH)
def read_extra_stats(stats_url):
    #//*[@id="yw2"]/table/tbody/tr[1]/td[2]
    driver.get(stats_url)
    time.sleep(5)
    s='//*[@id="yw2"]/table/tbody/tr[1]/td[3]'
    rows=len(driver.find_elements_by_xpath('//*[@id="yw2"]/table/tbody/tr'))
    cols=len(driver.find_elements_by_xpath('//*[@id="yw2"]/table/tbody/tr[1]/td'))
    tab=[]
    for r in  range(1,min(rows+1,10)):
        col=[]
        for c in range(2,cols+1):
            s=s[:30]+str(r)+s[31:36]+str(c)+']'
            try:
                value = driver.find_element_by_xpath(s).text
            except:
                continue
            col.append(value)
        tab.append(col)
    s1='//*[@id="main"]/div[11]/div[2]/div[4]/table/tbody/tr[1]/td[2]'
    rows1=len(driver.find_elements_by_xpath('//*[@id="main"]/div[11]/div[2]/div[4]/table/tbody/tr'))
    cols1=len(driver.find_elements_by_xpath('//*[@id="main"]/div[11]/div[2]/div[4]/table/tbody/tr[1]/td'))
    tab1=[]
    for r in  range(1,min(rows1+1,10)):
        col1=[]
        for c in range(2,cols1+1):
            s1=s1[:53]+str(r)+s1[54:59]+str(c)+']'
            try:
                value = driver.find_element_by_xpath(s1).text
            except:
                continue
            col1.append(value)
        tab1.append(col1)
    #print('tab1',tab1)
    return tab,tab1
   
def main():
    plyrs=pd.read_csv(r'C:\Users\nallu\Dropbox\My PC (LAPTOP-1C2T7QTM)\Downloads\players.csv')
    ids=plyrs['player_id'].values
    urls=plyrs['url'].values
    names=plyrs['name'].values
    row=[]
    rows=[]
    for i in range(1):
        url=urls[i]
        driver.get(url)
	time.sleep(3)
	try:
        	youthclubs=driver.find_element_by_xpath('//*[@id="main"]/div[11]/div[1]/div[5]/div[2]').text
        	youth_clubs=[club for club in list(youthclubs.split(','))]
	except:
		youth_clubs=''
        stats='https://www.transfermarkt.co.uk/'+str(names[i])+'/leistungsdaten/spieler/'+str(ids[i])+"/plus/0?saison=ges"
        career_stats,stats_byclub=read_extra_stats(stats)
        #print(stats_extra)
        row=[ids[i],career_stats,stats_byclub,youth_clubs]
        rows.append(row)
    df=pd.DataFrame(rows,columns=['player_id','career_stats','stats_by-club','youth_clubs'])
    df.to_csv("extra_stats.csv", index=False)
    driver.close()
        
        
if __name__=='__main__':
    main()
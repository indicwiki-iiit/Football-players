# -*- coding: utf-8 -*-
"""
Created on Tue May 25 15:06:36 2021

@author: nallu
"""
from selenium import webdriver
import pandas as pd
import math as m
#import numpy as np
PATH=r"C:\Users\nallu\Dropbox\My PC (LAPTOP-1C2T7QTM)\Downloads\chromedriver.exe"
driver=webdriver.Chrome(PATH)
s2='//*[@id="main"]/div[11]/div[2]/div[2]/table/tbody/tr[2]/td[3]'
def read_stats(stats_url):
    driver.get(stats_url)
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
    return tab
def read_national_career(s):
    rows=len(driver.find_elements_by_xpath('//*[@id="main"]/div[11]/div[2]/div[3]/table/tbody/tr'))
    cols=len(driver.find_elements_by_xpath('//*[@id="main"]/div[11]/div[2]/div[3]/table/tbody/tr[1]/td'))
    tab=[]
    for r in  range(1,min(rows+1,5)):
        col=[]
        for c in range(3,cols+1):
            s=s[:53]+str(r)+s[54:59]+str(c)+']'
            try:
                value = driver.find_element_by_xpath(s).text
            except:
                continue
            col.append(value)
        tab.append(col)
    return tab
def read_debus(debu):
    s='//*[@id="main"]/div[11]/div[1]/div/div[2]/table/tbody/tr[3]/td[4]'
   # //*[@id="main"]/div[11]/div[1]/div/div[2]/table/tbody/tr[6]/td[2]/a
    driver.get(debu)
    rows=len(driver.find_elements_by_xpath('//*[@id="main"]/div[11]/div[1]/div/div[2]/table/tbody/tr'))
    #cols=len(driver.find_elements_by_xpath('//*[@id="main"]/div[11]/div[1]/div/div[2]/table/tbody/tr[2]/td'))
    tab=[]
    for r in range(2,min(rows+1,10)):
        col=[]
        for c in [2,4,6,7]:
            s=s[:57]+str(r)+s[58:63]+str(c)+']'
            try:
                value = driver.find_element_by_xpath(s).text
            except:
                continue
            col.append(value)
        if(len(col)>0):
            tab.append(col)
    return tab
            
    
def main():
    plyrs=pd.read_csv(r'C:\Users\nallu\Dropbox\My PC (LAPTOP-1C2T7QTM)\Downloads\players.csv')
    ids=plyrs['player_id'].values
    urls=plyrs['url'].values
    names=plyrs['name'].values
    row=[]
    rows=[]
    for i in range(0,2000):
        url=urls[i]
        driver.get(url)
        #Extracting birth_place attribute
        try:
            birth_place=driver.find_element_by_xpath('//*[@id="main"]/div[11]/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td/span').text
        except:
            try:
                birth_place=driver.find_element_by_xpath('//*[@id="main"]/div[11]/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td/span').text
            except:
                print('no dbp')
                birth_place=''
        #Extracting agent attribute
        try:
            agent=driver.find_element_by_xpath('//*[@id="main"]/div[11]/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[9]/td').text
        except:
            try:
                agent=driver.find_element_by_xpath('//*[@id="main"]/div[11]/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[9]/td').text
            except:
                print('no agent')
                agent=''
        #Extracting highest_market_value attribute
        try:
            hst_val=driver.find_element_by_xpath('//*[@id="main"]/div[11]/div[1]/div[2]/div[2]/div[1]/div/div[3]/div[2]/div/div/div/div[1]/div[1]/div/div[3]/div[2]').text
        #Extracting full_name
        except:
            print('no hst')
            hst_val=''
        try:
            full_name=driver.find_element_by_xpath('//*[@id="main"]/div[11]/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td').text
        except:
            print('no fn')
            full_name=''
        s='//*[@id="main"]/div[11]/div[2]/div[3]/table/tbody/tr[2]/td[3]'
        nat_car=read_national_career(s)
        #Adding ids
        debu='https://www.transfermarkt.co.uk/'+str(names[i])+'/debuets/spieler/'+str(ids[i])
        stats='https://www.transfermarkt.co.uk/'+str(names[i])+'/leistungsdaten/spieler/'+str(ids[i])
        debus=read_debus(debu)
        stats=read_stats(stats)
        row=[ids[i],birth_place,agent,hst_val,full_name,nat_car,debus,stats]
        rows.append(row)
    df=pd.DataFrame(rows,columns=['player_id','birth_place','agent','highest_market_value','full_name','national_career','debuts','stats'])
    df.to_csv("sample_attrs.csv", index=False)
    new_attrs=pd.read_csv("sample_attrs.csv")
    final_csv=pd.merge(plyrs,new_attrs,on='player_id',how='inner')
    final_csv.to_csv("final.csv", index=False)
    driver.close()
if __name__=='__main__':
    main()
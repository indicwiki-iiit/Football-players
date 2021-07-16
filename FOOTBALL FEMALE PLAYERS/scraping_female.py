# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:06:55 2021

@author: nallu
"""

#position=driver.find_element_by_xpath('').text
from selenium import webdriver
import pandas as pd
import math as m
import time
#import numpy as np
#path of chromedriver.exe
PATH=r"C:\Users\nallu\Dropbox\My PC (LAPTOP-1C2T7QTM)\Downloads\chromedriver.exe"
driver=webdriver.Chrome(PATH)
def read_stats(url):
    s='/html/body/main/div/div/div[2]/div[4]/div[6]/div/div/p[1]/span/span'
    col,cols=[],[]
    for i in range(1,8):
        col=[]
        if i==1:
            r=2
        elif i==2 or i==4:
            r=3
        elif i==3:
            r=6
        elif i==5:
            r=7
        elif i==6:
            r=8
        elif i==7:
            r=5
        for j in range(1,r+1):
            s1='/html/body/main/div/div/div[2]/div[4]/div['+str(i)+']/div/div/p['+str(j)+']/span/span'
            ele=driver.find_element_by_xpath(s1).text
            col.append(ele)
        cols.append(col)
    return cols
            
def main():
    fplyrs=pd.read_csv(r'C:\Users\nallu\Dropbox\My PC (LAPTOP-1C2T7QTM)\Downloads\female_links.csv')
    urls=fplyrs['links']
    rows=[]
    for i in range(len(urls)):
        url=urls[i]
        driver.get(url)
        time.sleep(5)
        name=driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/h1').text
        nation=driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/h2/a[2]').text
        height=driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div[2]/div[2]/div/div/p[1]/span/span[1]').text
        weight=driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div[2]/div[2]/div/div/p[2]/span/span[1]').text
        foot=driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div[2]/div[2]/div/div/p[3]/span').text
        dob=driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div[2]/div[2]/div/div/p[4]/span').text
        age=driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div[2]/div[2]/div/div/p[5]/span').text
        pos=driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div[2]/div[2]/div/div/p[6]').text
        work_rate=driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div[2]/div[2]/div/div/p[7]/span').text
        position=driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div[3]/div/div/div/p[1]/span/a/span').text
        kit_no=driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div[3]/div/div/div/p[2]/span').text
        stats=read_stats(url)
        ball_skills=stats[0]
        defence=stats[1]
        mental=stats[2]
        passing=stats[3]
        physical=stats[4]
        shooting=stats[5]
        goalkeeper=stats[6]
        row=[name,nation,height,weight,foot,dob,age,pos,work_rate,position,kit_no,ball_skills,defence,mental,passing,physical,shooting,goalkeeper]
        rows.append(row)
        print("player",i,"scraped successfully")
    df=pd.DataFrame(rows,columns=['Name','Nation','Height','Weight','Pref-Foot','Dob','age','positions','work_rate','position','kit_no','ball_skills','defence','mental','passing','physical','shooting','goalkeeper'])
    df.to_csv("female_plyrs_data.csv",index=False)
    driver.close()
if __name__=='__main__':
    main()
        
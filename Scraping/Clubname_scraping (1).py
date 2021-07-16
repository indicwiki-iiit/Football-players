# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:24:38 2021

@author: nallu
"""


from selenium import webdriver
import pandas as pd
import time
#import numpy as np
#path of chromedriver.exe
PATH=r"C:\Users\nallu\Dropbox\My PC (LAPTOP-1C2T7QTM)\Downloads\chromedriver.exe"
driver=webdriver.Chrome(PATH)
def main():
    #players.csv file path
    plyrs=pd.read_csv(r'C:\Users\nallu\Dropbox\My PC (LAPTOP-1C2T7QTM)\Downloads\players.csv')
    ids=plyrs['player_id'].values
    urls=plyrs['url'].values
    names=plyrs['name'].values
    clubids=plyrs['club_id'].values
    row=[]
    rows=[]
    n_rows=plyrs.shape[0]
    expire=''
    for i in range(3300,3500):
        url=urls[i]
        driver.get(url)
        time.sleep(1)
        cc='Current club:'
        #//*[@id="main"]/div[11]/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[10]/th
        #//*[@id="main"]/div[11]/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[10]/th
        #//*[@id="main"]/div[11]/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[10]/td
        try:
            r10=driver.find_element_by_xpath('//*[@id="main"]/div[11]/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[10]/th').text
            r9=driver.find_element_by_xpath('//*[@id="main"]/div[11]/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[9]/th').text
            r8=driver.find_element_by_xpath('//*[@id="main"]/div[11]/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[8]/th').text
            r7=driver.find_element_by_xpath('//*[@id="main"]/div[11]/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[7]/th').text
            if(r10==cc):
                club_name=driver.find_element_by_xpath('//*[@id="main"]/div[11]/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[10]/td').text
            elif(r9==cc):
                club_name=driver.find_element_by_xpath('//*[@id="main"]/div[11]/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[9]/td').text
            elif(r8==cc):
                club_name=driver.find_element_by_xpath('//*[@id="main"]/div[11]/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[8]/td').text
            elif(r7==cc):
                club_name=driver.find_element_by_xpath('//*[@id="main"]/div[11]/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[7]/td').text
            else:
                club_name=''
        except:
            club_name=''
        row=[ids[i],club_name]
        rows.append(row)
    df=pd.DataFrame(rows,columns=['player_id','club_name'])
    df.to_csv('Clubname.csv',index=False)
    driver.close()
if __name__=='__main__':
    main()
            

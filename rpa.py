from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
Service = Service()
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service,options=options)

# Entrando no site
browser.get('https://www.youtube.com/')

music = ['ACDC','Guns and Roses','Queen','Cure','Beatles']
sleep(4)
#Indo na parte de busca, pesquisando e tirando o print
for i in music:
    browser.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/div/div[2]/input').send_keys(i)
    browser.find_element(By.ID,'search-icon-legacy').click()
    sleep(2)    
    browser.save_screenshot(f'{i}.png')
    browser.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/div/div[2]/input').clear()
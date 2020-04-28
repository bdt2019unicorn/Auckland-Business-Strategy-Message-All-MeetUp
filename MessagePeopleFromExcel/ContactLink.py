import time 
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint

driver = webdriver.Chrome("chromedriver")

def WaitForLogin(): 
    try: 
        login_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginFormSubmit"]')))
        login_button.click()
    except Exception as e: 
        print(e)
        WaitForLogin()

def LoginMeetUp(): 
    
    driver.get("https://secure.meetup.com/login/")

    email_ID = driver.find_element_by_xpath('//*[@id="email"]')
    email_ID.send_keys("hanhfucnhonhoi@gmail.com")

    password_box = driver.find_element_by_xpath('//*[@id="password"]')
    password_box.send_keys("binhdeptrai")

    WaitForLogin()

    

def ColdMessage(): 
    file_name = "meetup cold message.txt"
    text_file = open(file_name,"r")
    message = text_file.read()
    text_file.close()
    return message

def WaitForPutTextIn(): 
    try:
        message = ColdMessage()
        message_box = driver.find_element_by_xpath('//*[@id="messaging-new-convo"]')
        message_box.send_keys(message)
    except Exception as exception: 
        WaitForPutTextIn()

def MessagePeople(link): 
    print(link)
    driver.get(link)
    WaitForPutTextIn()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="messaging-new-send"]').click()
    time.sleep(7)





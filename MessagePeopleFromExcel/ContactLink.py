from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    print(message)

def WaitForPutTextIn(): 
    try:
        message = """
        """
        message_box = driver.find_element_by_xpath('//*[@id="messaging-new-convo"]')
    except: 
        WaitForPutTextIn()

def MessagePeople(link): 
    driver.get(link)
    print(link)





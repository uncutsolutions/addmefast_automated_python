from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.common.exceptions import ElementNotInteractableException

with open("login_details.txt", "r") as file:
    addmefastemail = file.readline().strip()
    addmefastpassword = file.readline().strip()
    chromedir = file.readline().strip()



options = webdriver.ChromeOptions()
options.add_argument(chromedir)

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://uncutsolutions.com")
driver.implicitly_wait(10)
driver.get("https://addmefast.com/")
email_input = driver.find_element(by='xpath', value='/html/body/div[1]/section[2]/div/div[4]/form/div[1]/div[1]/input[1]')
password_input = driver.find_element(by="name", value="password")
driver.execute_script(f"arguments[0].value = '{addmefastemail}';", email_input)
driver.execute_script(f"arguments[0].value = '{addmefastpassword}';", password_input)
login_button = driver.find_element(by="name", value="login_button")
login_button.click()

driver.implicitly_wait(10)

driver.get("https://addmefast.com/free_points/youtube_subscribe")


try:
    while True:
 
        try:
            wait = WebDriverWait(driver, 10)
            subscribe_button1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn3')))
            subscribe_button1.click()
            driver.implicitly_wait(10)
        except:
            driver.get("https://addmefast.com/free_points/youtube_subscribe")
            wait = WebDriverWait(driver, 10)
            subscribe_button1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn3')))
            subscribe_button1.click()
            driver.implicitly_wait(10)

        sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        sleep(2)

        driver.maximize_window()
        sleep(2)
        wait = WebDriverWait(driver, 10)
        try:
            subscribe_button = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                          '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')))

            subscribe_button.click()
            sleep(3)
            driver.close()

        except:
            try:
                subscribe_button = wait.until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/tp-yt-paper-button/yt-formatted-string')))
                subscribe_button.click()
                sleep(3)
                driver.close()
            except:
                driver.close()

        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        driver.implicitly_wait(10)
except:
    driver.get("https://addmefast.com/free_points/youtube_subscribe")

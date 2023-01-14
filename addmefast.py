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
# Set up the webdriver
driver = webdriver.Chrome(chrome_options=options)

driver.get("https://uncutsolutions.com")

# Wait for the page to load
driver.implicitly_wait(10)


# Navigate to the login page
driver.get("https://addmefast.com/")

# Find the email and password input elements
email_input = driver.find_element(by='xpath', value='/html/body/div[1]/section[2]/div/div[4]/form/div[1]/div[1]/input[1]')
password_input = driver.find_element(by="name", value="password")

# Enter the email and password values using execute_script
driver.execute_script(f"arguments[0].value = '{addmefastemail}';", email_input)
driver.execute_script(f"arguments[0].value = '{addmefastpassword}';", password_input)

# Find the login button and click it
login_button = driver.find_element(by="name", value="login_button")
login_button.click()

# Wait for the login to complete (you may need to modify this if the login process takes longer)
driver.implicitly_wait(10)

# Now you should be logged in!

# Navigate to the earn points page for YouTube subscriptions
driver.get("https://addmefast.com/free_points/youtube_subscribe")


try:
    while True:
        # Wait for the subscribe button to be clickable
        try:
            wait = WebDriverWait(driver, 10)
            subscribe_button1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn3')))

            # Click the subscribe button
            subscribe_button1.click()
            # Wait for the subscribe popup to appear
            driver.implicitly_wait(10)
        except:
            driver.get("https://addmefast.com/free_points/youtube_subscribe")
            wait = WebDriverWait(driver, 10)
            subscribe_button1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn3')))

            # Click the subscribe button
            subscribe_button1.click()
            # Wait for the subscribe popup to appear
            driver.implicitly_wait(10)

        sleep(2)
        # Switch to the subscribe popup
        driver.switch_to.window(driver.window_handles[1])
        sleep(2)

        driver.maximize_window()
        sleep(2)
        # Click the subscribe button in the popup
        wait = WebDriverWait(driver, 10)

        # Check if the subscribe button exists
        # Check if the subscribe button exists
        try:
            subscribe_button = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                          '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')))
            # Subscribe button found, click it
            subscribe_button.click()
            sleep(3)
            driver.close()

        except:
            try:
                subscribe_button = wait.until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/tp-yt-paper-button/yt-formatted-string')))
                # Subscribe button found, click it
                subscribe_button.click()
                sleep(3)
                driver.close()
            except:
                driver.close()

        # Wait for the action to complete
        sleep(2)
        # Switch back to the main window
        driver.switch_to.window(driver.window_handles[0])
        driver.implicitly_wait(10)
except:
        # Handle the exception here (e.g. log a message, close the popup, etc.)
    driver.get("https://addmefast.com/free_points/youtube_subscribe")

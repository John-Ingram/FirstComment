from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait




youtuber = "https://www.youtube.com/user/havefun123for/videos"
oldVidUrl = "BVedu0aBNxE"

#Log in to Google Account

driver = webdriver.Firefox()

driver.get("https://accounts.google.com/signin")
email_phone = driver.find_element_by_xpath("//input[@id='identifierId']")
email_phone.send_keys("ministryofkek")
driver.find_element_by_id("identifierNext").click()
password = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))
)
password.send_keys("4chanpepe")
driver.find_element_by_id("passwordNext").click()


#Open YT page
driver.get(youtuber)
driver.find_element_by_id("video-title").click()
#Set up base page info


while True:

    driver.get(youtuber)
    
    
    timeout = 2
    try:
        element_present = EC.presence_of_element_located((By.ID, 'tabsContainer'))
        WebDriverWait(driver, timeout).until(element_present)
        driver.find_element_by_id("video-title").click()
    except TimeoutException:
        print("Timed out waiting videos to load. Retrying...")
    finally:
        print("Page loaded")
        timeout = 1
        try:
            element_present = EC.presence_of_element_located((By.ID, 'tabsContainer'))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting to find date")
            continue
        finally:
            if oldVidUrl not in driver.current_url: break


print("Success!")



from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.youtube.com/user/MrBeast6000/videos")
elem = driver.find_element_by_id("video-title")
elem.send_keys(Keys.RETURN)

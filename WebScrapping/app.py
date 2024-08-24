from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.parse
import undetected_chromedriver as uc








def convert_to_utf8_encoded(input_string):
    encoded_string = urllib.parse.quote(input_string, safe='')
    return encoded_string


input_string = 'c++'
encoded_string = convert_to_utf8_encoded(input_string)



# driver = webdriver.Chrome(options=chrome_options)
driver = uc.Chrome()


# driver.get(f"https://www.udemy.com/courses/search/?src=ukw&q={encoded_string}")
driver.get(f"https://www.udemy.com/")


# assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys(input_string)
elem.send_keys(Keys.RETURN)

time.sleep(5)

# elem = driver.find_element(By.XPATH, '//*[@id="PYMIw2"]/div/label/input')
elem = driver.find_element(By.CLASS_NAME, 'course-card-module--container--3oS-F')

print(elem.get_attribute('innerHTML'))
# assert "No results found." not in driver.page_source


time.sleep(30)
# driver.close()

# //*[@id="u57-popper-trigger--1033"]

# //*[@id="u57-popper-trigger--1036"]
# //*[@id="u57-popper-trigger--1039"]
# //*[@id="u57-popper-trigger--1039"]course-card-module--container--3oS-F
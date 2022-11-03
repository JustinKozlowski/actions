from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    driver.get('https://autograder.cse.buffalo.edu/auth/users/sign_in')
    print("Current Page: " + driver.title)
    elem = driver.find_element(By.TAG_NAME, 'input')  # Find the search box
    elem.click()
    print("Current Page: " + driver.title)
    elem = driver.find_element(By.NAME, 'j_username')
    elem.send_keys(os.environ['UBIT_USERNAME'])
    elem = driver.find_element(By.NAME, 'j_password')
    elem.send_keys(os.environ['UBIT_PASSWORD'] + Keys.RETURN)
    print("Current Page: " + driver.title)
    sleep(1)
    print("Current Page: " + driver.title)
    driver.quit()

if __name__ == "__main__":
    main()
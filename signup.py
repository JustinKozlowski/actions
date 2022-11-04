from time import sleep
import os
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from commitparser.parse_commit import parse_commit


def main():
    # Initialize chrom drive
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

    # navigate to autolab
    driver.get('https://autograder.cse.buffalo.edu/auth/users/sign_in')

    # Log In
    driver.find_element(By.TAG_NAME, 'input').click()
    driver.find_element(By.NAME, 'j_username').send_keys(os.environ['UBIT_USERNAME'])
    driver.find_element(By.NAME, 'j_password').send_keys(os.environ['UBIT_PASSWORD'] + Keys.RETURN)

    # Wait for duo

    # Navigate to submission page, wait for duo
    x = 0
    while (driver.title != 'Autolab Home') and (x < 15):
        sleep(1)
        x += 1
    if x == 15:
        print('Error in Duo authentication')
        return
    driver.get('https://autograder.cse.buffalo.edu/courses/UBHacking-f22/course_user_data/new')
    driver.find_element(By.ID, 'course_user_datum_user_attributes_email').send_keys("jjkozlow@buffalo.edu")
    driver.find_element(By.ID, 'user_submit').click()
    sleep(100)
    driver.quit()


if __name__ == "__main__":
    main()
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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
    while driver.title != 'Autolab Home' or x < 15:
        sleep(1)
        x += 1
    if x == 15:
        print('Error in Duo authentication')
        return
    driver.find_element(By.XPATH, "//a[text()='UB Hacking Submissions']").click()
    
    # Authorize AI
    driver.find_element(By.XPATH, "//form[@id='new_submission']/label").click()
    # Submit file
    driver.find_element(By.ID, 'submission_file').send_keys('C:/Users/JustinKozlowski/Documents/UB/Archive/Senior/Fall 2020/CSE 442/Activity5 - Cse442.pdf')
    print('Successfuly Submitted')
    driver.quit()

if __name__ == "__main__":
    main()
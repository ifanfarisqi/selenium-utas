from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# driver.maximize_window()


try:

    # Dashboard page login
    driver.get('https://member.utas.co/')

    # Input field not registered in system and error
    driver.find_element(By.ID, 'username').send_keys('percobaan')
    driver.find_element(By.ID, 'password').send_keys('dwq')
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/div[4]/button').click()
    # driver.find_element(By.XPATH, '/html/body/div[4]/div[7]/div/button').click()
    trigger_button = driver.find_element(By.ID, '/html/body/div[4]/div[7]/div/button')  # Adjust the locator
    trigger_button.click()
    alert = driver.switch_to.alert
    alert.accept()

    # Input field success
    # driver.find_element(By.ID, 'username').send_keys('percobaan')
    # driver.find_element(By.ID, 'password').send_keys('percobaan4321')
    # driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/div[3]/div[1]/div/label').click()
    # driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/div[4]/button').click()
    # driver.find_element(By.XPATH, '/html/body/div[4]/div[7]/div/button').click()

finally:
    time.sleep(5)
    driver.quit()
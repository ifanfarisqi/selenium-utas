from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

try:

    # Open Page Resgiter
    driver.get('https://member.utas.co/registration/starter')

    # Register Same Account and Test Error Field
    # driver.find_element(By.ID, 'username').send_keys('akunpercobaan')
    # driver.find_element(By.ID, 'email').send_keys('akunpercobaan@coba.com') 
    # driver.find_element(By.ID, 'password').send_keys('123456')
    # driver.find_element(By.ID, 'whatsapp_number').send_keys('0821637623')
    # driver.find_element(By.XPATH, '//*[@id="is-register-form"]/div/form/div[5]').click()
    # driver.find_element(By.ID, 'go-select-product').click()
    # driver.find_element(By.XPATH, '//*[@id="product_id"]/div/label/div').click()
    # driver.find_element(By.ID, 'register').click()

    # Register Success
    driver.find_element(By.ID, 'username').send_keys('percobaan')
    driver.find_element(By.ID, 'email').send_keys('percobaan@percobaan.com') 
    driver.find_element(By.ID, 'password').send_keys('percobaan4321')
    driver.find_element(By.ID, 'whatsapp_number').send_keys('08213267523')
    driver.find_element(By.XPATH, '//*[@id="is-register-form"]/div/form/div[5]').click()
    driver.find_element(By.ID, 'go-select-product').click()
    driver.find_element(By.XPATH, '//*[@id="product_id"]/div/label/div').click()
    driver.find_element(By.ID, 'register').click()
    driver.find_element(By.XPATH, '/html/body/div[5]/div[7]/div/button').click()

finally:
    time.sleep(5)
    driver.quit()
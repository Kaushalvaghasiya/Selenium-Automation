import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def new_acc(firstName, lastName):
    driver = webdriver.Chrome()

    driver.get("https://accounts.google.com/v3/signin/identifier?flowEntry=ServiceLogin&flowName=GlifWebSignIn&hl=en-GB&ifkv=ARZ0qKKQwWQKqD3xynlgTzM-fC4E0J25AeyL8_1a3iCQFCb90OvLx-rmYg_uKJDFJ4voDlUcN_1wBw&dsh=S-2012872008%3A1711085819833086&theme=mn&ddm=0")

    create_account_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Create account']")))
    create_account_button.click()

    for_personal_use_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='For my personal use']")))
    for_personal_use_option.click()

    firstname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "firstName")))
    firstname_field.send_keys(firstName)

    lastname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "lastName")))
    lastname_field.send_keys(lastName)

    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
    next_button.click()

    day_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "day")))
    day_field.send_keys("1")

    dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "month")))
    month_select = Select(dropdown)
    month_select.select_by_value("3")

    year_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "year")))
    year_field.send_keys("1999")

    dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "gender")))
    month_select = Select(dropdown)
    month_select.select_by_value("1")

    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
    next_button.click()

    own_gmail_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "selectionc4")))
    own_gmail_button.click()

    randomNo = str(random.randint(10000, 99999))
    username = firstName + lastName + randomNo
    password = firstName.capitalize() + "_" + lastName.capitalize() + "@" + randomNo

    email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "Username")))
    email_field.send_keys(username)

    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
    next_button.click()

    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "Passwd")))
    password_field.send_keys(password)

    c_password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "PasswdAgain")))
    c_password_field.send_keys(password)

    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
    next_button.click()

    time.sleep(10)
    driver.quit()

new_acc("armin", "conny")
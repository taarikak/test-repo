from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
from behave import given,when,then
import time

csv_path = 'E:/Python/BDD/features/test_data/user-pass-data.csv'

@given('I am on the login page')
def step_login_page(context):
    context.driver = webdriver.Chrome()
    # context.driver.get('https://www.saucedemo.com')

@when('I login with the "{Username}" and "{Password}"')
def step_login_username_password(context,Username,Password):
    # Read the CSV file
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            username = row['Username']
            password = row['Password']

    # Return to login page for next iteration
    context.driver.get('https://www.saucedemo.com')

    username_field = context.driver.find_element(By.NAME,'user-name')
    password_field = context.driver.find_element(By.NAME,'password')
    login_field = context.driver.find_element(By.NAME,'login-button')
    username_field.clear()
    password_field.clear()
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_field.click()

    try:
        home_title = context.driver.find_element(By.CSS_SELECTOR, '.app_logo')
        if  home_title.text == "Swag Labs":
            print(f"{username} - Login successful.")
        else:
            print(f"{username} -Login failed.")

    except Exception as e:
        print(f'{username} - login failed due to exception {str(e)}')

@then('I should see login result')
def step_login_result(context):
    time.sleep(5)
    context.driver.quit()
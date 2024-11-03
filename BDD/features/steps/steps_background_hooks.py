from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then

@given('I navigate to "{url}"')
def step_navigate(context, url):
    context.driver.get(url)

@when('I enter the username "{username}" and password "{password}"')
def step_enter_user_pass(context,username,password):
    user_field = context.driver.find_element(By.ID,"user-name").send_keys(username)
    pass_field = context.driver.find_element(By.ID,"password").send_keys(password)

@when('I click the login button')
def step_click_button(context):
    login_button = context.driver.find_element(By.ID, "login-button").click()

@then('I should be logged in successful')
def step_success(context):
    assert "inventory.html" in context.driver.current_url, "Login failed"

@then('I should see error message "{error_msg}"')
def step_error(context,error_msg):
    error_element = context.driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error_msg in error_element.text, f"Error -  {error_element.text}"


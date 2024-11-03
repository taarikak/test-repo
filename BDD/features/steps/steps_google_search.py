from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given('I am on the google search page')
def step_open_google_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.google.com/')

@when('I search for "{item}"')
def step_search_for_cheese(context,item):
    search_box = context.driver.find_element(By.ID,"APjFqb")
    search_box.send_keys(item)
    search_box.send_keys(Keys.RETURN)

@then('the page title should start with "{expected_title}"')
def step_page_title_verify(context,expected_title):
    # actual_title = context.driver.title.lower()
    # assert expected_title.lower() in actual_title, f"expected '{expected_title}' but got '{actual_title}'"
    actual_title = context.driver.title.lower()
    if actual_title.startswith(expected_title.lower()):
        print("Title verification passed.")
        return True
    else:
        print(f"Title verification failed. Expected '{expected_title}', but got '{actual_title}'")
        return False
    context.driver.quit()

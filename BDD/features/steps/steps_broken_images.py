from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

@given('I am on the broken images webpage "{url}"')
def step_given_webpage(context,url):
    context.driver = webdriver.Chrome()
    context.driver.get('https://the-internet.herokuapp.com/broken_images')

@when('I check all the images links on webpage')
def step_check_all_links(context):
    global links
    links = context.driver.find_elements(By.TAG_NAME,'img')

@then('it should validate status code for each image link')
def step_check_status_code(context):
    for link in links:
        url = link.get_attribute("src")
        response = requests.get(url)
        if response.status_code == 200:
            print(f"correct links: {url} and status code: {response.status_code}")
        else:
            print(f"broken links: {url} and status code: {response.status_code}")
    context.driver.quit()
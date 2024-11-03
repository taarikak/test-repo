from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

@given('I am on the dropdown page "{url}"')
def step_dropdown_page(context,url):
   context.driver = webdriver.Chrome()
   context.driver.get('https://the-internet.herokuapp.com/dropdown')

@when('I select the option "{option}" from dropdown')
def step_dropdown_select(context,option):
    selected_dropdown = context.driver.find_element(By.ID,'dropdown')
    dropdown = Select(selected_dropdown)
    dropdown.select_by_visible_text(option)

@then('The "{option}" should be selected successfully')
def step_option_select(context,option):
    selected_dropdown = context.driver.find_element(By.ID,'dropdown')
    dropdown = Select(selected_dropdown)
    options = dropdown.options

    for option in options:
        option_text=option.text
        print(f'all options:{option_text}')

    selected_option = dropdown.first_selected_option
    print(f'selected option {selected_option.text}')
    context.driver.quit()
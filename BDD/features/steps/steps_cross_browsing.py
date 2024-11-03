from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import platform


@given('I open the web "{browser}"')
def step_open_browser(context,browser):
    context.browser = browser  # Store the browser in context

    if browser == 'chrome':
        context.driver = webdriver.Chrome()
    elif browser == 'firefox':
        context.driver = webdriver.Firefox()
    elif browser == 'edge':
        context.driver = webdriver.Edge()  
    elif browser == 'safari':
        if platform.system() == 'Darwin': #check kernL Darwin OS for mac
            context.driver = webdriver.Safari()
        else:
            print('Safari is only supported in macOS')
            context.driver = None # Handle this case by setting the driver to None
            return
    else:
        print('browser selection error')
        context.driver = None

@when('I navigate to google page "{url}"')
def step_open_google_page(context,url):
    if context.driver: # Ensure that driver is not None
        context.driver.get(url)
    else:
        print(f'Skip  the test for  browser: {context.browser} (unsupported browser)')
        return

@when('I search for word "{search_term}"')
def step_search_term(context,search_term):
    if context.driver:
        element = context.driver.find_element(By.CSS_SELECTOR,'#APjFqb')
        element.send_keys(search_term)
        element.send_keys(Keys.RETURN)

@then('I should see the google logo with alternate title')
def check_logo_alt_title(context):
    if context.driver:
        wait = WebDriverWait(context.driver, 10)
        logo_title =  wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="hplogo" or @id="logo"]')))
        alt_logo_title = logo_title.get_attribute('title')
        if alt_logo_title:
            print(f'Alternate title : {alt_logo_title}')
        else:
            print(f'Title not found.')

        print(f'test passed on browser: {context.browser}')
        context.driver.quit()
    else:
        print(f'Test skipped for browser: {context.browser}')
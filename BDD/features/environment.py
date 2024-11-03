from selenium import webdriver

# Hooks in environment.py ensure a controlled environment, where the browser opens only once (for all tests) and closes automatically. 
# Additionally, after_scenario adds robustness by capturing screenshots on failure for debugging purposes.

def before_all(context):
    print("Global setup")
    context.driver = webdriver.Chrome()

def before_feature(context,feature):
    print(f"Starting feature - {feature.name}")

def before_scenario(context,scenario):
    print(f"Start of scenario - {scenario.name}")
    context.driver.implicitly_wait(10)

def after_scenario(context, scenario):
    if scenario.status == "failed":
        context.driver.save_screenshot(f"reports/{scenario.name}.png")

def after_feature(context,feature):
    print(f"Completed feature - {feature.name}")

def after_all(context):
    print("Cleanup")
    context.driver.quit()

# before_all: Sets up the browser at the start of the test suite.
# after_scenario: Captures a screenshot if a scenario fails and saves it in the reports folder.
# after_all: Closes the browser after all tests are complete.

# environment.py typically includes hook functions that Behave recognizes and runs at specific times:
# before_all(context): Executes before any feature runs. Use it for global setup, like initializing WebDriver.
# before_feature(context, feature): Runs before each feature file. Useful for setup specific to certain features.
# before_scenario(context, scenario): Executes before each scenario. Great for preparing scenario-specific contexts.
# after_scenario(context, scenario): Runs after each scenario. Often used to clean up or capture screenshots on failure.
# after_feature(context, feature): Runs after each feature file completes.
# after_all(context): Executes after all features and scenarios have finished running, commonly used to close resources like the WebDriver.
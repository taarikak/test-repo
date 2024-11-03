Feature: Login to Saucedemo website

    #Background steps help set up shared context, like navigating to the application URL before each scenario

    Background: 
        Given I navigate to "https://www.saucedemo.com/"

    Scenario: Successful login with the valid credentials
        When I enter the username "standard_user" and password "secret_sauce"
        And I click the login button
        Then I should be logged in successful

    Scenario: Failed login with invalid credentials
        When I enter the username "invalid_user" and password "invalid_pass"
        And I click the login button
        Then I should see error message "Epic sadface: Username and password do not match any user in this service"


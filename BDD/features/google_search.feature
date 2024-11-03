Feature: Google search
    Google search for cheese

    Scenario: Finding cheese on Google search
    Given I am on the google search page
    When I search for "Cheese"
    Then the page title should start with "cheese"
Feature: Cross browser testing for google search
    Scenario Outline: Perform google search on different browsers
    Given I open the web "<browser>"
    When I navigate to google page "https://www.google.ca/" 
    And I search for word "selenium"
    Then I should see the google logo with alternate title
    Examples:
    |browser|
    |chrome|
    |firefox|
    |edge|
    |safari|

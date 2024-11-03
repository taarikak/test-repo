Feature: Verify broken links with status code
    Scenario: Check all links of webpage
    Given I am on the webpage "<url>"
    When I check all the links on webpage
    Then it should validate status code for each link
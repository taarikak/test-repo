Feature: Verify broken images links with status code
    Scenario: Check all images links of webpage
    Given I am on the broken images webpage "<url>"
    When I check all the images links on webpage
    Then it should validate status code for each image link
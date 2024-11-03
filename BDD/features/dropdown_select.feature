Feature: Verify single option from dropdown
    Scenario: Verify if single option is available for selection in dropdown
    Given I am on the dropdown page "url"
    When I select the option "Option 2" from dropdown
    Then The "Option 2" should be selected successfully
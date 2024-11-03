Feature: Login with multiple credentials
    Scenario Outline:Attempt to login with multiple credentials from CSV test data file
    Given I am on the login page
    When I login with the "<Username>" and "<Password>"
    Then I should see login result
    # The Examples section will dynamically use values from the CSV in the step definitions.
    #<> - placeholder for dynamic values
    Examples:
    |Username|Password|
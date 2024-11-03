Feature: Sunday isn't Friday
    Everyone wants to know, when is Friday

    Scenario: Verify today is not Friday when it's Sunday
        Given today is "Sunday"
        When I check if today is Friday
        Then the result should be "False"
    
#rebase
Feature: API testing

    Scenario: Validate the response from GET request
    Given I have the API endpoint "https://jsonplaceholder.typicode.com/posts/1"
    When I send a GET request
    Then the response status code should be 200
    And the response body should contain title "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"

    Scenario: Validate the response from POST request
    Given I have the API endpoint "https://jsonplaceholder.typicode.com/posts"
    When I send a POST request with following data
    | title | body | userId |
    | my title taarika| my body | 1 |
    Then the response status code should be 201
    And the response body should contain userId "1"

    #this is with amend

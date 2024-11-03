from behave import given,when,then
import requests
import json


@given('I have the API endpoint "{url}"')
def step_given_url(context,url):
    context.url = url

@when('I send a GET request')
def step_send_get_request(context):
    global response
    response = requests.get(context.url)

@when('I send a POST request with following data')
def step_post_request(context):
    #json.loads(): This method parses the JSON string and converts it into a Python dictionary.
    #Difference between json=data and data=data:
    # json=data: This automatically serializes the Python dictionary data to JSON format and sets the Content-Type header to application/json.
    # data=data: This sends the data as form-encoded (like submitting a web form). It does not serialize it to JSON.
    #context.text: This could refer to the text of a response or an incoming payload (depending on your use case in testing). It’s a string containing JSON data.
    global response
    # data = json.loads(context.text)
    post_data = {}
    for row in context.table:
        post_data['title'] = row['title']
        post_data['body'] = row['body']
        post_data['userId'] = row['userId']
    response = requests.post(context.url, json=post_data)

#You use :d when you want to format a value explicitly as a decimal integer in Python string formatting. For example, 
# in situations where you know the value should always be a whole number, 
# like HTTP status codes, you can use :d to ensure that it gets formatted correctly as an integer.
@then('the response status code should be {status_code:d}')
def step_status_code(context, status_code):
    actual_status = response.status_code
    assert actual_status == status_code, f'Expected {status_code} but got {actual_status}'

@then('the response body should contain title "{title}"')
def step_response_body(context,title):
    response_data = response.json()
    actual_data = response_data.get('title')
    assert actual_data == title, f'Expected {title} but got actual {actual_data}'

@then('the response body should contain userId "{userId}"')
def step_response_body(context,userId):
    response_data = response.json()
    actual_data = response_data['userId']
    assert actual_data == userId, f'expected {userId} but got {actual_data}'
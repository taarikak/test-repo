from behave import given, when, then

@given('today is "{day}"')
def step_given_today_is(context,day):
    context.today = day

@when('I check if today is friday')
def step_when_check_if_today_is_friday(context):
    context.is_friday = (context.today == "Friday")

@then('the result should be "{expected_result}"')
def step_then_result_should_be(context, expected_result):
    expected = (expected_result == "True")
    assert context.is_friday == expected, f"Expected {expected}, but got {context.is_friday}"

from behave import given, when, then



@given("the TV is on the home screen")
def step_impl(context):
    print("Simulating: Go to home screen")

@when("I open the YouTube app")
def step_impl(context):
    print("Simulating: Launch YouTube app")

@then("I should see the YouTube home page")
def step_impl(context):
    print("Simulating: Validate YouTube home screen")

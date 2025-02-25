from behave import *

@given('I am on the login page')
def step_impl(context):
    print("Navigating to the login page.")

@when('I enter username as "{username}" and password as "{password}"')
def step_impl(context, username, password):
    print(f"Entering username: {username} and password: {password}")

@then('I should see the dashboard page')
def step_impl(context):
    print("Dashboard page displayed.")

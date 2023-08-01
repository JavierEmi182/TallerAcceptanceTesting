from behave import *

@given('the to-do Dictionary contains tasks')
def step_impl(context):

    global dictionary
    context.dictionary = {
        "complete" : [],
        "incomplete" : []
    }

@when('the user checks if tasklist is empty')
def step_impl(context):
    global tasksList
    global cond
    cond = len(context.dictionary) <= 0

@then('output should be that the list is empty')
def step_impl(context):
    print("List is empty.")
    
from behave import *

@given('the to-do Dictionary contains tasks to list')
def step_impl(context):

    global dictionary
    context.dictionary = {
        "complete" : [],
        "incomplete" : ["Buy groceries","Take a walk","Pay bills"]
    }

@when('the user list all tasks')
def step_impl(context):
    global dictionary
    context.dictionary = {
        "Completed" : [],
        "Incompleted" : ['Buy groceries','Take a walk','Pay bills']
    }


@then('the output should contain the entire Dictionary listed by keys and numbered')
def step_impl(context):

    print(" Complete: \n Incomplete: \n 1. Buy groceries\n2. Take a walk\n3. Pay bills")

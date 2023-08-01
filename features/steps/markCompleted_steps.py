from behave import *

@given('the to-do Dictionary contains tasks Buy groceries as incomplete')
def step_impl(context):

    global dictionary
    context.dictionary = {
        "complete" : [],
        "incomplete" : ["Buy groceries"]
    }

@when('the user mark task "Buy groceries" as completed')
def step_impl(context):
    global dictionary
    context.dictionary = {
        "Completed" : ['Buy groceries'],
        "Incompleted" : []
    }
    

@then('a message will be displayed mentioning that the task Buy groceries was marked as complete')
def step_impl(context):
    print("\nMarked as complete the task: Buy groceries")
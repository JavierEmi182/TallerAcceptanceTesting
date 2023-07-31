from behave import *

# Step 1: Given the to-do Dictionary is empty
@given('the to-do Diccionary is empty')
def step_impl(context):
    #set the to-do list as an empty list
    global tasksList

    tasksList = {
        "Completed" : [],
        "Incompleted" : []
    }

@when('the user adds a task "{task}"')
def step_impl(context,task):
    global tasksList
    tasksList["Incompleted"]=task

@then('the to-do  Diccionary should contain "{task}"')
def step_impl(context,task):
    assert task in tasksList, f'Task "{task}" not found in the to-do Dictionary'
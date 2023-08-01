from behave import *

@given('the to-do Dictionary contains tasks')
def step_impl(context):
    #set the to-do list as an empty list
    global tasksList

    tasksList = {
        "Completed" : [],
        "Incompleted" : ['Buy groceries', 'Take a walk']
    }

@when('the user clears the to-do Dictionary')
def step_impl(context,task):
    global tasksList
    context.list=clearList(tasksList)

@then('the to-do Dictionary should be empty')
def step_impl(context,task):
    global tasksList
    tasksList = {
        "Completed" : [],
        "Incompleted" : []
    }
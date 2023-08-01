from behave import *

@given('the to-do Dictionary contains tasks:')
def step_impl(context):
    #set the to-do list as an empty list
    global tasksList

    tasksList = {
        "Completed" : [],
        "Incompleted" : []
    }

@when('the user checks if tasklist is empty')
def step_impl(context,task):
    global tasksList
    context.list=checkEmpty(tasksList)

@then('output should be :')
def step_impl(context,task):
    global tasksList
    tasksList = {
        "Completed" : [],
        "Incompleted" : []
    }
    print("List is empty.")
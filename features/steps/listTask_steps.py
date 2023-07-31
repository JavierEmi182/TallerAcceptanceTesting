from behave import *

@given('the to-do Dictionary contains tasks')
def step_impl(context):

    global tasksList

    tasksList = {
        "Completed" : [],
        "Incompleted" : ['Buy groceries','Take a walk','Pay bills']
    }

@when('the user list all tasks')
def step_impl(context):
    global tasksList
    tasksList = {
        "Completed" : [],
        "Incompleted" : ['Buy groceries','Take a walk','Pay bills']
    }
    
    context.list=listTasks(tasksList)

@then('the output should contain:')
def step_impl(context):
    global tasksList
    tasksList = {
        "Completed" : [],
        "Incompleted" : ['Buy groceries','Take a walk','Pay bills']
    }
    print(" Complete: \n Incomplete: \n 1. Buy groceries\n2. Take a walk\n3. Pay bills")

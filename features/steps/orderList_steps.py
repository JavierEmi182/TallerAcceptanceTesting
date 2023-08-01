from behave import *

@given('the to-do Dictionary contains tasks to sort')
def step_impl(context):
    global tasksList

    tasksList = {
        "Completed" : ['Pay bills','Finish code'],
        "Incompleted" : ['Buy groceries','Take a walk']
    }

@when('the user sort the to-do Dictionary by completed criteria')
def step_impl(context):
    global tasksList
    tasksList = {
        
    } 
    context.list=orderList(tasksList)

@then('the output should contain the list sorted:')
def step_impl(context):
    global tasksList
    tasksList = {
        "Completed" : ['Pay bills','Finish code'],
        "Incompleted" : ['Buy groceries','Take a walk']
    }
    print("1. Pay bills\n2. Finish code")
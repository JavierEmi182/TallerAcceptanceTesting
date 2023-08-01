from behave import *

@given('the to-do Dictionary contains tasks')
def step_impl(context):

    global tasksList

    tasksList = {
        "Completed" : [],
        "Incompleted" : ['Buy groceries']
    }

@when('the user mark task "Buy groceries" as completed')
def step_impl(context):
    global tasksList
    tasksList = {
        "Completed" : [],
        "Incompleted" : ['Buy groceries']
    }
    
    context.list=completeTask(tasksList)

@then('the output should contain:')
def step_impl(context):
    global tasksList
    tasksList = {
        "Completed" : ['Buy groceries'],
        "Incompleted" : []
    }
    print("\nMarked as complete the task: %s"%tasklist["Completed"][0])
    #print("\nMarked as complete the task: Buy groceries")
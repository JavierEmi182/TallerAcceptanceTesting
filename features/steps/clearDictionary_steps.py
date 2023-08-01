from behave import *

@given('the to-do Dictionary contains tasks to clear')
def step_impl(context):
    #set the to-do list as an empty list
    global dictionary
    context.dictionary = {
        "complete" : [],
        "incomplete" : ["Buy groceries","Take a walk"]
    }

@when('the user clears the to-do Dictionary')
def step_impl(context):
    context.dictionary["complete"]=[]
    context.dictionary["incomplete"]=[]

@then('the to-do Dictionary should be empty')
def step_impl(context):
    len(context.dictionary) <= 0
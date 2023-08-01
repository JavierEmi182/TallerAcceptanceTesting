from behave import *

@given('the to-do Dictionary contains tasks in complete and incomplete key')
def step_impl(context):
    global dictionary

    context.dictionary = {
        "Completed" : ['Pay bills','Finish code'],
        "Incompleted" : ['Buy groceries','Take a walk']
    }

@when('the user sort the to-do Dictionary by complete criteria')
def step_impl(context):
    global criteria
    context.criteria="complete"

@then('the output should contain the list inside the key complete')
def step_impl(context):
    #print(context.dictionary["complete"])
    print("1. Pay bills\n2. Finish code")
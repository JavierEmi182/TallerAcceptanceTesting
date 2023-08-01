from behave import *

# Step 1: Given the to-do Dictionary is empty
@given('the to-do diccionary is empty')
def given_an_empty_dictionary(context):
    #set the to-do list as an empty list
    #context.dictionary = json.loads(dictionary)
    global dictionary
    dictionary = {
        "complete" : [],
        "incomplete" : []
    }

@when('the user adds a task Buy groceries')
def add_buy_groceries(context):
    #global tasksList
    #tasksList["Incompleted"]=task
    #context.list=addTask(tasksList)
    task = "Buy groceries"
    #context.dictionary['complete']=['{context.task}']
    dictionary['incomplete']=task

@then('the to-do  Dictionary should contain Buy groceries')
def check_added(context):
    #assert task in tasksList, f'Task "{task}" not found in the to-do Dictionary'
    #print("\nMarked as complete the task: %s"%{task})
    assert "Buy groceries" in dictionary["incomplete"], f'Buy groceries is not found in dictionary'
    #print(context.dictionary)
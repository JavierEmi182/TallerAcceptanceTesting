from behave import *

# Step 1: Given the to-do Dictionary is empty
@given('the to-do dictionary is empty')
def step_impl(context):
    #set the to-do list as an empty list
    #context.dictionary = json.loads(dictionary)
    global dictionary
    context.dictionary = {
        "complete" : [],
        "incomplete" : []
    }

@when('the user adds a task "Buy groceries"')
def step_impl(context):
    #global tasksList
    #tasksList["Incompleted"]=task
    #context.list=addTask(tasksList)
    context.task = "Buy groceries"
    #context.dictionary['complete']=['{context.task}']
    context.dictionary['incomplete']=context.task
    #addTask(context.task)

@then('the a message will print with the task added "Buy groceries"')
def step_impl(context):
    #assert task in tasksList, f'Task "{task}" not found in the to-do Dictionary'
    #print("\nMarked as complete the task: %s"%{task})
    #assert "Buy groceries" in dictionary["incomplete"], f'Buy groceries is not found in dictionary'
    print("\nTask Buy groceries added.")
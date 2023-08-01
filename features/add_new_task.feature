# -- FILE: features/add_new_task.feature
Feature: Adding new task to to_do Dictionary

    Scenario: Add a task to the to-do Dictionary
        Given the to-do dictionary is empty
        """
        {
            "complete" : [],
            "incomplete" : []
        }
        """
        When the user adds a task "Buy groceries"
        Then the a message will print with the task added "Buy groceries"

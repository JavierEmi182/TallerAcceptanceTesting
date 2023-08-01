# -- FILE: features/add_new_task.feature
Feature: Adding new task to to_do Dictionary

    Scenario: Add a task to the to-do Dictionary
        Given the to-do <Dictionary> is empty
        When the user adds a task "Buy groceries"
        Then the to-do Dictionary should contain Buy groceries under key value incomplete

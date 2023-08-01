# -- FILE: features/list_tasks.feature
Feature: List all tasks in the Dictionary

    Scenario: List all tasks in the to-do Dictionary
        Given the to-do Dictionary contains tasks:
        | Complete |  Incomplete   |
        |          | Buy groceries |
        |          |  Take a walk  |
        |          |   Pay bills   |
        When the user list all tasks
        Then the output should contain the entire Dictionary listed by keys and numbered

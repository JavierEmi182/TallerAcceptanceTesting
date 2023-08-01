# -- FILE: features/mark_completed.feature
Feature: Mark task as completed

    Scenario: Mark a task as completed
        Given the to-do Dictionary contains tasks:
        |   Complete   |   Incomplete   |
        |              |  Buy groceries |

        When the user mark task "Buy groceries" as completed
        Then a message will be displayed mentioning that the task Buy groceries was marked as complete
# -- FILE: features/order_list.feature
Feature: Sorting the tasklist according to some criteria

    Scenario: Sort the tasklist according to completed tasks
        Given the to-do Dictionary contains tasks:
        |    Complete    |  Incomplete   |
        |   Pay bills    | Buy groceries |
        |   Finish code  |  Take a walk  |
        When the user sort the to-do Dictionary by completed criteria
        Then the output should contain the list inside the key Complete
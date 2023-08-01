# -- FILE: features/clear_to_do_dictionary.feature
Feature: Deleting all content of the incomplete and complete section of the Dictionary

    Scenario: Clear the entire Dictionary
        Given the to-do Dictionary contains tasks:
        | Complete |  Incomplete   |
        |          | Buy groceries |
        |          |  Take a Walk  |
        When the user clears the to-do Dictionary
        Then the to-do Dictionary should be empty:
        | Complete |  Incomplete   |
        |          |               |
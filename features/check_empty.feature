# -- FILE: features/check_emtpy.feature
Feature: Checks if the to-do Dictionary is empty

    Scenario: user checks if to-do Dictionary is empty
        Given the to-do Dictionary contains tasks:
        |   Complete   |   Incomplete   |
        |              |                |

        When the user checks if tasklist is empty
        Then output should be that the list is empty
# -- FILE: features/order_list.feature
Feature: Sorting the tasklist according to some criteria

    Scenario: Sort the tasklist according to completed tasks
        Given the to-do Dictionary contains tasks in complete and incomplete key
        """
        {
            "complete" : ["Pay bills","Finish code"],
            "incomplete" : ["Buy groceries","Take a walk"]
        }
        """
        When the user sort the to-do Dictionary by complete criteria
        Then the output should contain the list inside the key complete
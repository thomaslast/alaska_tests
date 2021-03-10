Feature: This test set is for basic Alaska interface testing

Background:
Given the api wrapper object is created


Scenario Outline:
  Given there are no bears stored
  When a bear is created with the following info:
  | bear_type   | name   | description   | age    |
  | <bear_type> | <name> | <description> | <age> |
  Then when the full bears list is requested, the bear is in the list
  Examples:
  | bear_type | name | description | age |
  | WHITE     | Hello There | This is a description | 132 |

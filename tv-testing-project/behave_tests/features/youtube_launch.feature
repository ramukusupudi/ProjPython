
Feature: Launching YouTube App

  Scenario: Open YouTube and see homepage
    Given the TV is on the home screen
    When I open the YouTube app
    Then I should see the YouTube home page

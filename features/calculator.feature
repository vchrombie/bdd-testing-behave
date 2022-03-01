# Created by p0tt3r at 01/03/22
Feature: Test Calculator Functionality

  Scenario: Addition
      Given I have the numbers 10 and 5
      When I add them
      Then I expect the result to be 15

  Scenario: Multiplication
  Given I have the numbers 10 and 5
  When I mult them
  Then I expect the result to be 50

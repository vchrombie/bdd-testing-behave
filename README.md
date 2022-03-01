# bdd-testing-behave

<img src="https://behave.readthedocs.io/en/stable/_static/behave_logo1.png" align="right">

## Installation

```
$ poetry add behave
```

## Structure

```
.
|____calculator.py
|____features
| |____steps
| | |____steps.py
| |____calculator.feature
| |____environment.py
```

- `calculator.py` contains the source code the calculator app
- `features/` contains all the files related to `behave` (feature configurations, steps, etc.)
- `features/calculator.feature` contains the feature configurations for the calculator (features, scenarios, rules, etc.)
- `features/environment.py` used to define code to run before and after certain events
- `features/steps/` contains the steps implementations
- `features/steps/steps.py` contains the steps for calculator

## Example

```
(.venv) $ behave
Feature: Test Calculator Functionality # features/calculator.feature:2

  Scenario: Addition                  # features/calculator.feature:4
    Given I have the numbers 10 and 5 # features/steps/steps.py:4 0.001s
    When I add them                   # features/steps/steps.py:11 0.000s
    Then I expect the result to be 15 # features/steps/steps.py:21 0.000s

  Scenario: Subtraction               # features/calculator.feature:9
    Given I have the numbers 10 and 5 # features/steps/steps.py:4 0.000s
    When I sub them                   # features/steps/steps.py:11 0.000s
    Then I expect the result to be 5  # features/steps/steps.py:21 0.000s

  Scenario: Multiplication            # features/calculator.feature:14
    Given I have the numbers 10 and 5 # features/steps/steps.py:4 0.000s
    When I mult them                  # features/steps/steps.py:11 0.000s
    Then I expect the result to be 50 # features/steps/steps.py:21 0.000s

  Scenario: Division                  # features/calculator.feature:19
    Given I have the numbers 10 and 5 # features/steps/steps.py:4 0.000s
    When I div them                   # features/steps/steps.py:11 0.000s
    Then I expect the result to be 2  # features/steps/steps.py:21 0.000s

1 feature passed, 0 failed, 0 skipped
4 scenarios passed, 0 failed, 0 skipped
12 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.003s

```

## Resources

- https://behave.readthedocs.io/en/stable/tutorial.html
- https://medium.com/@hmurari/bdd-quickstart-with-python-4cf366cfc11c

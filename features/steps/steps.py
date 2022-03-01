from behave import given, when, then


@given(u'I have the numbers {num1} and {num2}')
def step_impl(context, num1, num2):
    print(u'STEP: Given I have the numbers {} and {}'.format(num1, num2))
    context.num1 = int(num1)
    context.num2 = int(num2)


@when(u'I {opr} them')
def step_impl(context, opr):
    print(u'STEP: When I {} them'.format(opr))
    context.opr = opr
    context.result = context.calculator(
        context.opr,
        context.num1,
        context.num2,
    )


@then(u'I expect the result to be {result}')
def step_impl(context, result):
    print(u'STEP: Then I expect the result to be {}'.format(result))
    assert context.result == int(result), 'Expected {}, got {}'.format(result, context.result)
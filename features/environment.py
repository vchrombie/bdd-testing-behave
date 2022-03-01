from calculator import Calculator


def before_all(context):
    context.calculator = Calculator()


def after_all(context):
    del context.calculator

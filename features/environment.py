from calculator import calculator


def before_all(context):
    context.calculator = calculator


def after_all(context):
    del context.calculator

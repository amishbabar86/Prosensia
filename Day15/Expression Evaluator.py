import re

def evaluate_expression(expr, variables):
    def replace_variables(match):
        var_name = match.group(0)
        if var_name in variables:
            return str(variables[var_name])
        else:
            raise ValueError(f"Undefined variable: {var_name}")

    expr = re.sub(r'\b\w+\b', replace_variables, expr)
    return eval(expr)

def main():
    expr = "a + b * c"
    variables = {'a': 2, 'b': 3, 'c': 4}
    try:
        print("Evaluated expression:", evaluate_expression(expr, variables))
    except ValueError as e:
        print(e)

main()

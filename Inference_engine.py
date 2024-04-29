# Define rules
rules = [
    lambda a, b: (not (a and b), (not a) or (not b)),  # De Morgan 1
    lambda a, b: (not (a or b), (not a) and (not b)),  # De Morgan 2
    lambda *args: (not all(args), sum((not arg) for arg in args)),  # De Morgan 3
    lambda *args: (not any(args), 1 if all((not arg) for arg in args) else 0),  # De Morgan 4
    lambda a, b, c: ((a and b) or (not a and c), (a or c) and (not a or b)),  # Transposition
    lambda a, b, c: (a or (b and c), (a or b) and (a or c)),  # Duality
    lambda a: (a and 0, 0),  # Rule 7
    lambda a: (a or 1, 1),   # Rule 8
    lambda a: (a and 1, a),  # Rule 9
    lambda a: (a or 0, a),   # Rule 10
    lambda a: (a or a, a),   # Rule 11
    lambda a: (a and a, a),  # Rule 12
    lambda a: (a or (not a), 1),  # Rule 13
    lambda a: (a and (not a), 0),  # Rule 14
    lambda a: ((not (not a)), a),  # Rule 15
    lambda a, b: (a or b, b or a),  # Rule 16
    lambda a, b: (a and b, b and a),  # Rule 17
    lambda a, b, c: (a or (b or c), (a or b) or c),  # Rule 18
    lambda a, b, c: (a and (b and c), (a and b) and c),  # Rule 19
    lambda a, b, c: (a or (b and c), (a and b) or (a and c)),  # Rule 20
    lambda a, b: (a and (a or b), a),  # Rule 21
    lambda a, b: (a or (a and b), a),  # Rule 22
    lambda a, b: (a or (not a and b), a or b),  # Rule 23
    lambda a, b: (a and (not a or b), a and b),  # Rule 24
]

# Helper function to apply rules to the expression
def apply_rules(expression):
    stack = [expression]
    transformed_expressions = []

    while stack:
        current_expr = stack.pop()
        applied = False

        for rule in rules:
            if len(rule.__code__.co_varnames) == len(current_expr):
                result = rule(*current_expr)
                if result != current_expr:
                    if result not in transformed_expressions: # To avoid duplicates
                        transformed_expressions.append(result)
                        stack.append(result)
                    applied = True
                    break

        if not applied:
            transformed_expressions.append(current_expr)

    return transformed_expressions

# Given expression
expression = ['A.B', 'B.C\'', 'A.C']

# Apply rules to the expression
transformed_expressions = apply_rules(expression)

# Print transformed expressions
print("Transformed Expressions:")
for expr in transformed_expressions:
    print(' + '.join(map(str, expr)))  # Convert boolean values to strings for printing



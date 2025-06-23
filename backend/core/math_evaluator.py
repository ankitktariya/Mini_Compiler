import re
import math

def tokenize(expr):
    token_pattern = r"\d+\.\d+|\d+|[+\-*/^()%]|[a-zA-Z_]+"
    return re.findall(token_pattern, expr)

def precedence(op):
    return {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3}.get(op, 0)

def apply(op, b, a=None):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b
    if op == '%': return a % b
    if op == '^': return a ** b
    if op == 'u-': return -b  # Unary minus

def evaluate(expression):
    tokens = tokenize(expression.replace(" ", ""))
    values, ops = [], []
    i = 0

    while i < len(tokens):
        token = tokens[i]

        if re.match(r'\d+(\.\d+)?', token):
            values.append(float(token))

        elif token == "pi":
            values.append(math.pi)
        elif token == "e":
            values.append(math.e)

        elif token in ("sqrt", "abs", "sin", "cos", "tan"):
            ops.append(token)

        elif token == "(":
            ops.append(token)

        elif token == ")":
            while ops and ops[-1] != "(":
                op = ops.pop()
                if op in ("sqrt", "abs", "sin", "cos", "tan"):
                    arg = values.pop()
                    result = abs(arg) if op == "abs" else getattr(math, op)(arg)
                    values.append(result)
                else:
                    b = values.pop()
                    a = values.pop() if op != "u-" else None
                    values.append(apply(op, b, a))
            if ops and ops[-1] == "(":
                ops.pop()
            if ops and ops[-1] in ("sqrt", "abs", "sin", "cos", "tan"):
                func = ops.pop()
                arg = values.pop()
                result = abs(arg) if func == "abs" else getattr(math, func)(arg)
                values.append(result)

        elif token == '-' and (i == 0 or tokens[i - 1] in "(+-*/%^"):
            ops.append('u-')

        else:
            while ops and precedence(ops[-1]) >= precedence(token):
                op = ops.pop()
                b = values.pop()
                a = values.pop() if op != "u-" else None
                values.append(apply(op, b, a))
            ops.append(token)

        i += 1

    while ops:
        op = ops.pop()
        b = values.pop()
        a = values.pop() if op != "u-" else None
        values.append(apply(op, b, a))

    return values[0]

# ✅ CLI Testing Mode
if __name__ == "__main__":
    print("🔢 Smart Math Evaluator — Type 'exit' to quit")
    while True:
        expr = input("MATH> ")
        if expr.lower() in ["exit", "quit", "q"]:
            break
        try:
            result = evaluate(expr)
            print("✅ Result:", result)
        except Exception as e:
            print("❌ Error:", e)

class Calculator:
    sum = lambda a, b: a + b
    sub = lambda a, b: a - b
    mul = lambda a, b: a * b
    exp = lambda a, b: a ** b
    root = lambda a, b: a ** (1/b)
    div = lambda a, b: a/b if b!=0 else 'Não é possível dividir por 0'
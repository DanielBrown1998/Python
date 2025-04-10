from math import factorial, pow

pot = "^"
def find_exp_monomios(expr: str):
    global pot
    expr = expr.split(pot)
    neg = "-"
    n:str = expr[1]
    div = ""
    expr: str = expr[0][1:-1]

    for c in expr:
        div = c if c.isalpha() else ""
        if div:
            break

    expr = expr.split(div)
    a = expr[0]
    if not a:
        a = "1"
    elif a == "-":
        a = "-1"
    b = expr[1]

    return a, b, n, div


def expand(expr: str):
    global pot
    a, b, n, div = find_exp_monomios(expr)

    if n.strip() == "0":
        return "1"
    
    print(expr, a, b, n, div)

    coeficientes = []
    for p in range(int(n)+1):
        coeficientes.append(
            int(
                (factorial(int(n))/(factorial(p)*factorial(int(n)-p)))
                *
                pow(int(a), int(n)-p)*pow(int(b), int(p))
                 )
        )

    print(coeficientes)
    termos = ""
    for p, item in enumerate(coeficientes):

        if int(n) - p != 1:
            if item == -1:
                expr = f"-{div}{pot}{int(n)-p}"
            else:
                expr = f"{div}{pot}{int(n)-p}"

        else:
            if item == -1:
                expr = f"-{div}"
            else:
                expr = div

        
        if int(n) - p == int(n):
            if item != 1 and item != -1:
                termos += str(item) + expr
            else:
                termos += expr
        elif int(n) - p != 0:    
            if item != 1:
                termos += str(item) + expr if str(item)[0] == "-" else f"+{item}" + expr
            else:
                termos += expr
        else:
            termos += str(item) if str(item)[0] == "-" else f"+{item}"

    return termos
    

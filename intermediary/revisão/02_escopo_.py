#escopo_funções

x = 10
y = 8
print("Váriavel y antes de ser alterada", y)
def escopo():
    x = 8  # variável local
    global y
    y = 10
    print("Variável local x dentro da função: ", x)
    print("Alterando y global dentro da função y=", y)
    return x

#chamando a função
print("Variável local x fora da função: ", x)
x = escopo()
print("Variável local x fora da função após chamada da função: ", x)
print("Variável local y fora da função após chamada da função: ", y)

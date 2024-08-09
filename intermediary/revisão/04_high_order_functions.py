
# High Order Function: "funções que poden receber e/ou retornar outras funções"

def saudacau(msg):
    return msg

def executa(func, msg: str):
    return func(msg)


oi = executa(saudacau, 'oi')
print(oi)

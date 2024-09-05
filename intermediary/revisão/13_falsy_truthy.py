

# falsys:
lista = []    
dicionario = {}
tupla = ()
conjunto = set()
string = ""
numero = 0
booleano = False
intervalo = range(0)
nulo = None
flutuante = 0.0
complexo: complex = 0 + 0j  
if not complexo and isinstance(complexo, complex):
    print(complexo, type(complexo))
# truthys:
lista = [1]
dicionario = {"chave": "valor"}
tupla = (1,)
conjunto = {1}
string = " "
numero = 1
booleano = True
intervalo = range(1)
nulo = 0
flutuante = 0.1
complexo = 1j
complexo2 = 1 + 2j
complexo += complexo2
metodo = 'conjugate'
if complexo and isinstance(complexo, complex):
    if hasattr(complexo, metodo):
        print(getattr(complexo, metodo)(), end=' ')
        print(complexo, complexo.__abs__(), type(complexo))
    else:
        print(complexo, complexo.__abs__(), type(complexo))



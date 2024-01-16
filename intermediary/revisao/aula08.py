lista_par = [c for c in range(100) if c % 2 == 0]
lista_impar = [c for c in range(100) if c % 2 != 0]

my_set_par = set()
my_set_impar = set()
my_set_par.update(lista_par)
my_set_impar.update(lista_impar)
print(my_set_par)
print(my_set_impar)
print(f'A união dos conjuntos é {my_set_impar.union(my_set_par)}')
print(f'A intersecção dos conjuntos é {my_set_impar.intersection(my_set_par)}')

from types import GeneratorType

multiplica_por_3 = map(
    lambda x: x*3,
    [c for c in range(1, 6)]
)

print(multiplica_por_3)
print(*list(multiplica_por_3), sep='\n')

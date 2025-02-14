import pyomo.environ as pyo

modelo = pyo.ConcreteModel()

modelo.x_tomate = pyo.Var(domain=pyo.NonNegativeReals)
modelo.x_alface = pyo.Var(domain=pyo.NonNegativeReals)

modelo.lucro = pyo.Objective(expr=2*modelo.x_tomate + 1.5*modelo.x_alface, sense=pyo.maximize)

modelo.restricao_agua = pyo.Constraint(expr=3*modelo.x_tomate + 2*modelo.x_alface <= 6000)
modelo.restricao_espaco = pyo.Constraint(expr=2*modelo.x_tomate + 3*modelo.x_alface <= 5500)
modelo.restricao_diversificacao = pyo.Constraint(expr=modelo.x_tomate >= 0.1*modelo.x_alface)

solver = pyo.SolverFactory('glpk')
resultado = solver.solve(modelo, tee=True)


modelo.x_tomate.display()
modelo.x_alface.display()

print(f"Quantidade de tomates: {pyo.value(modelo.x_tomate)} Kg")
print(f"Quantidade de alfaces: {pyo.value(modelo.x_alface)} Kg")

print(f"Lucro total: R${pyo.value(modelo.lucro)}")

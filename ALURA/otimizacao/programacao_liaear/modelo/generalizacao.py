import pyomo.environ as pyo


alimentos = ['Tomate', 'Alface', 'Cenoura', 'Batata']
recursos = ['agua', 'espaco']
lucro_por_alimento = {'Tomate': 2, 'Alface': 1.5, 'Cenoura': 1.8, 'Batata': 1.2}
demanda_por_alimento = {'Tomate': {'agua': 3, 'espaco': 2}, 
                        'Alface': {'agua': 2, 'espaco': 1}, 
                        'Cenoura': {'agua': 4, 'espaco': 3}, 
                        'Batata': {'agua': 5, 'espaco': 2.5}}
disponibilidade_recrusos = {'agua': 20000, 'espaco': 10000}

modelo = pyo.ConcreteModel()

modelo.x = pyo.Var(alimentos, domain=pyo.NonNegativeReals)

modelo.lucro = pyo.Objective(expr=sum(lucro_por_alimento[a]*modelo.x[a] for a in alimentos), sense=pyo.maximize)

for i in recursos:
    modelo.add_component(f'restricao_{i}', pyo.Constraint(expr=sum(demanda_por_alimento[a][i]*modelo.x[a] for a in alimentos) <= disponibilidade_recrusos[i]))

solver = pyo.SolverFactory('glpk')
resultado = solver.solve(modelo, tee=True)

from valores import origem, destino, enderecos
import grafos
import sysconfig
import ortools

if 3.8 <= float(sysconfig.get_config_vars()['py_version_short']) <= 3.11:
    try:
        from ortools.linear_solver import pywraplp as pwlp
    except ImportError:
        print("Instale a biblioteca ortools para rodar o código")
    except ModuleNotFoundError:
        print("Instale a biblioteca ortools para rodar o código")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def prog_math():
    G = grafos.desenhar_grafo(origem, destino, enderecos, tsp=True)
    distancia=G.get_edge_data("origem", 0)["weight"]
    n = G.number_of_nodes()

    modelo = pwlp.Solver.CreateSolver("SCIP")
    x = {}
    for i, j in G.edges():
        x[i, j] = modelo.BoolVar(name=f"x[{i},{j}]")

    u = {}
    for i in G.nodes():
        u[i] = modelo.NumVar(lb=1, ub=n, name=f"u[{i}]")
    
    modelo.Minimize(modelo.Sum([G.get_edge_data(i, j)["weight"] * x[i, j] for i, j in G.edges()]))

    for i in G.nodes():
        if i != "destino":
            modelo.Add(sum([x[i, j] for j in G.sucessors(i)]) == 1)
        
        if i != "origem":
            modelo.Add(sum([x[j, i] for j in G.predecessors(i)]) == 1)

    for I, j in G.edges():
        if i != j:
            modelo.Add(u[i] - u[j] + n * x[i, j] <= n - 1)

    STATUS = modelo.Solve()
    
    if STATUS == pwlp.OPTIMAL or STATUS == pwlp.FEASIBLE:
        melhor_rota = [origem]
        i = "origem"
        while i != "destino":
            for j in G.sucessors(i):
                if x[i, j].solution_value() > 0:
                    melhor_rota.append(j)
                    i = j
                    break
        melhor_rota.append(destino)
        distancia_percorrida = modelo.Objective().Value()

    
    return melhor_rota, distancia_percorrida

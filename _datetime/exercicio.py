from datetime import datetime, timedelta

emprestimo = 1_000_000
taxa_mes = 0.01
tempo_anos = 5
total_meses = tempo_anos*12
dia_vencimento_emprestimo = 20
data_de_requisicao_emprestimo = '20/12/2020' 
fmt = "%d/%m/%Y"
# calculo total do valor do emprestimo
for mes in range(total_meses):
    if mes == 0:
        emprestimo_com_juros = round(emprestimo + emprestimo*taxa_mes,2)
    emprestimo_com_juros += round((emprestimo_com_juros * taxa_mes),2)

pagamento_mensal = round(emprestimo_com_juros/total_meses, 2)

data_de_requisicao_emprestimo = datetime.strptime(data_de_requisicao_emprestimo, fmt)
for c in range(total_meses):
    if data_de_requisicao_emprestimo.month in [1, 3, 5, 7, 8, 10, 12]:
        data_de_requisicao_emprestimo += timedelta(days=31)
    elif data_de_requisicao_emprestimo.month == 2:
        if data_de_requisicao_emprestimo.year % 2 != 0 or (data_de_requisicao_emprestimo.year % 2== 0 and int(data_de_requisicao_emprestimo.year) % 4 != 0):
            data_de_requisicao_emprestimo += timedelta(days=28)
        else:
            data_de_requisicao_emprestimo += timedelta(days=29)
    else:
        data_de_requisicao_emprestimo += timedelta(days=30)
    emprestimo_com_juros -= pagamento_mensal
    if c == 59:
        pagamento_mensal += round(emprestimo_com_juros, 2)
        emprestimo_com_juros = 0
    print(f"parcela número {c+1}, faltam {total_meses-(c+1)}\n"
          f"vencimento: {datetime.strftime(data_de_requisicao_emprestimo, fmt)}\n"
          f"valor a pagar: {pagamento_mensal}\n"
          f"valor do emprestimo a pagar: {round(emprestimo_com_juros, 2)}\n\n")

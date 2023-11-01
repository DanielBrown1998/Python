from datetime import datetime, timedelta

valor_inicial = 10**6
valor_juros = 1.57*valor_inicial
nome = 'Maria'
date_initial = datetime(2020, 12, 20)
month = 60
valor_parcela = valor_juros/month
print(f"O empréstimo de R${valor_inicial:,.2f} foi pego  por {nome} no dia {date_initial.strftime('%d/%m/%Y')}")
print(f"O valor total do empréstimo com juros foi e R${valor_juros:,.2f}")
date_pay = date_initial
for c in range(month):
    date_pay += timedelta(days=25)
    while date_pay.day != 20:
        date_pay += timedelta(days=1)
    print(f"data: {date_pay.strftime('%d/%m/%Y')} valor: R${valor_parcela:,.2f}")

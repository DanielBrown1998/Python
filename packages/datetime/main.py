from datetime import datetime
hora = str(datetime.now()).split(' ')[1].split('.')[0]
fmt = '%Y-%m-%d'

print(hora, '09:00:00' < hora < '18:00:00')

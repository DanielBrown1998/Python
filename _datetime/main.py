from datetime import datetime, timedelta, timezone
from typing import List, Optional


#fmt = "%d/%m/%Y %H:%M:%S"
fmt = "%d/%m/%Y"
date_today = datetime.now()
date_nasc = datetime.strptime('03/02/1998', fmt)
delta = date_today-date_nasc # timedelta é adiferença entre duas datas
#time_delta = timedelta(days=7)
#print(date_today + time_delta)
#print(delta.days//365)
days = 10
for day in range(days):
    dia = datetime.strftime(date_today + timedelta(days=day), fmt)
    week_day = datetime.strptime(dia , fmt).isoweekday()
    if week_day not in [6, 7]:
        print(dia)

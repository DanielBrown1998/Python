from datetime import datetime
from pytz import timezone
fmt = '%Y-%m-%d %H:%M:%S'
data_start = datetime.strptime("2023-10-30 17:02:30", fmt)
data_fim = datetime.strptime("2024-01-01 00:00:00", fmt)
data = datetime.strptime("2023-12-30 17:02:30", fmt)
# data = datetime.now()
delta = data_start - data_fim
print(data + delta)


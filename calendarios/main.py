import calendar
import datetime

#print(calendar.calendar(2024))
#print(list(calendar.day_name))

num_first_day, last_day = calendar.monthrange(2024, 8)
print(calendar.day_name[num_first_day], last_day)
print(calendar.day_name[calendar.weekday(2024, 8, last_day)])
print(*calendar.monthcalendar(2024, 8), sep='\n')
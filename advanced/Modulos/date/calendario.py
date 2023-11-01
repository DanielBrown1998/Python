import calendar
# print(calendar(2023))
# x, y = calendar.monthrange(2023, 5)
# print(f"dia {y} de {calendar.month_name[5]} de 2023, {list(calendar.day_name)[x]}")

day_week = calendar.day_name
for week in calendar.monthcalendar(2023, 7):
    for e, c in enumerate(week):
        if c == 0:
            continue
        else:
            print(f"{day_week[e]}: {c}")

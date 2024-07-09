import locale
import os
import sys
import calendar

locale.setlocale(locale.LC_ALL, locale.getlocale()[0]+'.UTF-8')

print(calendar.calendar(2024))
print('.'.join(locale.getlocale()))

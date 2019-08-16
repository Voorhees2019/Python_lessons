from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta  # difference in dates
import locale

d1 = date(2019, 7, 10)  # year, month, day
print(d1)
print(d1.year)
print(d1.month)
print(d1.day)
print('----------------------------')
t1 = time(23, 15, 9)
print(t1)
print(t1.hour)
print(t1.minute)
print(t1.second)
print('----------------------------')
print('today is {}'.format(date.today()))
print(f'max date: {date.max}')
print(f'min date: {date.min}')
print(f'max time: {time.max}')
print(f'min time: {time.min}')
print('----------------------------')
dt = datetime(2019, 6, 17, 8)
print(dt)
print(dt.date().year)
print(dt.time().hour)
now_dt = datetime.now()
print(f'now_dt: {now_dt}')
new_dt = now_dt.replace(year=2010)
print('new_dt = {}'.format(new_dt))
print('----------------------------')
dt = datetime.strptime('10/07/2019', '%d/%m/%Y')  # %d - day, %m - month, %Y - year in 4 digits, %y - year in 2 digits
print(dt)
dt = datetime.strptime('10/07/2019 17:29', '%d/%m/%Y %H:%M')  # %H - hours in 24h format, %M - minutes
print(dt)
dt = datetime.strptime('07-10-2019 17:31', '%m-%d-%Y %H:%M')
print(dt)
dt = datetime.strptime('2019-07-10', '%Y-%m-%d')
print(dt)
print('----------------------------')
print(locale.setlocale(locale.LC_ALL, ''))
now = datetime.now()
print(now.strftime('%d.%m.%Y (%a)'))  # strftime - в каком формате хотим увидеть объект типа datetime.
# %a - сокращенный вывод дня недели, %A - полное название дня недели
print(now.strftime('%Y.%B.%d (%A)'))  # %B - полное название месяца, %b - сокращенное название месяца
print('----------------------------')
delta1 = timedelta(days=3, hours=2, minutes=10)
delta2 = timedelta(days=2, hours=1, minutes=2)
print(delta1-delta2)
print(delta2-delta1)
my_birthday = date(2000, 6, 17)
delta = date.today() - my_birthday
print(type(delta))
my_age = int(delta.days/365)
print(f'my age is {my_age}')
friend_birthday = date(2000, 7, 15)
am_i_older = my_birthday < friend_birthday
print(am_i_older)


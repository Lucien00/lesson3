import datetime as dt
dt_now = dt.date.today()
delta = dt.timedelta(days=1)
print('Сегодня: ', dt_now)
print('Вчера: ', dt_now - delta)
print ('Месяц назад: ', dt_now - dt.timedelta(1*365/12))


strd = "01/01/17 12:10:03.234567"
date_dt = dt.datetime.strptime(strd, '%d/%m/%y  %H:%M:%S.%f')
print(date_dt)
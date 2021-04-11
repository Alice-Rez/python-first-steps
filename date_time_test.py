import datetime

now = datetime.datetime.now()
now_formated = now.strftime("%d/%m/%Y %H:%M:%S")
now_day = now.strftime("%d")
print(now)
print(now_formated)
print(now_day)

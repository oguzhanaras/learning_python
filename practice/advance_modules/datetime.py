from datetime import datetime

print(datetime.now())

suan = datetime.now()

print(suan.year)
print(suan.month)

print(datetime.strftime(suan, "%Y %B"))

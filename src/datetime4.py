import datetime

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
delta.days, delta.seconds, delta.microseconds
print(delta.days, delta.seconds, delta.microseconds)

delta.total_seconds()
print(delta.total_seconds())

str(delta)
print(str(delta))

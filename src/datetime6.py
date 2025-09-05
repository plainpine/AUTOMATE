import datetime

oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
oct21st
print(oct21st)

oct21st - aboutThirtyYears
print(oct21st - aboutThirtyYears)

oct21st - (2 * aboutThirtyYears)
print(oct21st - (2 * aboutThirtyYears))

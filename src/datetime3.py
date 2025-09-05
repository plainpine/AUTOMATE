import datetime

halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
halloween2019 == oct31_2019
print(halloween2019 == oct31_2019)

halloween2019 > newyears2020
print(halloween2019 > newyears2020)

newyears2020 > halloween2019
print(newyears2020 > halloween2019)

newyears2020 != oct31_2019
print(newyears2020 != oct31_2019)

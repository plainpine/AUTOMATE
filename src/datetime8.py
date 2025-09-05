import datetime
import time
oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
oct21st.strftime('%Y/%m/%d %H:%M:%S')
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))

oct21st.strftime('%I:%M %p')
print(oct21st.strftime('%I:%M %p'))

oct21st.strftime("%B of '%y")
print(oct21st.strftime("%B of '%y"))

import os
import census2010

os.chdir('.\work')

census2010.all_data['AK']['Anchorage']
print(census2010.all_data['AK']['Anchorage'])

anchoragePop = census2010.all_data['AK']['Anchorage']['pop']
print('2021年のアンカレッジの人口は ' + str(anchoragePop))

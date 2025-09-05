#! python3
# prettifiedStopwatch.py
# DOS窓で実行

import pyperclip, time

print('ENTER を押すと開始します。次にENTERを押すとラップを表示します。CTRL-Cを押して終了します。')
input()				
print('開始')
startTime = time.time()	
lastTime = startTime
lapNum = 1

lapTimes = []

try:
	while True:
	
		# 記録
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		
		# ラップ整形
		lap = 'ラップ # %s: ' % lapNum
		ttime = str(totalTime).rjust(7)
		ttimeSep = ' ('
		ltime = str(lapTime).rjust(7)
		ltimeSep = ')'
		formatted = lap + ttime + ttimeSep + ltime + ltimeSep
		
		print(formatted, end='')
		lapNum += 1
		lastTime = time.time()
		lapTimes.append(formatted)
		
except KeyboardInterrupt:
	print('\n終了')
	
	# Copy to pyperclip.
	pyperclip.copy('\n'.join(lapTimes))

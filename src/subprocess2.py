import subprocess

home = r'C:\users\plain'
path = rf'{home}\AppData\Local\Microsoft\WindowsApps\mspaint.exe'
#print(path)

paintProc = subprocess.Popen(path)
paintProc.poll() == None
print(paintProc.poll() == None)

paintProc.wait() # ペイントが終了するまで待つ

paintProc.poll() == None
print(paintProc.poll() == None)

paintProc.poll()
print(paintProc.poll())

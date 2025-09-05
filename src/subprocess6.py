fileObj = open('hello.txt', 'w')
fileObj.write('Hello, world!')

fileObj.close()

import subprocess
subprocess.Popen(['start', 'hello.txt'], shell=True)

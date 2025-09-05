# -*- coding: utf-8 -*-
#! python3

# madlibs.py - ADJECTIVE、NOUN、ADVERB、VERBという単語がテキストファイルのどこに出てきても、
# ユーザーが独自のテキストを設定できるプログラム。

import re

mad_libs = open("C:\\Users\\plain\\madlibs.txt", "w")
mad_libs.write('''The ADJECTIVE panda walked to the NOUN and then VERB.
A nearby NOUN was unaffected by these events.''')
mad_libs.close()

mad_libs = open("C:\\Users\\plain\\madlibs.txt")
content = mad_libs.read()
mad_libs.close()
check = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

while True:
    result = check.search(content)
    if result == None:
        break
    elif result.group() == "ADJECTIVE" or result.group() == "ADVERB":
        print("Enter an %s:" % (result.group().lower()))
    elif result.group() == "NOUN" or result.group() == "VERB":
        print("Enter a %s:" % (result.group().lower()))
    i = input()
    content = check.sub(i, content, 1)

print(content)
print("Name your file:")
name = input()
new_file = open(".\\%s.txt" % (name), "w")
new_file.write(content)
new_file.close()

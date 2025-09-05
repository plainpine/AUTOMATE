spam = ['apples', 'bananas', 'tofu', 'cats']

def commaCode(s):
    outStr = ""
    for i in range(len(s)):
        if i == 0:
            outStr = s[i]
        elif i == len(s) - 1:
            outStr = outStr + " and " + s[i]
        else:
            outStr = outStr + ", " + s[i]

    return outStr

print(commaCode(spam))

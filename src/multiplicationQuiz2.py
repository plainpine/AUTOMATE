import random, time

for i in range(10):
    a=random.randint(0,9)
    b=random.randint(0,9)
    correctAns=a*b
    startTime=time.time()
    print('Q-'+str(i+1)+':  計算結果は？ '+str(a)+'x'+str(b)+'   ')
    result=0
    for i in range(3):
        userAns=input('-->Try-'+str(i+1)+':  ')
        if userAns.isdecimal() :
            if int(userAns)==correctAns:
                result=1
                if result==1:
                    endTime=time.time()
                    totalTime=endTime-startTime
                break

                time.sleep(1)
            else:
                print('答えが間違っています')
        else:
            print('答えが間違っています')

    if result==1:
        if totalTime<=8:
            print('正解！')
        else:
            print("正解ですが、 残念ながら時間切れです！")

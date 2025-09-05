import time
def calcProd():
    # 1～999,999の積を求める
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product
startTime = time.time()
prod = calcProd()
endTime = time.time()
print('計算結果は %s 桁です。' % (len(str(prod))))
print('計算時間は %s 秒でした。' % (endTime - startTime))

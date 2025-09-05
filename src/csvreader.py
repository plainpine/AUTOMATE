import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
exampleData
print(exampleData)

exampleData[0][0]
print(exampleData[0][0])
exampleData[0][1]
print(exampleData[0][1])
exampleData[0][2]
print(exampleData[0][2])
exampleData[1][1]
print(exampleData[1][1])
exampleData[6][1]
print(exampleData[6][1])

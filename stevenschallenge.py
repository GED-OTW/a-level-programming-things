names = ["0:Isaac", "1:Gio", "2:Lloyd", "3:Caleb", "4:Mufed", "5:Richard", "6:Alex", "7:Sem", "8:Matt", "9:Alfie"]
daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
testScores = [
    [12, 14, 18, 25, 7, 23, 30],
    [25, 78, 90, 65, 98, 34, 43],
    [77, 65, 45, 87, 34, 78, 76],
    [12, 77, 45, 34, 78, 37, 27],
    [87, 57, 40, 49, 99, 100, 67],
    [74, 95, 36, 87, 34, 23, 97],
    [74, 24, 23, 74, 34, 23, 45],
    [35, 76, 85, 23 ,69, 23, 77],
    [34, 8, 54, 3, 45, 4, 7, 98,],
    [23, 55, 87, 19]
]
for i in range(len(testScores)):
    print("###################################")
    print(names[i])
    for j in range(len(testScores[0])):
        if j < 6:
            print(str(testScores[i][j]), end=" | " )
        else:
            print(str(testScores[i][j]))
    print("....................................")

#def printscores():
 #   print("_____________________________")
  #  for i in range(len(names)):
   #     print(names[i] + ": " + str(testScores[i]))

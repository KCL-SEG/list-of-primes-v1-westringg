import math


def medianGenerator(givenList):
    sortedList = givenList.sort()
    listLength = len(givenList)
    
    if(listLength%2>0):
        return givenList[math.floor(listLength/2)]
    else:
        return (givenList[math.floor(listLength/2)-1] + givenList[math.floor(listLength/2)])/2 

'''
print(medianGenerator([1,2,3,4,5]))
print(medianGenerator([8, 789, 2, 9, 391]))
print(medianGenerator([6,7,9,4658,2365,1,1,1]))
print(medianGenerator([2,2,2,9,9,9,9,2,2,2]))
print(medianGenerator([3]))
'''
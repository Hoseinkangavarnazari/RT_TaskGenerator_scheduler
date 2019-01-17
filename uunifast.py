import random
from math import floor


def generateTaskFromUtilization(UtilizationSet):
    taskList = []
    for i in range(len(UtilizationSet)):
        p = random.randint(1, 100)
        e = p * UtilizationSet[i]
        taskList.append(task(p, e))
    return taskList


class task(object):
    def __init__(self, p, e):
        self.period = p
        self.executionTime = e

    def Period(self):
        return self.period

    def ExecutionTime(self):
        return self.executionTime

    def Utilization(self):
        return (self.period)/(self.executionTime)

    def RelativeDeadline(self):
        return self.period


def uunifast(n, U):
    vectU = []
    sumU = U
    for i in range(1, n):
        # nextSumU = sumU * (random.uniform(0, 1)**(1/(n-i)))
        # if(nextSumU == 0):
        #     i = i-1
        nextSumU = sumU * (random.uniform(0, 1)**(1/(n-i)))
        vectU.append(sumU-nextSumU)
        sumU = nextSumU

    vectU.append(sumU)

    AllSum = 0
    for i in range(len(vectU)):
        AllSum += vectU[i]
    # print(AllSum)

    return AllSum, vectU


def writeTaskSetToFile(TaskSetID, taskSetList, file):

    # append to file here
    file.write("Task Set : " + str(TaskSetID))
    file.write("\n")
    for i in range(len(taskSetList)):
        file.write(str(taskSetList[i].Period()) + " " +
                   str(taskSetList[i].ExecutionTime()) + "\n")


def uunifasts(N, n, U):
    file = open("Task_List.txt", "a")
    counter = 1
    while(counter <= N):
        Sum, Vect = uunifast(n, U)
        # Because of rounding error, accept Task List only when Utilization is exactly equal to 1
        if(Sum == 1):
            # call function that makes the
            taskSet = generateTaskFromUtilization(Vect)
            writeTaskSetToFile(counter, taskSet, file)
            counter += 1


uunifasts(100, 100, 1)

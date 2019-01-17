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

        # in case we not to generate a task with 0 utilization
        # so we candidate a nextSumU and as it satisfies our constraint, we'll use it as nextSumU
        nextSumUCandidate = sumU * (random.uniform(0, 1)**(1/(n-i)))
        if (sumU - nextSumUCandidate != 0):
            nextSumU = nextSumUCandidate
            vectU.append(sumU-nextSumU)
            sumU = nextSumU
        else:
            i -= 1
            print ("***************")

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
    for i in range(0, N):
        Sum, Vect = uunifast(n, U)
        # Because of rounding error, accept Task List only when Utilization is exactly equal to 1
        if(Sum == 1):
            # call function that makes the
            taskSet = generateTaskFromUtilization(Vect)
            writeTaskSetToFile(i, taskSet, file)
        else:
            i -= 1


uunifasts(100, 100, 1)

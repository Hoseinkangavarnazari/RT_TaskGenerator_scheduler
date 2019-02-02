import random

def generateTaskFromUtilization(UtilizationSet):
    taskList = []
    for i in range(len(UtilizationSet)):
        p = random.randint(1, 100)
        e = p * UtilizationSet[i]
        taskList.append(task(p, e))
    return taskList


def writeTaskSetToFile(TaskSetID, taskSetList, file):

    # append to file here
    file.write("Task Set : " + str(TaskSetID))
    file.write("\n")
    for i in range(len(taskSetList)):
        file.write(str(taskSetList[i].Period()) + " " +
                   str(taskSetList[i].ExecutionTime()) + "\n")


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

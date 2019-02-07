import random


def generateTaskFromUtilization(UtilizationSet):
    taskList = []
    for i in range(len(UtilizationSet)):
        p = random.randint(2, 10)
        e = p * UtilizationSet[i]
        taskList.append(task(p, e))
    return taskList


def writeTaskSetToFile(TaskSetID, taskSetList, file):
    # append to file here
    file.write("Task Set : " + str(TaskSetID))
    file.write("\n")
    for i in range(len(taskSetList)):
        file.write(str(taskSetList[i].Period()) + " " +
                   str(taskSetList[i].Utilization()) + "\n")


class task(object):
    def __init__(self, p, e):
        self.period = p
        self.executionTime = e
        self.seen = False
        self.ID = -1
        self.executedTime = 0
        self.cycle = 1

    def Period(self):
        return self.period

    def getExecutionTime(self):
        return self.executionTime

    def getExecutedTime(self):
        return self.executedTime

    def Utilization(self):
        return (self.executionTime)/(self.period)

    def RelativeDeadline(self):
        return self.period

    def getSeenFlag(self):
        return self.seen

    def seenFlagActivation(self):
        self.seen = True
        return True

    def setID(self, ID):
        self.ID = ID

    def getID(self):
        return self.ID

    def reset(self):
        self.seen = False
        self.cycle += 1
        self.executedTime = 0

    # it's automatically activate seen flag
    def execute(self, currentTime):
        self.executedTime = self.executedTime + 1
        if(self.executedTime == self.executionTime):
            self.seenFlagActivation()
        # if(currentTime > self.period):
        #     return False
        # else:
        #     return True

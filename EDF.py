# Hosein Kangavar Nazari - CS student, IASBS university
# RealTime course second assinment's code
# implementation of earliest deadline first algorithm

from task import task
from math import floor
from LCM import LCM
INFINITY = 9999999999

def readTaskLists(FileAddress):
    tasksListDB = open(FileAddress, 'r')

    # get configuration data
    TASKS_SET_NUMBERS, TASKS_NUMBER_IN_A_SET = tasksListDB.readline().split()
    # change the type from string to integer
    TASKS_SET_NUMBERS = int(TASKS_SET_NUMBERS)
    TASKS_NUMBER_IN_A_SET = int(TASKS_NUMBER_IN_A_SET)

    # It's a two dimentional list that keeps all tasks list files
    TaskSetsHolder = []
    for taskSetID in range(0, TASKS_SET_NUMBERS):
        # it's not needed for this function but it holds the task ID number
        # I just use this here to skip this line
        taskID = tasksListDB.readline()

        # Holds data about a Task list
        taskListObj = []
        for i in range(0, TASKS_NUMBER_IN_A_SET):
            jobInfo = tasksListDB.readline().split()

            # This steps store the data wich has been readed form file
            # calculate new period , utilization and execution time
            # I have saved 3 floating point for utilization and multiply period with 1000 in order to have integer execution time
            # It's a lot easier to coup with integer execution time than float one
            p = int(jobInfo[0])*1000
            u = floor(float(jobInfo[1])*1000)/1000
            e = round(p * u)
            newCreatedTask = task(p, e)
            newCreatedTask.setID(i)
            taskListObj.append(task(p, e))

        TaskSetsHolder.append(taskListObj)

    return TaskSetsHolder, TASKS_SET_NUMBERS, TASKS_NUMBER_IN_A_SET


def findMinimumDeadlineNotSeen(TaskSet):
    minimum = INFINITY
    minID = -1
    for i in range (0 , len(TaskSet)):
        if (TaskSet[i].period <= minimum and TaskSet[i].getSeenFlag() == False):
            minimum = TaskSet[i].period
            minID = i
    
    #seen flag will be activated outside
    return minID



TaskSetsHolder, TASKS_SET_NUMBERS, TASKS_NUMBER_IN_A_SET = readTaskLists(
    "Task_List.txt")

GlobalTaskSetsSchedulingArray = [] 
# EDF algorithm starts from here
for i in range(0, TASKS_SET_NUMBERS):
    periodList = []
    for j in range(0, TASKS_NUMBER_IN_A_SET):
        periodList.append(TaskSetsHolder[i][j].period)

    hyperPeriod = LCM(periodList)
    # lest consider that our hyper period is equal to 10000
    hyperPeriod = 10000
    LocalTaskSetSchedulingArray =  [hyperPeriod]

    # print(hyperPeriod)
    k = 0 

    # while (k < hyperPeriod):
    #     print("test")
    #     # find the minimum period which haven't seen yet 
    #     # until the period of that write it's id into the
    #     # set K to the k = k + execution time of that task 
    # # write the result into a file acctually append to a file 

    for k in range ( 0, hyperPeriod):
        minimumID = findMinimumDeadlineNotSeen(TaskSetsHolder[i])
        TaskSetsHolder[i][minimumID].seenFlagActivation()
        for k in range ( k , k +  TaskSetsHolder[i][minimumID].ExecutionTime ):
            LocalTaskSetSchedulingArray[k]= minimumID
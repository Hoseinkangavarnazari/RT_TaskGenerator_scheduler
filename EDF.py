# Hosein Kangavar Nazari - CS student, IASBS university
# RealTime course second assinment's code
# implementation of earliest deadline first algorithm

from task import task
from math import floor
from LCM import LCM
INFINITY = 9999999999


def checkFeasibility(Task_list, currentTime):
    # for each task that period%currentTime == 0
    # if executed == execution it's ok, else miss have happend in system
    # if executed == execution, call reset function

    if(currentTime == 10000):
        a = 0
        for i in range(len(Task_list)):
            a = a + Task_list[i].Utilization()
    if(currentTime != 0):
        for i in range(0, len(Task_list)):
            if((currentTime % Task_list[i].Period()) == 0):
                if(Task_list[i].getExecutedTime() == Task_list[i].getExecutionTime()):
                    Task_list[i].reset()
                else:
                    return False

    return True


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
        totalU = 0
        for i in range(0, TASKS_NUMBER_IN_A_SET):
            jobInfo = tasksListDB.readline().split()

            # This steps store the data wich has been readed form file
            # calculate new period , utilization and execution time
            # I have saved 3 floating point for utilization and multiply period with 1000 in order to have integer execution time
            # It's a lot easier to coup with integer execution time than float one

            p = int(jobInfo[0])*1000
            u = floor(float(jobInfo[1])*1000)/1000
            e = round(p * u)

            # just for test , we should turn this off for real Tasksets
            #p = int(jobInfo[0])
            #u = float(jobInfo[1])
            #e = round(p * u)

            newCreatedTask = task(p, e)
            # increased by one, starts ID's from one
            newCreatedTask.setID(i+1)
            taskListObj.append(newCreatedTask)

        TaskSetsHolder.append(taskListObj)

    return TaskSetsHolder, TASKS_SET_NUMBERS, TASKS_NUMBER_IN_A_SET


def findMinimumDeadlineNotSeen(TaskSet, currentTime):
    minimum = INFINITY
    minID = 0
    for i in range(0, len(TaskSet)):
        if ((TaskSet[i].period * TaskSet[i].cycle) <= minimum and TaskSet[i].getSeenFlag() == False):
            minimum = TaskSet[i].period * TaskSet[i].cycle
            minID = TaskSet[i].getID()
    # seen flag will be activated outside
    return minID


def writeSchedulerToFile(GlobalTaskSetsSchedulingArray):
    file = open("SchedulerList.txt", "w")

    for i in range(0, len(GlobalTaskSetsSchedulingArray)):
        # Taskset numbers start at 1 but i starts from zero so i shifted that one unit
        file.write("Task Set : " + str(i+1))
        file.write("\n")
        if(len(GlobalTaskSetsSchedulingArray[i]) == 0):
            file.write(" Missed " + " " + "\n")
            continue

        for j in range(0, len(GlobalTaskSetsSchedulingArray[i])):
            #  j shows the time and the GlobalTaskSetsSchedulingArray[i][j] has the id
            file.write(str(j) + " " +
                       str(GlobalTaskSetsSchedulingArray[i][j]) + "\n")


def fullyExecuted(TaskSet):
    for i in range(0, len(TaskSet)):
        if (TaskSet[i].getExecutedTime() != TaskSet[i].getExecutionTime()):
            return False
    return True


TaskSetsHolder, TASKS_SET_NUMBERS, TASKS_NUMBER_IN_A_SET = readTaskLists(
    "Task_List.txt")

# Store all scheduler results
GlobalTaskSetsSchedulingArray = []
# EDF algorithm starts from here
for i in range(0, TASKS_SET_NUMBERS):
    print("Running stage: ", i)
    # finding hyperperiod
    periodList = []
    for j in range(0, TASKS_NUMBER_IN_A_SET):
        periodList.append(TaskSetsHolder[i][j].period)

    hyperPeriod = LCM(periodList)

    # lest consider that our hyper period is equal to 10000
    # hyperPeriod = 10000
    # check for this wether it's empty or not
    LocalTaskSetSchedulingArray = []

    print(hyperPeriod)
    k = 0
    counterTEST = 0
    counterTEST2 = 0

    missedFlag = False
    for k in range(0, hyperPeriod):

        flagLocalSeen = False
      
        feasible = checkFeasibility(TaskSetsHolder[i], k)

        if(feasible == False):
            missedFlag = True
            break

        # find the earliest deadLine task
        minimumID = findMinimumDeadlineNotSeen(TaskSetsHolder[i], k)
        if(minimumID > 10 or minimumID < 0):
            print("pause")
        # if minimumID is equal to -1 it means is idle for rest of this
        if (minimumID == 0):
            LocalTaskSetSchedulingArray.append(minimumID)
            flagLocalSeen = True
        else:
            counterTEST += 1
            # execute that task for 1 cycle
            # this function itself handels all thing related to deadline
            TaskSetsHolder[i][minimumID-1].execute(k)
            LocalTaskSetSchedulingArray.append(minimumID)
            flagLocalSeen = True

    if (missedFlag == False and fullyExecuted(TaskSetsHolder[i])):
        GlobalTaskSetsSchedulingArray.append(LocalTaskSetSchedulingArray)
    else:
        GlobalTaskSetsSchedulingArray.append([])
writeSchedulerToFile(GlobalTaskSetsSchedulingArray)

# we will need a function to write to file

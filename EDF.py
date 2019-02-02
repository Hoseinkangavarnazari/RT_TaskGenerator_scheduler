# Hosein Kangavar Nazari - CS student, IASBS university
# RealTime course second assinment's code
# implementation of earliest deadline first algorithm

from task import task
from math import floor

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
        #it's not needed for this function but it holds the task ID number 
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
            taskListObj.append(task(p, e))
        TaskSetsHolder.append(taskListObj)
    return TaskSetsHolder


TaskSetsHolder = readTaskLists("Task_List.txt")

print("done")
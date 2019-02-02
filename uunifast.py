# Hosein Kangavar Nazari - CS student, IASBS university 
# RealTime course first assinment's Code 
# UUnifast for making different task sets

import random
from task import task, generateTaskFromUtilization, writeTaskSetToFile


def uunifast(n, U):
    vectU = []
    sumU = U
    for i in range(1, n):
        nextSumU = sumU * (random.uniform(0, 1)**(1/(n-i)))
        vectU.append(sumU-nextSumU)
        sumU = nextSumU
    vectU.append(sumU)
    AllSum = 0

    #summation over all utilization for finding global utilization
    for i in range(len(vectU)):
        AllSum += vectU[i]

    return AllSum, vectU


def uunifasts(N, n, U):
    file = open("Task_List.txt", "a")
    counter = 1
    while(counter <= N):
        Sum, Vect = uunifast(n, U)
        # Because of rounding errors, utilization may not be same as given U
        # for example, 0.9999 is unacceptable when utilization(U) is equal to 1
        if(Sum == U):
            # call function that makes the
            taskSet = generateTaskFromUtilization(Vect)

            #counters seperates outputs of each runs
            writeTaskSetToFile(counter, taskSet, file)
            counter += 1
    file.close()

# run 1000 time , make 100 job in each list and with 1 utilization
# set proper values here 
RUN = 1000   # how many times we run unifast algorithm
JOB_NUMBERS = 100 #task number in each list 
UTILIZATION = 1 #Utilization
uunifasts(RUN, JOB_NUMBERS, UTILIZATION)
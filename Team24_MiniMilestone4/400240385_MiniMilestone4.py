'''
IBEHS 1P10 Mini Milestone 4 Individual File
Name:

Student Number: 400240385

Date: October 11th 2019
'''

##Student ID: 400240385
'''
ADD INDIVIDUAL OBJECTIVES HERE (e.g., objective1(), objective2(), etc.)
'''
import math

#Objective 2: Calculating number of motor revolutions per 90* rotation
def objective2(gearR):
    Rotations = gearR * 0.25
    return Rotations

#Objective 4: Calculating the required time to rotate the finger from open to close(90*)
def objective4(RPM, gearR):
    OutputSpeed = RPM/gearR
    # calculate time in minutes
    timeM = ((90*math.pi)/180) / (OutputSpeed * (2*math.pi))
    timeS = 60 * timeM
    return timeS


##Do not include any function calls - as they will be called in main()




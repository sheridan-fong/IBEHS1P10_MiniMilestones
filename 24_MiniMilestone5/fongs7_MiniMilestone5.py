'''
IBEHS 1P10 Mini Milestone 5 Individual File
Name:

Student Number: 400240385

Date: November 1 2019
'''

##Student ID: 400240385


#Objective 2: Calculate the pitch diameter
def objective2(teethlist, module):
    Pdiameter = []
    length = len(teethlist)
    for i in range(length):
        diameter = teethlist[i]*module
        #adding value to the end of the list
        Pdiameter.append(diameter)
    return Pdiameter

#Objective 3: Caluclate the center distance
def objective3(diameterlist):
    total = 0
    #determines how many gears are in the file
    length = len(diameterlist)
    for i in range(length-1):
        Centredistance = (diameterlist[i]/2) + (diameterlist[i+1]/2)
        print(Centredistance)
        total += Centredistance
    return total



##Do not include any function calls - as they will be called in main()


'''
IBEHS 1P10 Mini Milestone 5 Main File

Team Number: 24

Student 1 Details: Madison Trafford, 400261091


Student 2 Details: Sheridan Fong, 400240385

Date: November 1 2019
'''

import math

##Student ID: 400261091

#Objective 1: Calculate the gear ratio of your gearing mechanism

def objective1(First_level,Second_level):
    #determining output and input gears for the first list
    input1 = First_level[0]
    output1 = First_level[-1]
    #calculating gear ratio for the first list
    gear_ratio1 = output1/input1
    #determining output and input gears for the second list
    input2 = Second_level[0]
    output2 = Second_level[-1]
    #calculating gear ratio for the second list
    gear_ratio2 = output2/input2
    total_gear_ratio = gear_ratio1*gear_ratio2
    #finding then returning the total gear ratio
    return total_gear_ratio

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


##Student ID: 400240385

#Objective 3: Caluclate the center distance
def objective3(diameterlist):
    total = 0
    #determines how many gears are in the file
    length = len(diameterlist)
    for i in range(length-1):
        Centredistance = (diameterlist[i]/2) + (diameterlist[i+1]/2)
        total += Centredistance
    return total

##Student ID: 400261091

#Objective 4:Calculate the x-y position of the forefinger in 10 degree increments from open to closed

def objective4():
    #defining variables
    values_of_theta = [0,10,20,30,40,50,60,70,80,90]
    finger_length = 36
    xy_forefinger_position = []
    #using a for loop to determine x and y coordinates and put them into an empty list
    for number in values_of_theta:
        theta_rad = math.radians (number)
        x_coordinate = round((-finger_length*math.cos(theta_rad)),3)
        y_coordinate = round(finger_length - finger_length*math.sin(theta_rad),3)
        coordinates = [x_coordinate, y_coordinate]
        xy_forefinger_position.append(coordinates)
    #return xy coordinates as multiple lists within a list
    return xy_forefinger_position

##Main Function

def main():
    Listofteeth = [4,6,8,10,15]
    module = 2
    gearlist1 = [24,22,34,12]
    gearlist2 = [24,14,12,32]

    #objective 1: Calculates the gear ratio of your gearing mechanism
    Gear_Ratio = objective1(gearlist1,gearlist2)
    print ("The gear ratio is: \t",round(Gear_Ratio,2))

    #objective 2: finds the pitch diameter of gears using a teeth list and module
    PitchDiameter = objective2(Listofteeth, module)
    print(*PitchDiameter,sep='\n')

    #objective 3: Finds the total centre distance from input to ouput gear
    Centredistance = objective3(PitchDiameter)
    print("The centre distance is: \t",round(Centredistance,2))

    #objective 4: 
    XY_Coordinate = objective4()
    for i in range(10):
        print(XY_Coordinate[i][0],"\t",XY_Coordinate[i][1])

    


#Add function call here (main)
main()

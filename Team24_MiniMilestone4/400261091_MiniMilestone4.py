'''
IBEHS 1P10 Mini Milestone 4 Individual File

Date: October 11, 2019
'''


'''
ADD INDIVIDUAL OBJECTIVES HERE (e.g., objective1(), objective2(), etc.)
'''

#Objective 1: Calculate output speed for a gearing mechanism
def objective1(gear_ratio, input_speed):
    #output speed is being caluclated 
    output_speed = input_speed/gear_ratio
    output_speed = round (output_speed, 2)
    return output_speed

#Objective 3: Calculate the x-y coordinates of the forefinger tip

import math

#angle corresponds to the angle of forefinger rotation
def objective3 (angle):
    angle_rad = math.radians (angle)
    #the next couple of lines calculate the x and y coordinates
    x_coordinate = -36 * math.cos(angle_rad)
    x_coordinate = round (x_coordinate, 2)
    y_coordinate = 36 * math.sin ((math.pi/2) - angle_rad)
    y_coordinate = round (y_coordinate, 2)
    return [x_coordinate, y_coordinate]



    
    


##Do not include any function calls - as they will be called in main()

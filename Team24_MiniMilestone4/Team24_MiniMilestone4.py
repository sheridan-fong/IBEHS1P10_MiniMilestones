'''
IBEHS 1P10 Mini Milestone 4 Main File

Team Number: 24

Student 1 Details (Name, Student Number): Sheridan Fong, 400240385


Student 2 Details (Name, Student Number): Madison Trafford 400261091


Date: October 11th 2019
'''
import math

##Student ID: 400261091

#Objective 1: Calculate output speed for a gearing mechanism
def objective1(gear_ratio, input_speed):
    #output speed is being caluclated 
    output_speed = input_speed/gear_ratio
    output_speed = round (output_speed, 2)
    return output_speed


##Student ID: 400240385

#Objective 2: Calculating number of motor revolutions per 90* rotation
def objective2(gearR):
    Rotations = gearR * 0.25
    return Rotations

##Student ID: 400261091

#Objective 3: Calculate the x-y coordinates of the forefinger tip
#angle corresponds to the angle of forefinger rotation
def objective3 (angle):
    angle_rad = math.radians (angle)
    #the next couple of lines calculate the x and y coordinates
    x_coordinate = -36 * math.cos(angle_rad)
    x_coordinate = round (x_coordinate, 2)
    y_coordinate = 36 * math.sin ((math.pi/2) - angle_rad)
    y_coordinate = round (y_coordinate, 2)
    return [x_coordinate, y_coordinate]

##Student ID: 400240385

#Objective 4: Calculating the required time to rotate the finger from open to close(90*)
def objective4(RPM, gearR):
    OutputSpeed = RPM/gearR
    # calculate time in minutes
    timeM = ((90*math.pi)/180) / (OutputSpeed * (2*math.pi))
    #convert to seconds
    timeS = 60 * timeM
    return timeS


##Main Function
def main():
    GearRatio = 16/3
    print(GearRatio)
    InputSpeed = 144
    GivenAngle = 90
    
    #Objective1: Output Speed
    OutputSpeed = objective1(GearRatio,InputSpeed)
    print("Output speed of gearing mechanism:\t",OutputSpeed,"rpm")
    

    #Objective2: Number of motor revolutions per 90* forefinger rotation
    MotorRev = objective2(GearRatio)
    print("Motor revolutions per 90 degrees:\t",round(MotorRev, 2),"revolutions")

    #Objective 3: Calc. the x and y coordinates
    Coordinates = objective3(GivenAngle)
    print("X-Y Coordinates of the forefinger:\t",Coordinates)

    #Objective 4: Required time for a open to close rotation (finger)
    RotationTime = objective4(InputSpeed, GearRatio)
    print("Rotation time for 90 degrees:\t",round(RotationTime, 2), "s")


#Add function call here (main)
main()

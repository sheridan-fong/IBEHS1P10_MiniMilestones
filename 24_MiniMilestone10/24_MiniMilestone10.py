'''
IBEHS 1P10 Mini Milestone 10 Main File

Team Number: 24

Student 1 Details (Name, Student Number): Madison Trafford, 400261091


Student 2 Details (Name, Student Number): Sheridan Fong, 400240385


Date: January 24th 2020
'''

""" GIVEN Functions """

import time

## This function calculates the gear ratio of your gearing mechanism
## This is a repeat of Mini-Milestone 5 (Wk-8), Objective #1
def calc_GR(gear_list1, gear_list2):
    ratio1 = gear_list1[-1] / gear_list1[0]
    ratio2 = gear_list2[-1] / gear_list2[0]
    gear_ratio = ratio1 * ratio2
    return gear_ratio

## This function calculates the required time (in seconds) to rotate the forefinger 90°
## This is a repeat of Mini-Milestone 4 (Wk-6&7), combining Objective #2 and Objective #4
def calc_elapsed_time(input_speed, gear_ratio):
    FOREFINGER_ROTATION_ANGLE = 90
    num_finger_revolutions = FOREFINGER_ROTATION_ANGLE / 360
    num_motor_revolutions = gear_ratio * num_finger_revolutions
    rev_per_sec = input_speed / 60
    elapsed_time = num_motor_revolutions / rev_per_sec
    return elapsed_time

## This function reads data from a file to a list
## This is a repeat of Mini-Milestone 7 (Wk-11), Objective #3/4
def read_file(filename):
    IO_gears = []
    with open(filename) as gear_list:
        for line in gear_list:
            line = float(line.rstrip())
            IO_gears.append(line)
    return IO_gears






##Student ID: 400261091

def simulate_motion(input_speed, gear_list1, gear_list2):
    gear_ratio = calc_GR(gear_list1, gear_list2)
    time_elapsed = calc_elapsed_time(input_speed, gear_ratio)
    data_list = []
    total_time = 0
    for i in range(7):
        if i%2 == 0:
            data_list.append("OPEN\t"+str(round(total_time,2)))
            total_time += time_elapsed
        else:
            data_list.append("CLOSED\t"+str(round(total_time,2)))
            total_time += time_elapsed
    return (data_list)

##Student ID: 400240385

def find_gear_config(GR, Gear_Number):
    Gear_List = []
    FL_input = 12
    SL_input = 12

    for Gear in Gear_Number:
        FL_output = Gear
        for Gear in Gear_Number:
            SL_output = Gear
            calc_gear_ratio = round(FL_output/FL_input * SL_output/SL_input , 3)
        if calc_gear_ratio == round(GR,3):
            return[FL_input,FL_output,SL_input,SL_output]
            

##Main Function

def main():
    input_speed = 144 #assigned in mini-milestone1
    gear_ratio = 16/3
    FL = [12,20,32]
    SL = [12,12,12,24]
    filename1 = "GearList-1.txt"
    filename2 = "GearRatios-1.txt"
    
    IO_gears = read_file(filename1)
    list_of_GR = read_file(filename2)
    list_of_data = simulate_motion(input_speed,FL,SL)
    timer = calc_elapsed_time(input_speed,gear_ratio)

    
    for i in range(7):
        print(list_of_data[i])
        time.sleep(timer)
     
    for Gear_Ratio in list_of_GR:
        data = find_gear_config(Gear_Ratio,IO_gears)
        print(Gear_Ratio, data)
        
    
    
        

#Add function call here (main)
main()

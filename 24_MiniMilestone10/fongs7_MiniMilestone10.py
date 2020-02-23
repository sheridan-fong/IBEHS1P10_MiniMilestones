'''
IBEHS 1P10 Mini Milestone 10 Individual File
Name: Sheridan Fong

Student Number: 400240385

Date: January 24th 2020
'''

""" GIVEN Functions """
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




##Student ID: 400240385

def find_gear_config(GR, Gear_Number):
    Gear_List = []
    FL_input = 12
    SL_input = 12

    for Gear1 in Gear_Number:
        FL_output = Gear1
        for Gear2 in Gear_Number:
            SL_output = Gear2
            calc_gear_ratio = round(FL_output/FL_input * SL_output/SL_input,3)
            if calc_gear_ratio == round(GR,3):
                print("HI")
                return [FL_input,FL_output,SL_input,SL_output]
       

            
##Do not include any function calls - as they will be called in main()
Gear_List = [12,20,32, 12, 24]
GR = 16/3
data = find_gear_config(GR, Gear_List)
print(data)



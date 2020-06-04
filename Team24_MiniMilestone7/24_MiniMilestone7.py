'''
IBEHS 1P10 Mini Milestone 7 Main File

Team Number: 24


Date: November 22 2019
'''

""" GIVEN Functions """
## This function calculates the gear ratio of your gearing mechanism
## This is a repeat of Mini-Milestone 5 (Wk-8), Objective #1
def calc_GR(gear_list1, gear_list2):
    ratio1 = gear_list1[-1] / gear_list1[0]
    ratio2 = gear_list2[-1] / gear_list2[0]
    gear_ratio = ratio1 * ratio2
    return gear_ratio

## This function calculates the pitch diameter (in mm) for a set of gears
## This is a repeat of Mini-Milestone 5 (Wk-8), Objective #2
def calc_PD(gear_list, module):
    pitch_diameter_list = []
    for gear in gear_list:
        pitch_diameter_list.append(gear * module)
    return pitch_diameter_list

## This function calculates the center distance (in mm) between input and output for a set of gears
## This is a repeat of Mini-Milestone 5 (Wk-8), Objective #3
def calc_CD(pitch_diameter_list):
    center_distance = 0
    for gear in pitch_diameter_list:
        center_distance += gear
    center_distance -= (pitch_diameter_list[0])/2
    center_distance -= (pitch_diameter_list[len(pitch_diameter_list)-1])/2
    return center_distance



def verify_gear_ratio (team_gear_ratio,first_level,second_levelf,second_levelt):
#Calling calc_GR function and calculating the gear ratio
    forefinger = calc_GR(first_level,second_levelf)
    thumb = calc_GR(first_level,second_levelt)
    if forefinger and thumb == team_gear_ratio:
        print ("Both are correct")
    elif forefinger == team_gear_ratio:
        print ("Just the forefinger is correct")
    elif thumb == team_gear_ratio:
        print ("Just the thumb is correct")
    else:
        print ("None are correct")



def verify_center_distance(module, firstlevel, secondlevelF, secondlevelT):
    FIRST_LEVEL_CD = 42
    FOREFINGER_CD = 42
    THUMB_CD = 36

    #Generate Pitch diameter list
    PDfirstlevel = calc_PD(firstlevel, module)
    PDsecondlevelF = calc_PD(secondlevelF, module)
    PDsecondlevelT = calc_PD(secondlevelT, module)

    #Calculate centre distance using pitch diameter
    CDfirstlevel = calc_CD(PDfirstlevel)
    CDsecondlevelF = calc_CD(PDsecondlevelF)
    CDsecondlevelT = calc_CD(PDsecondlevelT)

    print(CDfirstlevel)

    # this code will test to see which CDs match up and which don't
    if CDfirstlevel == FIRST_LEVEL_CD and CDsecondlevelF == FOREFINGER_CD and CDsecondlevelT == THUMB_CD:
        print("all three lists of gears and their desired CDs match up!!")
    elif CDfirstlevel == FIRST_LEVEL_CD and CDsecondlevelF == FOREFINGER_CD:
        print("the first level gears and the forefinger gear CDs match up!")
    elif CDfirstlevel == FIRST_LEVEL_CD and CDsecondlevelT == THUMB_CD:
        print("The first level gears and the thumb gear CDs match up!!")
    elif CDsecondlevelT == THUMB_CD and CDsecondlevelF == FOREFINGER_CD:
        print("The thumb level gears and the forefinger level gear CDs match up!")
    elif CDfirstlevel == FIRST_LEVEL_CD:
        print("Only the first level gear CD match up!")
    elif CDsecondlevelF == FOREFINGER_CD:
        print("Only the forefinger CDs match up!")
    elif CDsecondlevelT == THUMB_CD:
        print("Only the thumb CDs match up!")
    else:
        print("None of the gears match up :(")


def read_file_case1(txtfile):
    #opens text file in read only mode
    file = open(txtfile, "r")
    data = file.read()
    values = data.split()

    file.close()

    gear_list = []
    for value in values:
        gear_list.append(int(value))

    return gear_list

def find_gear():
    #ask user input for the filename
    txtfile = input("Enter the name of the textfile (pls. include .txt)")
    given_gear_list = read_file_case1(txtfile)

    #ask user for a teeth number value
    teethNum = int(input("Enter a number of gear teeth to see if it is in the list"))

    isinlist = False
    
    #for loop to see if the value is in the list
    for gear in given_gear_list:
        if gear == teethNum:
            isinlist = True
            print("Gear tooth is in list")
            
    if isinlist == False:
            print("not in list.... :(")


def read_file_case2(text_file):
#opening and reading a text file
    file = open ('GearData-2.txt','r')
    data = file.read()
    list_of_gears = []
#splitting list into individual strings
    values = data.split()
    file.close
#putting individual strings into an empty list as integers 
    for number in values:
        list_of_gears.append (int(number))
    return list_of_gears

def gear_occurance():
    user_text_file = input ("What is the name of the text file? ")
#call previous function to get the list of gears based on user input
    gearlist = read_file_case2(user_text_file)
    user_gear_teeth = int (input ("What is the number of gear teeth? "))
    counter = 0
#finding number of times the number of gear teeth appears in the list
    for value in gearlist:
        if user_gear_teeth == value:
            counter = counter + 1
    print ("The number of gear teeth appears in the list ",counter," times.")

        



##Main Function

def main():
    module = 1
    gearratio = 5 + 1/3
    First_level = [12,20,32]
    second_forefinger = [12,12,12,24]
    second_thumb = [12,18,24]

    #Madison
    print ("The below work was done by Madison Trafford")

    verify_gear_ratio (gearratio,First_level,second_forefinger,second_thumb)
    gear_occurance()

    #Sheridan
    print("The below work was done by Sheridan Fong")
    
    verify_center_distance(module,First_level, forefinger, thumb)
    find_gear()

    

#Add function call here (main)
main()

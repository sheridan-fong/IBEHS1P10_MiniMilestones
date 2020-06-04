'''
IBEHS 1P10 Mini Milestone 10 Main File

Team Number: 24


Date: January 31st 2020
'''
import math

def read_file(filename):
    data = []
    with open(filename) as inputted_data:
        for line in inputted_data:
            information = float(line)
            data.append(information)
    return data

def average_value(thelist, numberofpoints):
    total = 0

    if len(thelist)< numberofpoints:
        return None
    else:
        for i in range(numberofpoints):
            total += thelist[-1-i]

        average = total/numberofpoints
        return average


def total_above(thelist, threshold):
    totalabove = 0
    lengthoflist = len(thelist)

    for i in range(lengthoflist):
        if thelist[i] > threshold:
            totalabove += 1
    return totalabove

def amplitude(thelist, numberofpoints):
    highestvalue = 0
    lowestvalue = 0
    if len(thelist) < numberofpoints:
        return None
    else:
        for i in range(numberofpoints):
            if i == 0:
                highestvalue = thelist[-1-i]
                lowestvalue = thelist[-1-i]
            elif highestvalue <= thelist[-1-i]:
                highestvalue = thelist[-1-i]
            elif lowestvalue >= thelist[-1-i]:
                lowestvalue = thelist[-1-i]
    ## Calculating the amplitude (difference between highest and lowest point)
    
    amplitude = abs(highestvalue) - abs(lowestvalue)
    absoluteamplitude = abs(amplitude)
    return absoluteamplitude
    
                    
        
            

def main():
    temp_values = []

    ## the read file function
    
    try:
        listname = input("Which list do you want to use? ('don't forget .txt')")
        data_list = read_file(listname)
    except FileNotFoundError:
      print("LoL where's your file!")

    
    for i in data_list:
        temp_values.append(round(i,2))


    ## The average function

    try:
        numberofpoints = int(input("Enter the number of points you want to calculate average for"))
    except ValueError:
        print("ERROR invalid input please run file again and put an integer")
    else:
        average = average_value(temp_values,numberofpoints)

    ## The threshold function

    try:
        threshold_value = int(input("Enter the threshold value"))
        
    except ValueError:
        print("Blah that is not an integer or valid input!!!")
    else:
        choice1 = total_above(temp_values, threshold_value)

    ## the amplitude function
    try:
        pointnumber = int(input("Enter the number of data points you want to use for calculating amplitude"))
    except ValueError:
        print("that doesn't work")
    else: 
        choice2 = amplitude(temp_values, pointnumber)

    ## printing out everything
    try:
        print(data_list,'\t', round(average,2), '\t',round(choice1,2), '\t', round(choice2,2))
    except TypeError:
        print("There as an invalid input along the way, you cannot round NONE type")
   

main()

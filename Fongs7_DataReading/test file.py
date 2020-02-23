def average_value(thelist, numberofpoints):
    total = 0

    if len(thelist)< numberofpoints:
        return None
    else:
        for i in range(numberofpoints):
            total += thelist[-1-i]

        average = total/numberofpoints
        return average

thelist = [1,2,3]
points = "$"
average = average_value(thelist, points)
print(average)

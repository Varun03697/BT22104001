x = int(input("Enter the day:\n"))
y = int(input("Enter the month:\n"))
z = int(input("Enter the year:\n"))
if z % 4 == 0:
    if z % 100 == 0 and z % 400 != 0:
        if y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12:
            if 1 <= x < 31:
                x = x + 1
                y = y
                z = z
            elif x == 31 and y != 12:
                x = 1
                y = y + 1
                z = z
            elif x == 31 and y == 12:
                x = 1
                y = 1
                z = z + 1
            else:
                print("Invalid Input")
        elif y == 4 or y == 6 or y == 9 or y == 11:
            if 1 <= x < 30:
                x = x + 1
                y = y
                z = z
            elif x == 30:
                x = 1
                y = y + 1
                z = z
            else:
                print("Invalid Input")
        elif y == 2:
            if 1 <= x < 28:
                x = x + 1
                y = y
                z = z
            elif x == 28:
                x = 1
                y = y + 1
                z = z
            else:
                print("Invalid Input")
        else:
            print("Invalid Output")
    else:
        if y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12:
            if 1 <= x < 31:
                x = x+1
                y = y
                z = z
            elif x == 31 and y != 12:
                x = 1
                y = y+1
                z = z
            elif x == 31 and y == 12:
                x = 1
                y = 1
                z = z+1
            else:
                print("Invalid Input")
        elif y == 4 or y == 6 or y == 9 or y == 11:
            if 1 <= x < 30:
                x = x + 1
                y = y
                z = z
            elif x == 30:
                x = 1
                y = y + 1
                z = z
            else:
                print("Invalid Input")
        elif y == 2:
            if 1 <= x < 29:
                x = x+1
                y = y
                z = z
            elif x == 29:
                x = 1
                y = y+1
                z = z
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")
elif z % 4 != 0:
    if y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12:
        if 1 <= x < 31:
            x = x + 1
            y = y
            z = z
        elif x == 31 and y != 12:
            x = 1
            y = y + 1
            z = z
        elif x == 31 and y == 12:
            x = 1
            y = 1
            z = z + 1
        else:
            print("Invalid Input")
    elif y == 4 or y == 6 or y == 9 or y == 11:
        if 1 <= x < 30:
            x = x + 1
            y = y
            z = z
        elif x == 30:
            x = 1
            y = y + 1
            z = z
        else:
            print("Invalid Input")
    elif y == 2:
        if 1 <= x < 28:
            x = x + 1
            y = y
            z = z
        elif x == 28:
            x = 1
            y = y + 1
            z = z
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")
if y == 1:
    y = "January"
elif y == 2:
    y = "February"
elif y == 3:
    y = "March"
elif y == 4:
    y = "April"
elif y == 5:
    y = "May"
elif y == 6:
    y = "June"
elif y == 7:
    y = "July"
elif y == 8:
    y = "August"
elif y == 9:
    y = "September"
elif y == 10:
    y = "October"
elif y == 11:
    y = "November"
elif y == 12:
    y = "December"
else:
    print("Invalid Input")

print("Next Date is:",x,"/",y,"/",z)
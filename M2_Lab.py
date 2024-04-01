""" Alexander Schalk
SDEV 220 - Evan Mitchell 
3/20/24
M1 Programming Assignment """

#Tests if student is on the deans list or honor role

while True: #Continue checking students until loop is broken
    try:
        last_name = input("What is the students last name?")
        if last_name == "ZZZ": break;
        else:
            first_name = input("What is the students first name?")
            gpa = float(input("What is the students gpa?"))
            #All data entered
            if gpa >= 3.5: print(f"{first_name} {last_name} is on the Deans List.")
            if gpa >= 3.23: print(f"{first_name} {last_name} is on the Honor Role.")

    except ValueError:
        print("Invalid input, try again! Please enter ZZZ as a last name to exit the loop.") #Input validation
        continue


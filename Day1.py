#The goal of this file is to extract a password for the elves.
#I am given an input with instructions for a lock, a direction and a number.
#The amount of times the lock ends on zero is the password

curNum = 50
password = 0
number = ""
direction = ""
lines = []

#opening the file and breaking each down each line and putting it into array lines
with open('D1_Input.txt', 'r') as file:
    for line in file:
        line.strip()
        lines.append(line)

#breaking apart direction and number for each line in lines
for i in range(0, len(lines)):
    line = lines[i]
    for c in line:
        if c.isalpha():
            direction = c
        elif c.isdigit():
            number += c

    #converting number to integer from string
    inputNum = int(number)

    #if the direction is left, subtract the input number from the current number
    if direction == 'L':
        curNum = curNum - inputNum
        #if the current number is less then 0 (negative) find the remainder to get the actual number on the lock
        if curNum <= 0:
            curNum  = curNum % 100

    #same logic as above
    elif direction == 'R':
        curNum = curNum + inputNum
        if curNum >= 99:
            curNum = curNum % 100

    #resetting number string for each line input
    number = ""

    #if the current number is zero, add to count to find the password
    if curNum == 0:
        password+= 1

print(f"The password is {password}")

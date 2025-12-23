"""
You'll need to find the largest possible joltage each bank can produce. In the above example:

In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
In 818181911112111, the largest joltage you can produce is 92.
The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.
"""
test = ['887654321111119']
testBatteriesIn = ['987654321111111', '811111111111119','234234234234278','818181911112111']
batteriesSTR = [] #list of battery numbers as strings
batteriesINT = [] #list of batterynumbers as integers
batteryList = [] #list of the individual battery as an integer
wholeNumList = []
sum = 0

with open("D3_Input.txt", 'r') as file:
    for line in file:
        line.strip()
        batteriesSTR.append(line)


#setting up lists
for battery in batteriesSTR:
    batteryList = [] #list of the individual battery as an integer
    battery = battery.strip()

    #converting the character to an int and putting it into the list for one battery
    for b in battery:
        intB = int(b)
        batteryList.append(intB)

    batteriesINT.append(batteryList) #list that holds all integer value batteries

for batt in batteriesINT:
    index = 0
    #finding the first large number
    for n in range(0, len(batt) - 1):
        if batt[index] < batt[n]:
            index = n
    
    index2 = index + 1

    #finding the second large number, that occurs after the index of the first
    for k in range(index + 1, len(batt)):
        if batt[index2] < batt[k]:
            index2 = k

    #creating the whole number
    strNum1 = str(batt[index])
    strNum2 = str(batt[index2])
    wholeNumstr = strNum1 + strNum2
    wholeNumInt = int(wholeNumstr)

    #keeping track and creating sum
    wholeNumList.append(wholeNumInt)
    sum += wholeNumInt

print(f"List of the largest nums in each battery{wholeNumList}")
print(f"The sum of these numbers is {sum}")
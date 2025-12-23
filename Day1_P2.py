"""
--- Part Two ---
You're sure that's the right password, but the door won't open. You knock, but nobody answers. You build a snowman while you think.

As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the snow:

"Due to newer security protocols, please use password method 0x434C49434B until further notice."

You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.

Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:

The dial starts by pointing at 50.
The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
The dial is rotated L30 to point at 52.
The dial is rotated R48 to point at 0.
The dial is rotated L5 to point at 95.
The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
The dial is rotated L55 to point at 0.
The dial is rotated L1 to point at 99.
The dial is rotated L99 to point at 0.
The dial is rotated R14 to point at 14.
The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.
In this example, the dial points at 0 three times at the end of a rotation, plus three more times during a rotation. So, in this example, the new password would be 6.

Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!

"""
testList = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
curNum = 50
zeros = 0
lines = []

#opening the file and breaking each down each line and putting it into array lines
with open('D1_Input.txt', 'r') as file:
    for line in file:
        line.strip()
        lines.append(line)

#breaking apart direction and number for each line in lines
for line in testList:
    number = ""
    direction = ""
    for c in line:
        if c.isalpha():
            direction = c
        elif c.isdigit():
            number += c

    #converting number to integer from string
    inputNum = int(number)

    clicks = inputNum // 100 #find the number of complete rotations
    rotations = inputNum % 100 #remainder/incomplete rotations

    zeros += clicks #complete rotations go over zero so add to zeros

    if direction == 'L':
        #check if we cross zero going left
        if curNum > 0 and curNum - rotations <= 0:
            zeros += 1
        curNum = (curNum - rotations) % 100
        
    elif direction == 'R':
        # Check if we cross 0 going right (pass 99 to 0)
        if curNum + rotations >= 100:
            zeros += 1
        curNum = (curNum + rotations) % 100

print(f"The new password is {zeros}")
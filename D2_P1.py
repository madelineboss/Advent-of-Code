invalidNums = []
sum = 0
testRanges = ['11-22', '95-115', '998-1012', '1188511880-1188511890', '222220-222224', '1698522-1698528', '446443-446449', '38593856-38593862']
'''
11-22 has two invalid IDs, 11 and 22.
95-115 has one invalid ID, 99.
998-1012 has one invalid ID, 1010.
1188511880-1188511890 has one invalid ID, 1188511885.
222220-222224 has one invalid ID, 222222.
1698522-1698528 contains no invalid IDs.
446443-446449 has one invalid ID, 446446.
38593856-38593862 has one invalid ID, 38593859.
The rest of the ranges contain no invalid IDs.
'''
with open("D2_Input.txt", 'r') as file:
    input = file.read()

ranges = input.split(',')

for rng in ranges:
    strMin, strMax = rng.split('-')
    intMin = int(strMin)
    intMax = int(strMax)

    for num in range(intMin, intMax + 1):
        strNum = str(num)
        if len(strNum) % 2 == 0:
            halfLen = len(strNum) // 2
            h1 = strNum[0:halfLen]
            h2 = strNum[halfLen:len(strNum)]

            if h1 == h2:
                invalidNums.append(strNum)
                sum += num

print(f"List of invalid numbers {invalidNums}")
print(f"Sum of invalid numbers {sum}")

    
invalidNums = []
sum = 0
test = ['565653-565659']
testRanges = ['11-22', '95-115', '998-1012', '1188511880-1188511890', '222220-222224', '1698522-1698528', '446443-446449', '38593856-38593862', '565653-565659', '824824821-824824827', '2121212118-2121212124']
'''
11-22 still has two invalid IDs, 11 and 22.
95-115 now has two invalid IDs, 99 and 111.
998-1012 now has two invalid IDs, 999 and 1010.
1188511880-1188511890 still has one invalid ID, 1188511885.
222220-222224 still has one invalid ID, 222222.
1698522-1698528 still contains no invalid IDs.
446443-446449 still has one invalid ID, 446446.
38593856-38593862 still has one invalid ID, 38593859.
565653-565659 now has one invalid ID, 565656.
824824821-824824827 now has one invalid ID, 824824824.
2121212118-2121212124 now has one invalid ID, 2121212121.
Adding up all the invalid IDs in this example produces 4174379265.
'''

with open("D2_Input.txt", 'r') as file:
    input = file.read()

ranges = input.split(',')

for rng in ranges:
    strMin, strMax = rng.split('-')
    intMin = int(strMin)
    intMax = int(strMax)
    equivalent = True

    for num in range(intMin, intMax + 1):
        divisibleNums = []
        groups = []
        strNum = str(num)
        lengthNum = len(strNum)

        for n in range(1, lengthNum):
            if lengthNum % n == 0:
                divisibleNums.append(n)

        for number in divisibleNums:
            groups.append([(strNum[i:i+number]) for i in range(0, len(strNum), number)])
        
        for group in groups:
            equivalent = True
            for i in range(0, len(group)):
                if group[0] != group[i]:
                    equivalent = False

            if equivalent == True:
                invalidNums.append(num)
                sum += num
                break
            
print(f"List of invalid numbers {invalidNums}")
print(f"Sum of invalid numbers {sum}")

    


def main():

    validCount = 0
    with open('aocInput.txt', 'r') as file:

        for line in file:
            linelen = len(line)
            minCount = line[0]
            maxCount = line[2]
            letter = line[4]
            lettercount = 0
            password = line[6:linelen]

            for char in password:
                if char == letter:
                    lettercount += 1
                    print(lettercount)

            if lettercount >= int(minCount) and lettercount <= int(maxCount):
                validCount += 1

        print(validCount)

main()
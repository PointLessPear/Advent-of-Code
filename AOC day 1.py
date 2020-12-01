numList = []
def stringsToNumbers(number):
    newNumber = ''.join([x for x in number if x != "[]',"])
    return newNumber

def main():
    with open('aocInput.txt', 'r') as file:
        for num in file:
            number = stringsToNumbers(num.split('\n'))
            numList.append(int(number))

    for i in numList:
        for j in numList:
            for k in numList:
                if i + j + k == 2020:
                    print(f'i = {i} j = {j}, k = {k} Answer = {i*j*k}')

main()
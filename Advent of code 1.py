
file = open('AOC1.txt', 'r').read()
MassItem = file.split('\n')

def getfuel(mass):

        return int(mass / 3) - 2

totalfuel = 0
for mass in MassItem:
     mass = int(mass)
     calcdmass = getfuel(mass)

     totalfuel = totalfuel + calcdmass

print(totalfuel)

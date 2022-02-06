# Imports
from statistics import mean
from os import system


# Declare variables
day = 0
log = []


# Deffinitions
class Employees:
    total = 0
    trapped = 0
    roaming = 0
    ratio = 0
    rate = 0

    def recalculate_vars(self): # Recalculate the variables
        self.total = 2 * (day + 1)
        self.roaming = self.total - self.trapped
        self.ratio = 100 * (self.trapped / self.total)
        self.rate = mean(log)

employees = Employees()


clear = lambda: system("cls")


# Main Program
clear()
print("Welcome to 3008 Employee Counter!") # Greeting

# Initialize the variables
day = int(input("To get things started, what day number is it? ")) # Days
if day < 0: # Error checking
    raise Exception("What the hell! You cant have a negative day!")

employees.trapped = int(input("How many employees are trapped? ")) # Trapped
if employees.trapped < 0: # Error checking
    raise Exception("What the hell! You cant have a negative amount trapped!")
if employees.trapped > 2 * (day + 1):
    raise Exception("What the hell! You cant trap more than the amount in the store!")

for i in range(-1, day):
    log.append(0)

employees.recalculate_vars()
clear()
message = "Here we go!"


while True: # Main loop
    print(f"{message}\n\nIt is day {day}\n{employees.total} Employees Total\n{employees.trapped} Employee(s) Trapped\n{employees.roaming} Employee(s) Roaming\n{round(employees.ratio, 2)}% Trapped\n{log[day]} Employee(s) Trapped/Lost Today\n{round(employees.rate)} Employee(s) trapped per day on average\n")

    inp = input()
    clear()
    if inp == "t":
        if employees.roaming == 0:
            message = "You got them all! How the fuck did you get another one?"
        else:
            employees.trapped += 1
            log[day] += 1
            message = "Nice job!"

    elif inp == "l":
        if employees.trapped == 0:
            message = "You dont got any, how the fuck did you loose one?"
        else:
            employees.trapped -= 1
            log[day] -= 1
            message = "Aw man!"

    elif inp == "d":
        day += 1
        message = "Its a new day!"
        log.append(0)

    elif inp == "g":
        for i in range(len(log)):
            txt = "Day {}: {}"
            print(txt.format(i, log[i]))
            message = "Here you go!"

    elif inp == "e":
        exit()

    employees.recalculate_vars()
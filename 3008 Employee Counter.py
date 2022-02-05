# Imports
from statistics import mean
from os import system


# Deffinitions
def recalculate_vars(): # Recalculate the variables
    global total
    global roaming
    global ratio
    global rate

    total = 2 * (day + 1)
    roaming = total - trapped
    ratio = 100 * (trapped / total)
    rate = mean(log)

clear = lambda: system("cls")

clear()
print("Welcome to 3008 Employee Counter!") # Greeting

# Initialize the variables
day = int(input("To get things started, what day number is it? ")) # Days
if day < 0: # Error checking
    raise Exception("What the hell! You cant have a negative day!")

trapped = int(input("How many employees are trapped? ")) # Trapped
if trapped < 0: # Error checking
    raise Exception("What the hell! You cant have a negative amount trapped!")
if trapped > 2 * (day + 1):
    raise Exception("What the hell! You cant trap more than the amount in the store!")

log = []
for i in range(-1, day):
    log.append(0)

recalculate_vars()
clear()
message = "Here we go!"

while True: # Main loop
    print(f"{message}\n\nIt is day {day}\n{total} Employees Total\n{trapped} Employee(s) Trapped\n{roaming} Employee(s) Roaming\n{round(ratio, 2)}% Trapped\n{log[day]} Employee(s) Trapped/Lost Today\n{round(rate)} Employee(s) trapped per day on average\n")

    inp = input()
    clear()
    if inp == "t":
        if roaming == 0:
            message = "You got them all! How the fuck did you get another one?"
        else:
            trapped += 1
            log[day] += 1
            message = "Nice job!"

    elif inp == "l":
        if trapped == 0:
            message = "You dont got any, how the fuck did you loose one?"
        else:
            trapped -= 1
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

    recalculate_vars()
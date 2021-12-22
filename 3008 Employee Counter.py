#imports
from statistics import mean
from os import system


#function deffinitions
def recalculate_vars(): #recalculate the variables
    global total
    global roaming
    global ratio
    global rate

    total = 2 * (day + 1)
    roaming = total - trapped
    ratio = 100 * (trapped / total)
    rate = mean(log)

clear = lambda: system("cls")

print("Welcome to 3008 Employee Counter!") #greeting

#initialize the variables
day = int(input("To get things started, what day number is it? ")) #days
if day < 0: #error checking
    raise Exception("What the hell! You cant have a negative day!")

trapped = int(input("How many employees are trapped? ")) #trapped
if trapped < 0: #error checking
    raise Exception("What the hell! You cant have a negative amount trapped!")
if trapped > 2 * (day + 1):
    raise Exception("What the hell! You cant trap more than the amount in the store!")

log = []
for i in range(-1, day):
    log.append(0)

recalculate_vars()
clear()
message = "Here we go!"

while True: #main loop
    txt = "{}\n\nIt is day {}\n{} Employees Total\n{} Employee(s) Trapped\n{} Employee(s) Roaming\n{}% Trapped\n{} Employee(s) Trapped/Lost Today\n{} Employee(s) trapped per day on average\n"
    print(txt.format(message, day, total, trapped, roaming, round(ratio, 2), log[day], round(rate)))

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
        message = log

    elif inp == "e":
        exit()

    recalculate_vars()
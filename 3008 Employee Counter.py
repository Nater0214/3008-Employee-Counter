from statistics import mean #imports

def recalculate_vars(): #recalculate the variables
    global total
    global roaming
    global ratio
    global rate

    total = 2 * (day + 1)
    roaming = total - trapped
    ratio = 100 * (trapped / total)
    rate = mean(log)


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

while True: #main loop
    txt = "It is day {}\n{} Employees Total\n{} Employee(s) Trapped\n{} Employee(s) Roaming\n{}% Trapped\n{} Employee(s) Trapped/Lost Today\n{} Employee(s) trapped per day on average\n"
    print(txt.format(day, total, trapped, roaming, round(ratio, 2), log[day], round(rate)))
    inp = input()
    if inp == "t":
        if roaming == 0:
            print("You got them all! How the fuck did you get another one?\n")
        else:
            trapped += 1
            log[day] += 1
            print("Nice job\n")
    elif inp == "l":
        if trapped == 0:
            print("You dont got any, how the fuck did you loose one?\n")
        else:
            trapped -= 1
            log[day] -= 1
            print("Aw man!\n")
    elif inp == "d":
        day += 1
        print("Its a new day!\n")
        log.append(0)
    elif inp == "g":
        print(log)
        print()

    recalculate_vars()
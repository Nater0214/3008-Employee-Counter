def recalculate_vars(): #recalculate the variables
    global total
    global roaming
    global ratio

    total = 2 * (day + 1)
    roaming = total - trapped
    ratio = 100 * (trapped / total)


print("Welcome to 3008 Employee Counter!") #greeting

#initialize
day = int(input("To get things started, what day number is it? ")) #days
if day < 0: #error checking
    raise Exception("What the hell! You cant have a negative day!")

trapped = int(input("How many employees are trapped? ")) #trapped
if trapped < 0: #error checking
    raise Exception("What the hell! You cant have a negative amount trapped!")
if trapped > 2 * (day + 1):
    raise Exception("What the hell! You cant trap more than the amount in the store!")

recalculate_vars()

trends = []
for i in range(-1, day):
    trends.append(0)

while True:
    txt = "{} Employees Total\n{} Employees Trapped\n{} Employees Roaming\n{}% Trapped\n{} Employees Trapped/Lost Today\n"
    print(txt.format(total, trapped, roaming, ratio, trends[day]))
    inp = input()
    if inp == "t":
        if roaming == 0:
            print("You got them all! How the fuck did you get another one?\n")
        else:
            trapped += 1
            trends[day] += 1
            print("Nice job\n")
    elif inp == "l":
        if trapped == 0:
            print("You dont got any, how the fuck did you loose one?\n")
        else:
            trapped -= 1
            trends[day] -= 1
            print("Aw man!\n")
    elif inp == "d":
        day += 1
        print("Its a new day!\n")
        trends.append(0)

    recalculate_vars()
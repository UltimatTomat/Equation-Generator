import random
import time

def get_number():
    myAnswer = input()
    if myAnswer.isnumeric() == False:
        time.sleep(1)
        print("Please enter a number.")
        myAnswer = input()
        if myAnswer.isnumeric() == False:
            time.sleep(1)
            print("That wasn't a number either!")
            myAnswer = input()
            if myAnswer.isnumeric() == False:
                time.sleep(1)
                print("You are pretty dumb!")
    return myAnswer          
    
def easy_equation():
    idiotTest = 0
    print("The equation:")
    while True:
        x = random.randint(2,10)
        y = random.randint(1,50)
        z = random.randint(50,100)
        stepOne = z - y
        stepTwo = stepOne / x
        if stepTwo != int(stepTwo) or stepTwo < 1:
            continue
        time.sleep(1)
        print(x, "x + ", y, " = ", z, sep='')
        time.sleep(1)
        print("What is x?")
        myAnswer = get_number()
        if myAnswer.isnumeric() == False:
            idiotTest = 1
            break
        if int(myAnswer) == (stepTwo):
            time.sleep(1)
            print("That's correct!")
            break
        else:
            time.sleep(1)
            print("Hmm... Try again:")
            myAnswer = get_number()
            if myAnswer.isnumeric() == False:
                idiotTest = 1
                break
            if int(myAnswer) == (stepTwo):
                time.sleep(1)
                print("That's correct!")
                break
            else:
                time.sleep(1)
                print("Unfortunately that was wrong again.")
                time.sleep(1)
                print("The correct answer was ", int(stepTwo), ".", sep='')
                break
    return idiotTest            

def intermediate_equation():
    idiotTest = 0
    print("The equation:")
    while True:
        x = random.randint(2,10)
        y = random.randint(1,9)
        z = random.randint(2,10)
        w = random.randint(50,100)
        stepOne = x * y
        stepTwo = x * z
        stepThree = stepTwo + w
        stepFour = stepThree / stepOne
        if stepFour != int(stepFour) or stepFour < 1:
            continue
        time.sleep(1)
        print(x, "(", y, "x - ", z, ")", " = ", w, sep='')
        time.sleep(1)
        print("What is x?")
        myAnswer = get_number()
        if myAnswer.isnumeric() == False:
                idiotTest = 1
                break
        if int(myAnswer) == (stepFour):
            time.sleep(1)
            print("That's correct!")
            break
        else:
            time.sleep(1)
            print("Hmm... Try again:")
            myAnswer = get_number()
            if myAnswer.isnumeric() == False:
                idiotTest = 1
                break
            if int(myAnswer) == (stepFour):
                time.sleep(1)
                print("That's correct!")
                break
            else:
                time.sleep(1)
                print("Unfortunately that was wrong again.")
                time.sleep(1)
                print("The correct answer was ", int(stepFour), ".", sep='')
                break
    return idiotTest

def hard_equation():
    idiotTest = 0
    print("The equation:")
    while True:
        x = random.randint(2,10)
        y = random.randint(1,10)
        z = random.randint(1,50)
        w = random.randint(1,50)
        v = random.randint(2,10)
        u = random.randint(1,10)
        t = random.randint(1,50)
        stepOne = x * y
        stepTwo = x * z
        stepThree = stepTwo + w
        stepFour = v * u
        stepFive = v * t
        stepSix = stepFive + stepThree
        stepSeven = stepFour - stepOne
        if stepSeven == 0:
            continue
        stepEight = stepSix / stepSeven
        if stepEight != int(stepEight) or stepEight < 1:
            continue
        time.sleep(1)
        print(x, "(", y, "x + ", z, ") + ", w, " = ", v, "(", u, "x - ", t, ")", sep='')
        time.sleep(1)
        print("What is x?")
        myAnswer = get_number()
        if myAnswer.isnumeric() == False:
                idiotTest = 1
                break
        if int(myAnswer) == (stepEight):
            time.sleep(1)
            print("That's correct!")
            break
        else:
            time.sleep(1)
            print("Hmm... Try again:")
            myAnswer = get_number()
            if myAnswer.isnumeric() == False:
                idiotTest = 1
                break
            if int(myAnswer) == (stepEight):
                time.sleep(1)
                print("That's correct!")
                break
            else:
                time.sleep(1)
                print("Unfortunately that was wrong again.")
                time.sleep(1)
                print("The correct answer was ", int(stepEight), ".", sep='')
                break
    return idiotTest

print("Welcome!")
time.sleep(1)
print("What level of difficulty do you want?")

while True:
    diLevel = int(input())
    if diLevel == 1:
        time.sleep(1)
        idiot = easy_equation()
        if idiot == 1:
            break
        time.sleep(1)
        print("Again?")
        playAgain = input()
        if playAgain.lower() == "yes":
            time.sleep(1)
            print("What level of difficulty do you want?")
            continue
        elif playAgain.lower() == "no":
            break
        else:
            time.sleep(1)
            print("Please enter yes or no.")
            playAgain = input()
            if playAgain.lower() == "yes":
                time.sleep(1)
                print("What level of difficulty do you want?")
                continue
            elif playAgain.lower() == "no":
                break
            else:
                time.sleep(1)
                print("I'm gonna take that as a no.")
                break
    elif diLevel == 2:
        time.sleep(1)
        idiot = intermediate_equation()
        if idiot == 1:
            break
        time.sleep(1)
        print("Again?")
        playAgain = input()
        if playAgain.lower() == "yes":
            time.sleep(1)
            print("What level of difficulty do you want?")
            continue
        elif playAgain.lower() == "no":
            break
        else:
            time.sleep(1)
            print("Please enter yes or no.")
            playAgain = input()
            if playAgain.lower() == "yes":
                time.sleep(1)
                print("What level of difficulty do you want?")
                continue
            elif playAgain.lower() == "no":
                break
            else:
                time.sleep(1)
                print("I'm gonna take that as a no.")
                break
    elif diLevel == 3:
        time.sleep(1)
        idiot = hard_equation()
        if idiot == 1:
            break
        time.sleep(1)
        print("Again?")
        playAgain = input()
        if playAgain.lower() == "yes":
            time.sleep(1)
            print("What level of difficulty do you want?")
            continue
        elif playAgain.lower() == "no":
            break
        else:
            time.sleep(1)
            print("Please enter yes or no.")
            playAgain = input()
            if playAgain.lower() == "yes":
                time.sleep(1)
                print("What level of difficulty do you want?")
                continue
            elif playAgain.lower() == "no":
                break
            else:
                time.sleep(1)
                print("I'm gonna take that as a no.")
                break
    else:
        time.sleep(1)
        print("Please enter 1, 2 or 3.")
        time.sleep(1)

time.sleep(1)
print("Bye...")
time.sleep(1)
from random import randint

def readUserNumber():
    intNumber = -1
    while intNumber < 0:
        userInput = input("Quel est votre nombre ? ")
        try: 
            intNumber = int(userInput)
        except:
            print("Ce n'est pas un nombre")
    return intNumber

lowerBound = 0
higherBound = 100

numberToGuess = randint(lowerBound, higherBound)
guessedNumber = -1

while numberToGuess != guessedNumber :
        
    guessedNumber = readUserNumber()

    if guessedNumber == numberToGuess:
        print("Félicitation !")
    elif guessedNumber > numberToGuess:
        print("Trop grand...")
    elif guessedNumber < numberToGuess:
        print("Top petit...")


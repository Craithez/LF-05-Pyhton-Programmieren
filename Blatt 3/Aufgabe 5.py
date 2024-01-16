import random

num = random.randint(0, 100)
guess = None
counter = 0
while guess != num:
    guess = input("Errrate die Zahle zwischen 0 und 100: ")
    guess = int(guess)

    if guess == num:
        print("Gewonnen!")
        print("Versuche:",counter)
        break
    elif guess < num:
        print("Leider falsch, Zahl ist größer.")
        counter = counter + 1
        print("Versuche:",counter)

    else:
        print("Leider falsch, Zahl ist kleiner.")
        counter = counter + 1
        print("Versuche:",counter)
    

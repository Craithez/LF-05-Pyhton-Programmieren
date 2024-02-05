unten = int(input("Bitte unteres Intervall eingeben: "))
oben = int(input("Bitte oberes Intervall eingeben: "))

print("Primezahlen zwischen ", unten, "und", oben, "sind:")

for num in range(unten, oben + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
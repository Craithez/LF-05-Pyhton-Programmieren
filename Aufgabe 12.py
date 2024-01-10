#Fall b
print("Es gibt zwei Charaktere A und B, bitte nur mit r oder s antworten.")
print("Eine Frau und ein Mann werden befragt, der Mann antwortet: Wir sind beide Schurken.")
print("Was ist die Frau, was ist der Mann?")
frau = input("Frau: ")
mann = input("Mann: ")
ritter = "r"
schurke = "s"
if((frau == ritter)&(mann == schurke)):print("Stimmt!")
else :print("Falsch!")

#Fall c
print("Es gibt zwei Charaktere A und B, bitte nur mit r oder s antworten.")
print("Eine Frau und ein Mann werden befragt, der Mann antwortet: Mindestens einer von uns ist Schurke.")
print("Was ist die Frau, was ist der Mann?")
frau = input("Frau: ")
mann = input("Mann: ")
ritter = "r"
schurke = "s"
if((frau == schurke)&(mann == ritter)):print("Stimmt!")
else :print("Falsch!")

code = int(input("Code eingeben: "))
if code == 200:
    print(f"OK")
elif code == 201:
    print(f"Accepted")
elif code == 400:
    print(f"Bad Request")
elif code == 401:
    print(f"Connection Refuseder")
elif code == 403:
    print(f"Connection Refuseder")
elif code == 502:
    print(f"Bad Gateway")
else:
    print(f"Kein gültiger Code!")


#code = int(input("Code eingeben: "))
#if code == 200:
#    print(f"OK")
#elif code == 201:
#    print(f"Accepted")
#elif code == 400:
#    print(f"Bad Request")
#elif code == 401:
#    print(f"Connection Refuseder")
#elif code == 403:
#    print(f"Connection Refuseder")
#elif code == 502:
#    print(f"Bad Gateway")
#else:
#    print(f"Kein gültiger Code!")


def http_status_message_match_case(status_code):
    try:
        status_code = int(status_code)
        match status_code:
            case 200:
                print("OK")
            case 201:
                print("Accepted")
            case 400:
                print("Bad Request")
            case 401:
                print("Connection Refused")
            case 502:
                print("Gateway")
            case _:
                print("Ungueltiger HTTP-Satutscode")
    except ValueError:
        print("Ungueltige Eingabe")
user_input = input("Geben sie ihren HTTP Fehler Code ein.")
http_status_message_match_case(user_input)
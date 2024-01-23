import argparse
import psutil
import time

def get_cpu_load():
    return psutil.cpu_percent(interval=1)

def check_cpu_usage(cpu_load):
    if cpu_load < 70:
        return "OK", f"CPU Last beträgt {cpu_load}%. Alles in Ordnung."
    elif cpu_load >= 70 and cpu_load < 90:
        return "WARNING", f"CPU Last beträgt {cpu_load}%! Vorsicht!"
    else:
        return "CRITICAL", f"CPU Last beträgt {cpu_load}%! kritisch und so!!111!"
    
def display_result(status, message):
    print(f"Status: {status}\n{message}")

def main():
    parser = argparse.ArgumentParser(description='Überprüfe die CPU-Auslastung und gib eine Meldung aus.')
    args = parser.parse_args()

    try:
        while True:
            cpu_load = get_cpu_load()
            status, message = check_cpu_usage(cpu_load)
            display_result(status, message)

            time.sleep(10)  # Warte 10 Sekunden, bevor die nächste Überprüfung durchgeführt wird

    except KeyboardInterrupt:
        print("\nProgramm beendet.")

if __name__ == "__main__":
    main()
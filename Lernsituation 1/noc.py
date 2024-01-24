import argparse
import psutil
import time

def get_cpu_load():
    return psutil.cpu_percent(interval=1)

def check_cpu_usage(cpu_load, warning_threshold, critical_threshold):
    if cpu_load < warning_threshold:
        return "OK", f"CPU Last beträgt {cpu_load}%. Alles in Ordnung."
    elif warning_threshold <= cpu_load < critical_threshold:
        return "WARNING", f"CPU Last beträgt {cpu_load}%! Vorsicht!"
    else:
        return "CRITICAL", f"CPU Last beträgt {cpu_load}%! Kritisch und so!!111!"

def display_result(status, message):
    print(f"Status: {status}\n{message}")

def main():
    parser = argparse.ArgumentParser(description='Überprüfe die CPU-Auslastung und gib eine Meldung aus.')
    parser.add_argument('-w', '--warning', nargs=3, type=float, help='Schwellenwerte für Warnungen (z. B. -w 0.9 0.8 0.7)')
    parser.add_argument('-c', '--critical', nargs=3, type=float, help='Schwellenwerte für Kritikalität (z. B. -c 0.95 0.85 0.75)')
    args = parser.parse_args()

    try:
        while True:
            cpu_load = get_cpu_load()
            warning_threshold = args.warning[0]
            critical_threshold = args.critical[0]
            status, message = check_cpu_usage(cpu_load, warning_threshold, critical_threshold)
            display_result(status, message)

            time.sleep(10)  # Erneuter Aufruf nach 10 Sekunden
    except KeyboardInterrupt:
        print("\nProgramm beendet.")
    except Exception as e:
        print(f"Fehler aufgetreten: {e}")

if __name__ == "__main__":
    main()
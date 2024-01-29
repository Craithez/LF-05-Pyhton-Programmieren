# Für den ganzen Bums braucht man ein Linux OS oder zumindest Linux Bash+WLS aufm Windows und Visual Studios.
# Anschließend nur noch via cmd (mit Admin) ins Verzeichniss navigieren und mit "python load.py -w 70 80 90 -c 85 95 99 aufrufen".
import argparse
import psutil
import time

def get_cpu_load():
    return psutil.cpu_percent(interval=1)

def check_cpu_usage(cpu_load, warning_threshold, critical_threshold):
    if cpu_load < warning_threshold:
        return "OK", f"CPU Last betragt {cpu_load}%. Alles in Ordnung."
    elif warning_threshold <= cpu_load < critical_threshold:
        return "WARNING", f"CPU Last betraegt {cpu_load}%! Vorsicht!"
    else:
        return "CRITICAL", f"CPU Last betraegt {cpu_load}%! Kritisch und so!!111!"

def display_result(status, message):
    print(f"Status: {status}\n{message}")

def main():
    parser = argparse.ArgumentParser(description='Überprüfe die CPU-Auslastung und gib eine Meldung aus.')
    parser.add_argument('-w', '--warning', nargs=3, type=float, help='Schwellenwerte für Warnungen (z. B. -w 0.9 0.8 0.7)')      # Stellt sich er das nur 3 Eingaben akzeptiert werden.
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
        print(f"Fehler aufgetreten: {e}")   # Greift auf Exception Class zu und wirft Fehler aus,  e für Textbasierte Nachricht z.B 420

if __name__ == "__main__":
    main()


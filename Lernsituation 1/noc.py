import argparse
import psutil
import time

def get_cpu_load():
    return psutil.cpu_percent(interval=1)

def check_cpu_usage(threshold):
    cpu_usage = psutil.cpu_percent(interval=1)  # Aktuelle CPU-Auslastung in Prozent
    print(f"Aktuelle CPU-Auslastung: {cpu_usage}%")

    if cpu_usage > threshold:
        print("Kritische CPU-Auslastung erreicht! Benachrichtigung erforderlich.")

# Beispielaufruf mit einem Schwellenwert von 80%
check_cpu_usage(80)
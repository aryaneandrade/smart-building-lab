#!/usr/bin/env python3

import random
import subprocess
import time
from datetime import datetime

ZABBIX_SERVER = "127.0.0.1"
HOSTNAME = "HW-GERAL-01"
INTERVAL = 5  # segundos

energy_accumulator = {
    "A": 0.0,
    "B": 0.0,
    "C": 0.0,
}


def send(key, value):
    command = [
        "zabbix_sender",
        "-z", ZABBIX_SERVER,
        "-s", HOSTNAME,
        "-k", key,
        "-o", str(value)
    ]

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        print(f"[ERRO] {key}: {result.stderr.strip()}")


def phase_data(phase):
    voltage = round(random.uniform(218, 223), 2)
    current = round(random.uniform(3, 8), 2)
    power_factor = round(random.uniform(0.90, 0.98), 2)

    apparent_power = round(voltage * current, 2)
    active_power = round(apparent_power * power_factor, 2)
    reactive_power = round(((apparent_power ** 2) - (active_power ** 2)) ** 0.5, 2)

    # Energia acumulativa:
    # kWh = (W * horas) / 1000
    interval_hours = INTERVAL / 3600
    energy_accumulator[phase] += (active_power * interval_hours) / 1000
    energy = round(energy_accumulator[phase], 5)

    return {
        f"smartbuilding.phase[voltage,{phase}]": voltage,
        f"smartbuilding.phase[current,{phase}]": current,
        f"smartbuilding.phase[active_power,{phase}]": active_power,
        f"smartbuilding.phase[reactive_power,{phase}]": reactive_power,
        f"smartbuilding.phase[apparent_power,{phase}]": apparent_power,
        f"smartbuilding.phase[power_factor,{phase}]": power_factor,
        f"smartbuilding.phase[energy,{phase}]": energy,
    }


def grid_data():
    return {
        "smartbuilding.grid[frequency]": round(random.uniform(59.95, 60.05), 2),
        "smartbuilding.surge[magnitude]": 0
    }


def main():
    print("=" * 60)
    print("SMART BUILDING - TELEMETRY SIMULATOR")
    print("=" * 60)
    print(f"Servidor Zabbix : {ZABBIX_SERVER}")
    print(f"Host            : {HOSTNAME}")
    print(f"Intervalo       : {INTERVAL}s")
    print("Energia         : acumulativa por fase")
    print("=" * 60)

    while True:
        payload = {}

        payload.update(phase_data("A"))
        payload.update(phase_data("B"))
        payload.update(phase_data("C"))
        payload.update(grid_data())

        for key, value in payload.items():
            send(key, value)

        print(
            f"[{datetime.now().strftime('%H:%M:%S')}] "
            f"23 métricas enviadas | "
            f"Energia A={energy_accumulator['A']:.5f} kWh, "
            f"B={energy_accumulator['B']:.5f} kWh, "
            f"C={energy_accumulator['C']:.5f} kWh"
        )

        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()


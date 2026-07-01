#!/usr/bin/env python3

import subprocess
from datetime import datetime

ZABBIX_SERVER = "127.0.0.1"
HOSTNAME = "HW-GERAL-01"


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

    print(f"[{datetime.now().strftime('%H:%M:%S')}] {key} = {value}")

    if result.returncode != 0:
        print("[ERRO]", result.stderr.strip())


print("=" * 60)
print("SMART BUILDING - SIMULADOR DE PROBLEMAS ATIVOS")
print("=" * 60)

print("\n[PROBLEMA 1] Corrente alta na Fase B")
send("smartbuilding.phase[current,B]", 14.5)

print("\n[PROBLEMA 2] Tensão baixa na Fase A")
send("smartbuilding.phase[voltage,A]", 180)

print("\n[PROBLEMA 3] Tensão alta na Fase C")
send("smartbuilding.phase[voltage,C]", 250)

print("\n[PROBLEMA 4] Fator de potência baixo na Fase A")
send("smartbuilding.phase[power_factor,A]", 0.75)

print("\n[PROBLEMA 5] Frequência abaixo do permitido")
send("smartbuilding.grid[frequency]", 58.9)

print("\n[PROBLEMA 6] Surto elétrico detectado")
send("smartbuilding.surge[magnitude]", 1450)

print("\nProblemas enviados. As triggers devem permanecer ativas no Zabbix.")


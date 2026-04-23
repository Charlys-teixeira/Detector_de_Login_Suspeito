from dados import tentativas
from detector import detectar_ataques
import datetime
import json


print("=" * 50)
print(f"Scan executado em: {datetime.datetime.now()}")
print("=" * 50)

alertas = detectar_ataques(tentativas)

if not alertas:
    print("✅ Nenhuma atividade suspeita detectada")
else:
    print("🚨 ALERTAS DE SEGURANÇA:\n")

    for alerta in alertas:
        if "ip" in alerta:
            print(
                f"[IP] {alerta['ip']} → {alerta['tipo']} | Tentativas: {alerta['tentativas']} | Tempo: {alerta['tempo']}s"
            )

        if "usuario" in alerta:
            print(
                f"[USUÁRIO] {alerta['usuario']} → {alerta['tipo']} | Tentativas: {alerta['tentativas']} | Tempo: {alerta['tempo']}s"
            )

with open("alertas.json", "w") as f:
    json.dump(alertas, f, indent=4)

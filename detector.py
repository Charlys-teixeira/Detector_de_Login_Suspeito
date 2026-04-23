def detectar_ataques(tentativas):
    falhas_por_ip = {}
    falhas_por_usuario = {}
    alertas = []

    # Agrupar falhas
    for tentativa in tentativas:
        if tentativa["status"] == "fail":

            # IP
            ip = tentativa["ip"]
            if ip not in falhas_por_ip:
                falhas_por_ip[ip] = []
            falhas_por_ip[ip].append(tentativa)

            # USUÁRIO
            usuario = tentativa["usuario"]
            if usuario not in falhas_por_usuario:
                falhas_por_usuario[usuario] = []
            falhas_por_usuario[usuario].append(tentativa)

    # Análise por IP
    for ip, falhas in falhas_por_ip.items():
        if len(falhas) >= 5:
            tempo_total = falhas[-1]["tempo"] - falhas[0]["tempo"]

            if tempo_total <= 30:
                alerta = {
                    "ip": ip,
                    "tipo": "brute_force",
                    "tentativas": len(falhas),
                    "tempo": tempo_total,
                }
                alertas.append(alerta)

    # Análise por USUÁRIO
    for usuario, falhas in falhas_por_usuario.items():
        if len(falhas) >= 5:
            tempo_total = falhas[-1]["tempo"] - falhas[0]["tempo"]

        if tempo_total <= 30:
            ips_unicos = set(f["ip"] for f in falhas)

            if len(ips_unicos) > 1:
                tipo = "credential_stuffing"
            else:
                tipo = "brute_force_usuario"

            alerta = {
                "usuario": usuario,
                "tipo": tipo,
                "tentativas": len(falhas),
                "tempo": tempo_total,
                "ips_unicos": len(ips_unicos),
            }

            alertas.append(alerta)
    return alertas

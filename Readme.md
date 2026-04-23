# 🔐 Detector de Login Suspeito

Projeto em Python para detecção de atividades suspeitas em tentativas de login, simulando comportamentos comuns de ataques em sistemas reais.

## 🚀 Funcionalidades

- Detecção de ataques de força bruta (Brute Force)
- Detecção de Credential Stuffing
- Análise baseada em tempo (janela de 30 segundos)
- Agrupamento por IP e por usuário
- Geração de alertas estruturados
- Exportação de alertas em JSON

## 🧠 Lógica de Detecção

O sistema analisa tentativas de login e identifica padrões suspeitos:

- **Brute Force (IP)**: múltiplas falhas vindas do mesmo IP em curto período
- **Brute Force (Usuário)**: múltiplas falhas em um único usuário
- **Credential Stuffing**: múltiplos IPs tentando acessar o mesmo usuário

## 📂 Estrutura do Projeto

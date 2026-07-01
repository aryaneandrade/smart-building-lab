# SMART BUILDING LAB

Proof of Concept (PoC) para monitoramento elétrico utilizando Zabbix e Grafana.

---

## Objetivo

Validar uma plataforma de monitoramento elétrico utilizando dados simulados enviados por um script Python, permitindo acompanhar métricas em tempo real, histórico e alertas.

---

## Tecnologias

- Docker
- PostgreSQL
- Zabbix 7.4
- Grafana 12
- Python

---

## Arquitetura

![Arquitetura](images/arquitetura.png)

---

## Dashboards

![visao-geral](images/visao-geral.png)

![telemetria](images/telemetria.png)

---

## Estrutura do Projeto
## Estrutura do Projeto

```text
smart-building-lab/
│
├── docker/
│   └── docker-compose.yml          # Ambiente Docker da PoC
│
├── python/
│   ├── smartbuilding.py            # Simulador de telemetria
│   ├── smartbuilding_events.py     # Simulador de eventos e alertas
│   └── requirements.txt            # Dependências do projeto
│
├── zabbix/
│   ├── template/
│   │   └── Template_Smart_Building.yaml
│   └── screenshots/
│
├── grafana/
│   ├── dashboards/
│   │   ├── dashboard-visao-geral.json
│   │   └── dashboard-telemetria.json
│   │
│   ├── business-text/
│   │   ├── cabecalho.html
│   │   ├── frequencia.html
│   │   ├── consumo.html
│   │   ├── fator-potencia.html
│   │   ├── surto.html
│   │   ├── fase-a.html
│   │   ├── fase-b.html
│   │   └── fase-c.html
│   │
│   └── screenshots/
│
├── docs/
│   └── SMART_BUILDING_PoC.pdf
│
├── images/
│   ├── arquitetura.png
│   ├── visao-geral.png
│   └── telemetria.png
│
├── README.md
└── .gitignore
```

### Descrição das Pastas

| Pasta | Descrição |
|--------|-----------|
| **docker/** | Arquivos para implantação do ambiente utilizando Docker Compose. |
| **python/** | Scripts responsáveis pela simulação das grandezas elétricas e eventos enviados ao Zabbix. |
| **zabbix/** | Template exportado do Zabbix e capturas de tela da configuração. |
| **grafana/** | Dashboards exportados em JSON, códigos HTML dos painéis Business Text e capturas de tela. |
| **docs/** | Documentação técnica da Prova de Conceito. |
| **images/** | Imagens utilizadas no README e na documentação do projeto. |

---

## Como executar

docker compose up -d

---

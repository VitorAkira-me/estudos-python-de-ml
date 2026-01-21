# Mini Lake (Bronze / Silver / Gold)

Pipeline inicial: **Clima** via Open-Meteo.

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Rodar (primeiro conector)
```bash
python -m mini_lake.connectors.weather_open_meteo
```

## Próximos passos (Sprint atual)
- Padronizar logging (JSON logs)
- Criar camada Bronze (salvar JSON bruto em `data/bronze/`)
- Criar estado incremental (checkpoint por dia/cidade)

# Skill: Bootstrap HydraClone

## Objetivo
Dejar el entorno listo (venv, deps, .env) para ejecutar HydraClone sin dependencias externas.

## Pasos
1) Crear y activar venv:
```
python3 -m venv venv
source venv/bin/activate
```
2) Instalar dependencias:
```
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```
3) Configurar entorno:
```
cp .env.example .env    # editar tokens opcional
```

## Salidas esperadas
- venv/ creado.
- `.env` presente.

## Ejemplo de uso
```
bash -lc "cd /home/dev/leo/hydra-clone && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && cp .env.example .env"
```

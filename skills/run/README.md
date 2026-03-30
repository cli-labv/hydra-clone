# Skill: Ejecutar HydraClone

## Objetivo
Levantar la CLI, autenticar y generar clones/reportes dentro del proyecto.

## Pasos
1) Activar entorno:
```
source venv/bin/activate
```
2) Ejecutar CLI:
```
bash scripts/run.sh
# o
python3 src/main.py
```
3) Ingresar URLs (http/https/ssh). Detecta plataformas automáticamente.
4) Credenciales:
   - Usa `.env` si existen tokens.
   - Si no, las solicita y guarda en `config/.credentials/credentials.json` (chmod 600).

## Salidas esperadas
- Repos: `clones/FECHA_HORA/<plataforma>/<repo>`
- Reporte: `reports/clone-report_YYYY-MM-DD_HH-MM-SS.md`

## Ejemplo de uso
```
bash -lc "cd /home/dev/leo/hydra-clone && source venv/bin/activate && python3 src/main.py"
```

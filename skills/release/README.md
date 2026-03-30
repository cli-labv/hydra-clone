# Skill: Release HydraClone

## Objetivo
Publicar una versión estable con checklist reproducible.

## Pasos
1) Bump de versión en `src/config.py` (y README si aplica).
2) Changelog: actualizar `docs/CAMBIOS.md` con fecha y cambios.
3) Docs: asegurar `INDEX.md`, `QUICKSTART.md`, `USAGE.md` reflejan rutas actuales (clones/FECHA_HORA, reports/, config/.credentials/).
4) Dependencias: revisar/actualizar `requirements.txt`; recrear venv si cambia.
5) Smoke manual:
```
source venv/bin/activate
python3 src/main.py   # clonar 1 repo público
```
   Verifica que cree `clones/TS/...` y `reports/clone-report_*.md`.
6) Gitignore: confirmar `config/.credentials/` y `clones/` siguen ignorados.
7) Tag (si aplica):
```
git tag vX.Y.Z
git push --tags
```

## Ejemplo de checklist en un comando
```
bash -lc "cd /home/dev/leo/hydra-clone && source venv/bin/activate && python3 - <<'PY'\nprint('Smoke: ejecutar main.py y validar clones/reportes dentro del repo')\nPY"
```

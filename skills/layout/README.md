# Skill: Layout HydraClone

## Objetivo
Verificar que la estructura y rutas generadas estén dentro del proyecto.

## Estructura esperada
```
hydra-clone/
├─ src/            # main.py, config.py
├─ modules/        # auth, clone, reports, animations...
├─ scripts/        # install.sh, run.sh, test.sh
├─ docs/           # documentación
├─ clones/TS/      # salida de clonaciones (runtime)
├─ reports/        # reportes MD (runtime)
├─ config/.credentials/ # credenciales JSON (runtime, gitignored)
├─ .env / .env.example
├─ requirements.txt
└─ venv/ (local)
```

## Checks rápidos
- `config/.credentials/` existe o se crea en runtime y está gitignored.
- `clones/` y `reports/` se crean dentro del repo (no en `~/`).

## Ejemplo de validación
```
bash -lc "cd /home/dev/leo/hydra-clone && ls src modules scripts docs clones reports config/.credentials"
```

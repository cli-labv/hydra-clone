# Skill: Upgrade/Migración HydraClone

## Objetivo
Migrar desde v1.x (clones y credenciales fuera del repo) a la estructura actual.

## Pasos
1) Mover clones previos (si existen):
```
mkdir -p clones/TS/github
cp -r ~/clones/github/* clones/TS/github/    # ajustar TS y plataforma
```
2) Migrar credenciales previas:
```
mkdir -p config/.credentials
cp ~/.hydra-clone/credentials.json config/.credentials/  # opcional
chmod 600 config/.credentials/credentials.json
```
3) Asegurar ignores:
- `config/.credentials/`
- `clones/`

4) Revisar docs: rutas internas (clones/FECHA_HORA, reports/, config/.credentials/).

## Ejemplo de uso
```
bash -lc "cd /home/dev/leo/hydra-clone && mkdir -p clones/2026-03-30_00-00-00/github && cp -r ~/clones/github/* clones/2026-03-30_00-00-00/github/ 2>/dev/null || true"
```

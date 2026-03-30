# HydraClone Skills Catalog

Estructura según “agent skills”: cada skill vive en su carpeta con un `README.md` que define objetivo, pasos y ejemplo de uso (comandos listos para ejecutar).

Skills incluidas:
- `bootstrap/` — preparar entorno y dependencias.
- `layout/` — validar estructura de proyecto y rutas generadas.
- `run/` — ejecutar HydraClone con credenciales y salidas esperadas.
- `release/` — checklist para cortes de versión.
- `upgrade/` — migrar desde v1.x (rutas antiguas) a la versión actual.

Uso general:
```
cd skills/<skill>
cat README.md
```

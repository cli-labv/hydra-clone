# 📁 Scripts Directory

Scripts de automatización para HydraClone.

## Archivos

### `install.sh`
Script de instalación y configuración inicial del proyecto.

**Qué hace:**
- ✅ Verifica Python 3 y Git
- ✅ Crea entorno virtual Python
- ✅ Instala dependencias
- ✅ Copia `.env.example` a `.env`

**Cómo usar:**
```bash
bash scripts/install.sh
# O desde la raíz:
bash install.sh
```

### `run.sh`
Script para ejecutar HydraClone.

**Qué hace:**
- ✅ Verifica entorno virtual
- ✅ Activa venv
- ✅ Ejecuta CLI principal

**Cómo usar:**
```bash
bash scripts/run.sh
# O desde la raíz:
bash run.sh
```

### `test.sh`
Script para ejecutar pruebas.

**Cómo usar:**
```bash
bash scripts/test.sh
```

## Estructura

```
scripts/
├── install.sh    → Instalación
├── run.sh        → Ejecución
└── test.sh       → Pruebas
```

## Wrappers en raíz

Para mayor comodidad, existen wrappers en la raíz del proyecto:
- `install.sh` → Llama a `scripts/install.sh`
- `run.sh` → Llama a `scripts/run.sh`

Puedes usar cualquiera indistintamente.

## Agregar más scripts

Para agregar nuevos scripts:

1. Crea el script en esta carpeta: `scripts/nuevo-script.sh`
2. Hazlo ejecutable: `chmod +x scripts/nuevo-script.sh`
3. Opcionalmente, crea un wrapper en raíz si es necesario

Ejemplo:
```bash
echo '#!/bin/bash' > scripts/deploy.sh
chmod +x scripts/deploy.sh
echo 'exec bash "$(dirname "$0")/../scripts/deploy.sh" "$@"' > deploy.sh
chmod +x deploy.sh
```

---

**Versión:** 2.0.0  
**Última actualización:** 2026-03-25

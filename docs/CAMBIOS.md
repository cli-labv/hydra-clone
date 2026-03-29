# 📝 Changelog - HydraClone v2.0.0

## 🔄 Restructuración Principal (v2.0.0)

### 📁 Cambios en la Estructura del Proyecto

#### Antes (v1.0.0):
```
hydra-clone/
├── main.py
├── config.py
├── auth.py
├── clone.py
├── reports.py
├── animations.py
├── hydra_banner.py
├── hydra_progress.py
├── *.md (documentación suelta)
├── config/
├── clones/
├── reports/
└── venv/
```

#### Después (v2.0.0):
```
hydra-clone/
├── src/
│   ├── main.py (CLI principal)
│   ├── config.py (configuración)
│   └── __init__.py
├── modules/
│   ├── auth.py (autenticación)
│   ├── clone.py (clonación)
│   ├── reports.py (generación de reportes)
│   ├── hydra_banner.py (banner animado)
│   ├── hydra_progress.py (progreso/estadísticas)
│   └── __init__.py
├── docs/
│   ├── CAMBIOS.md
│   ├── INDEX.md
│   ├── PROYECTO.txt
│   ├── QUICKSTART.md
│   ├── USAGE.md
│   ├── EXAMPLE_URLS.md
│   └── README_OLD.md
├── clones/
│   └── YYYY-MM-DD_HH-MM-SS/ (nueva: timestamp por bloque)
│       ├── github/
│       ├── gitlab/
│       └── bitbucket/
├── reports/
├── config/
├── README.md (raíz)
├── .env (nuevo)
├── .env.example (nuevo)
├── hydra-clone.py (wrapper)
├── run.sh (actualizado)
├── install.sh (actualizado)
├── requirements.txt
└── venv/
```

### 🔐 Soporte para Variables de Entorno

#### Nuevos archivos:
- **.env** - Archivo de variables de entorno (gitignored)
- **.env.example** - Template de configuración

#### Nuevas variables de entorno:
```bash
GITHUB_TOKEN=                 # Token de GitHub
GITLAB_TOKEN=                 # Token de GitLab
BITBUCKET_TOKEN=              # Token de Bitbucket
BITBUCKET_USER=               # Usuario de Bitbucket
```

#### Funcionalidad:
- Si los tokens están en `.env`, se usan automáticamente
- Si no existen o son inválidos, se piden en la interfaz
- Se mantiene la funcionalidad de auth interactiva

### 📂 Cambios en Directorios de Clonación

#### Estructura anterior (v1.x):
```
~/clones/github/repo1/
~/clones/github/repo2/
```

#### Estructura nueva:
```
proyecto/clones/2026-03-25_10-30-45/github/repo1/
proyecto/clones/2026-03-25_10-30-45/github/repo2/
proyecto/clones/2026-03-25_14-22-15/gitlab/repo3/
```

#### Ventajas:
- ✅ Cada sesión de clonación tiene su carpeta con timestamp
- ✅ Fácil identificar cuándo se clonaron los repos
- ✅ Aislamiento de bloques de clonación
- ✅ Ubicación local en el proyecto (no en home)

### 🔧 Cambios en Configuración

#### config.py (src/):
- Importa `python-dotenv` para leer `.env`
- Genera `CLONE_SESSION_TIMESTAMP` automáticamente
- Crea `CLONES_DIR = CLONES_BASE_DIR / CLONE_SESSION_TIMESTAMP`
- Añade variables de entorno: `GITHUB_TOKEN`, `GITLAB_TOKEN`, `BITBUCKET_TOKEN`, `BITBUCKET_USER`

#### main.py (src/):
- Actualiza imports para nuevo layout
- Integración con rutas correctas de módulos

#### auth.py (modules/):
- Intenta primero usar tokens de `.env`
- Si no existen o fallan, solicita interactivamente
- Mantiene compatibilidad con funcionalidad antigua

#### run.sh:
- Ahora ejecuta `python3 src/main.py`
- Verifica existencia de `.env`
- Mensajes actualizados

#### install.sh:
- Copia `.env.example` a `.env` en primera instalación
- Mensajes de instrucciones actualizados
- Nota sobre configuración de tokens

### 📚 Documentación

#### Cambios:
- ✅ Se movieron todos los `.md` a la carpeta `docs/` (excepto `README.md`)
- ✅ Se mantiene `README.md` en la raíz del proyecto
- ✅ `CAMBIOS.md` ahora en `docs/CAMBIOS.md`

#### Archivos movidos:
- `EJEMPLO_URLS.md` → `docs/EXAMPLE_URLS.md`
- `INDEX.md` → `docs/INDEX.md`
- `PROYECTO.txt` → `docs/PROYECTO.txt`
- `QUICKSTART.md` → `docs/QUICKSTART.md`
- `USAGE.md` → `docs/USAGE.md`
- `CAMBIOS.md` → `docs/CAMBIOS.md`

### 🚀 Cómo Usar la Nueva Estructura

#### Setup inicial:
```bash
cd hydra-clone
bash install.sh
```

#### Configurar tokens (opcional):
```bash
# Opción 1: Editar .env
nano .env
# GITHUB_TOKEN=tu_token_aqui

# Opción 2: Dejar vacío y proporcionar en la interfaz
```

#### Ejecutar la aplicación:
```bash
bash run.sh
# O directamente:
python3 src/main.py
```

#### Verificar archivos clonados:
```bash
ls -la clones/
# Verás carpetas con timestamp:
# clones/2026-03-25_10-30-45/
# clones/2026-03-25_14-22-15/
```

#### Ver reportes:
```bash
ls -la reports/
# clone-report_2026-03-25_10-30-45.md
# clone-report_2026-03-25_14-22-15.md
```

### 🔄 Migración desde v1.x

Si tienes repositorios clonados en la versión anterior en `~/clones/`, debes:

1. Copiarlos manualmente a la nueva ubicación dentro del proyecto:
```bash
cp -r ~/clones/github/* clones/2026-03-25_00-00-00/github/
```

2. O generar reportes de los clones anteriores manualmente

### 📊 Mejoras Implementadas

1. **Estructura profesional** - Separación clara de responsabilidades
2. **Variables de entorno** - Configuración segura de credenciales
3. **Timestamps automáticos** - Mejor organización de sesiones
4. **Documentación centralizada** - Todo en `docs/`
5. **Código limpio** - Mínimo en raíz, máximo en módulos
6. **Mejor mantenimiento** - Fácil de escalar y modificar

### ⚠️ Cambios que Requieren Atención

- **IMPORTANTE**: Cambio de ubicación de clones de `~/clones/` a `proyecto/clones/TIMESTAMP/`
- **IMPORTANTE**: Nuevo sistema de variables de entorno (`.env`)
- Actualizar scripts que referencias rutas antiguas
- Actualizar documentación externa que mencione `~/clones/`

### 🔮 Roadmap Futuro

- [ ] Soporte para más plataformas (Gitea, Forgejo, etc.)
- [ ] Interfaz web (Django/FastAPI)
- [ ] Base de datos para historial de clonaciones
- [ ] Sistema de plugins
- [ ] Configuración por proyecto
- [ ] Estadísticas avanzadas

---

**Versión:** 2.0.0  
**Fecha:** 2026-03-25  
**Autor:** HydraClone Team

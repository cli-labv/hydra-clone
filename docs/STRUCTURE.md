# 📁 HydraClone - Estructura del Proyecto v3.1.0

## Árbol de directorios

```
hydra-clone/
│
├── 📄 README.md                    # Documentación principal
├── 🐉 start.sh                     # PUNTO DE ENTRADA ÚNICO (menú interactivo)
├── 🔧 hydra-clone.py              # Wrapper de ejecución alternativo
├── 📋 requirements.txt             # Dependencias
├── 📝 .env                         # Variables de entorno (gitignored)
├── 📝 .env.example                 # Template de .env
├── 🚫 .gitignore                   # Archivos ignorados en Git
│
├── 📁 src/                         # Código fuente principal
│   ├── __init__.py
│   ├── main.py                     # CLI principal
│   └── config.py                   # Configuración global
│
├── 📁 modules/                     # Módulos reutilizables
│   ├── __init__.py
│   ├── auth.py                     # Autenticación
│   ├── clone.py                    # Lógica de clonación
│   ├── reports.py                  # Reportes
│   ├── hydra_banner.py             # Banner animado
│   ├── hydra_progress.py           # Progreso y estadísticas
│   └── animations.py               # Animaciones
│
├── 📁 docs/                        # Documentación
│   ├── STARTUP.md                  # Guía de inicio (nuevo)
│   ├── STRUCTURE.md                # Estructura del proyecto
│   ├── CLEANUP.md                  # Cambios de limpieza
│   ├── CAMBIOS.md                  # Changelog
│   ├── QUICKSTART.md
│   ├── USAGE.md
│   ├── EXAMPLE_URLS.md
│   └── INDEX.md
│
├── 📁 scripts/                     # Scripts de automatización
│   ├── README.md                   # Documentación de scripts
│   ├── install.sh                  # Instalación
│   ├── run.sh                      # Ejecución
│   └── test.sh                     # Pruebas
│
├── 📁 clones/                      # Repositorios clonados (LOCAL)
│   └── YYYY-MM-DD_HH-MM-SS/        # Timestamp por sesión
│       ├── github/
│       ├── gitlab/
│       └── bitbucket/
│
├── 📁 reports/                     # Reportes generados
│   └── clone-report_TIMESTAMP.md
│
├── 📁 logs/                        # Logs
├── 📁 config/                      # Configuración proyecto
├── 📁 venv/                        # Entorno virtual
└── 📁 __pycache__/                 # Cache Python
```

## Descripción de carpetas

### `src/`
Código fuente principal del proyecto.
- **main.py**: Punto de entrada, CLI principal
- **config.py**: Configuración global, variables de entorno, directorios

### `modules/`
Módulos reutilizables y servicios.
- **auth.py**: Autenticación multi-plataforma
- **clone.py**: Lógica de clonación asincrónica
- **reports.py**: Generación de reportes Markdown
- **hydra_banner.py**: Banner animado de bienvenida
- **hydra_progress.py**: Pantalla de progreso y estadísticas
- **animations.py**: Efectos y animaciones generales

### `docs/`
Documentación técnica y de usuario.
- **CAMBIOS.md**: Changelog completo de v2.0.0
- **QUICKSTART.md**: Guía rápida
- **USAGE.md**: Instrucciones detalladas

### `scripts/`
Scripts de automatización y utilidad.
- **install.sh**: Instalación y configuración
- **run.sh**: Ejecución del CLI
- **test.sh**: Pruebas
- **README.md**: Documentación de scripts

## 🚀 Punto de Entrada Principal (v3.1.0)

### `start.sh` - Menú Interactivo Unificado

El archivo **`start.sh`** es el nuevo punto de entrada único:

```bash
./start.sh
```

Proporciona un menú interactivo con opciones:

```
¿Qué deseas hacer?

  1) 📦 Instalar dependencias     (primera vez)
  2) ▶️  Ejecutar aplicación       (usar HydraClone)
  3) 🧪 Ejecutar pruebas           (testing)
  4) ❌ Salir
```

Ver detalles completos en [STARTUP.md](STARTUP.md)

## Uso de Scripts

### Opción 1: Menú Interactivo (Recomendado)
```bash
./start.sh
```

### Opción 2: Scripts Directos
```bash
bash scripts/install.sh    # Instalar
bash scripts/run.sh        # Ejecutar
bash scripts/test.sh       # Pruebas
```

## Beneficios de v3.1.0

✅ Punto de entrada único y claro  
✅ Menú interactivo intuitivo  
✅ Validaciones automáticas de requisitos  
✅ Estructura profesional y escalable  
✅ Variables de entorno seguras  
✅ Timestamps automáticos por sesión  
✅ Documentación centralizada  
✅ Scripts organizados  
✅ Código modular y reutilizable  

---

**Versión:** 3.1.0  
**Última actualización:** 2026-03-25

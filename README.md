# HydraClone - Clonación Masiva de Repositorios 🐉

Herramienta ultra ligera para clonación masiva de repositorios desde múltiples plataformas (GitHub, GitLab, Bitbucket).

## 🚀 Características

✅ **Entrada Interactiva** - Ingresa URLs con validación automática
✅ **Detección Automática** - Identifica GitHub, GitLab, Bitbucket
✅ **Autenticación Flexible** - Tokens o navegador para OAuth
✅ **Clonación Concurrente** - Hasta 1000+ repos simultáneamente
✅ **Banner HydraClone** - Animación elegante con la hydra
✅ **Manejo Inteligente de Errores** - Continúa si falla un repo
✅ **Reporte en Markdown** - Detalle completo de éxitos y fallos
✅ **Ultra Ligero** - Bajo consumo de RAM y CPU

## 📋 Requisitos

- Python 3.8+
- Git instalado
- Conexión a internet

## 🔧 Instalación

```bash
./start.sh   # Opción 1 instala dependencias y prepara todo
```

Scripts de apoyo (ubicados en `scripts/`):
- `bash scripts/install.sh` para instalar manualmente.
- `bash scripts/run.sh` para ejecutar manualmente después de instalar.

## ▶️ Uso Rápido

```bash
./start.sh         # Menú interactivo (recomendado)
```

### Flujo Completo:

1. **Ejecutar start.sh** - Menú principal interactivo
2. **Opción 1: Instalar** - Primero configura el entorno (solo primera vez)
3. **Opción 2: Ejecutar** - Inicia HydraClone con banner animado
4. **Ingresa URLs** - Pega URLs una por una (tipo: `done` para terminar)
5. **Escaneo Automático** - Detecta plataformas
6. **Autenticación** - Solicita credenciales si las necesita
7. **Clonación Masiva** - Con animación de progreso
8. **Reporte Final** - Genera archivo `.md` con resultados

Ver detalles completos en [docs/STARTUP.md](docs/STARTUP.md)

## 🔐 Autenticación

### GitHub
- Token PAT: `https://github.com/settings/tokens`
- Permisos: `repo`, `read:user`

### GitLab
- Token PAT: `https://gitlab.com/profile/personal_access_tokens`
- Permisos: `read_api`, `read_user`, `read_repository`

### Bitbucket
- App Password: `https://bitbucket.org/account/settings/app-passwords/`

## 📊 Estructura

```
hydra-clone/
├── src/                    # Código principal
│   ├── main.py            # CLI principal
│   └── config.py          # Configuración centralizada
├── modules/               # Módulos reutilizables
│   ├── auth.py           # Autenticación
│   ├── clone.py          # Lógica de clonación
│   ├── reports.py        # Generación de reportes
│   ├── hydra_banner.py   # Banner animado
│   ├── hydra_progress.py # Barra de progreso
│   └── animations.py     # Efectos visuales
├── scripts/               # Scripts de automatización
│   ├── install.sh        # Instalación
│   ├── run.sh            # Ejecución
│   └── test.sh           # Pruebas
├── docs/                  # Documentación
│   ├── STRUCTURE.md      # Arquitectura del proyecto
│   ├── CAMBIOS.md        # Historial de cambios
│   ├── QUICKSTART.md     # Guía rápida
│   └── ...
├── clones/               # Repositorios clonados (generado)
├── reports/              # Reportes generados (generado)
├── logs/                 # Archivos de log (generado)
├── hydra-clone.py        # Punto de entrada
├── requirements.txt      # Dependencias
├── .env                  # Variables de entorno (local, no comprometer)
├── .gitignore            # Archivos ignorados en Git
└── README.md            # Esta documentación
```

Ver detalles completos en [docs/STRUCTURE.md](docs/STRUCTURE.md)

## 🎨 Banner HydraClone

```
🐉 Welcome to HydraClone

██╗  ██╗██╗   ██╗██╗███╗   ██╗ ██████╗ ██████╗ ██████╗ ███████╗
██║  ██║██║   ██║██║████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝
███████║██║   ██║██║██╔██╗ ██║██║     ██║   ██║██║  ██║█████╗  
██╔══██║██║   ██║██║██║╚██╗██║██║     ██║   ██║██║  ██║██╔══╝  
██║  ██║╚██████╔╝██║██║ ████║╚██████╗╚██████╔╝██████╔╝███████╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
```

## 💾 Configuración

### Variables de Entorno (.env)

Copia `.env.example` a `.env` y configura tus tokens:

```bash
cp .env.example .env
nano .env
```

Disponibles:
- `GITHUB_TOKEN` - Token de acceso personal de GitHub
- `GITLAB_TOKEN` - Token de acceso personal de GitLab
- `BITBUCKET_TOKEN` - Contraseña de aplicación de Bitbucket
- `BITBUCKET_USER` - Usuario de Bitbucket

**Nota:** Si no configuras tokens en `.env`, la aplicación te pedirá credenciales interactivamente.

## 🛠️ Opciones Futuras

- [ ] Filtrado por idioma/stars
- [ ] Espejo local automático
- [ ] Webhooks para actualizaciones
- [ ] Interfaz web
- [ ] Estadísticas de repositorios

## 📄 Licencia

MIT

---

**HydraClone v1.0** - Clonación masiva con la fuerza de la Hydra 🐉

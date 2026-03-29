# 🚀 HYDRACLONE CLI - GUÍA RÁPIDA

## Ubicación del Proyecto
```
/home/dev/leo/hydra-clone/
```

## ⚡ Inicio Rápido (3 pasos)

### Paso 1: Instalar
```bash
cd /home/dev/leo/hydra-clone
bash install.sh
```

### Paso 2: Ejecutar
```bash
bash run.sh
```

### Paso 3: Usar
1. Verás la pantalla de bienvenida animada
2. Ingresa URLs de repositorios (una por una)
3. Escribe `done` cuando termines
4. Confirma la clonación
5. ¡Listo! Espera a que se complete

---

## 📁 Archivos del Proyecto

### 🐍 Código Python
- `main.py` - CLI principal (punto de entrada)
- `animations.py` - Animaciones visuales
- `auth.py` - Gestión de autenticación
- `clone.py` - Lógica de clonación concurrente
- `reports.py` - Generación de reportes MD
- `config.py` - Configuración global

### 🔧 Scripts
- `run.sh` - Ejecutar HydraClone
- `install.sh` - Instalar dependencias
- `hydra-clone.py` - Punto de entrada alternativo

### 📚 Documentación
- `README.md` - Introducción del proyecto
- `USAGE.md` - Guía completa de uso (¡LEER ESTO!)
- `EXAMPLE_URLS.md` - Ejemplos de URLs
- `PROYECTO.txt` - Resumen del proyecto

### 📦 Configuración
- `requirements.txt` - Dependencias Python
- `venv/` - Entorno virtual (creado automáticamente)

---

## 🎯 Lo que Hace HydraClone

✅ **Entrada de URLs** - Ingresa múltiples repositorios
✅ **Detección Automática** - GitHub, GitLab, Bitbucket
✅ **Autenticación** - Tokens o navegador
✅ **Clonación Concurrente** - Hasta 8 simultáneamente
✅ **Continúa en Errores** - No se detiene si falla uno
✅ **Reporte Final** - Archivo Markdown con resultados
✅ **Animaciones** - Welcome screen + Progreso dinámico

---

## 📊 Características

| Característica | Soporte |
|---|---|
| Repositorios simultáneos | 10-1000+ |
| Plataformas | GitHub, GitLab, Bitbucket |
| Autenticación | PAT, OAuth, App Password |
| Reportes | Markdown con timestamp |
| Manejo errores | Continúa + reporta |
| RAM | ~145 MB |
| CPU | ~35% |

---

## 🔐 Credenciales

Se guardan automáticamente en:
```
config/.credentials/credentials.json
```

Primero que se solicite, elige:
- **GitHub:** Token PAT (recomendado)
- **GitLab:** Token PAT
- **Bitbucket:** App Password

Puedes obtenerlos en:
- GitHub: https://github.com/settings/tokens
- GitLab: https://gitlab.com/profile/personal_access_tokens
- Bitbucket: https://bitbucket.org/account/settings/app-passwords/

---

## 📍 Dónde se guardan los Clones

```
clones/FECHA_HORA/
├── github/
│   ├── flask/
│   ├── requests/
│   └── ...
├── gitlab/
│   └── ...
└── bitbucket/
    └── ...
```

---

## 📄 Reportes

Se generan en:
```
reports/clone-report_FECHA_HORA.md
```

Contiene:
- ✅ Repos clonados exitosamente
- ❌ Repos con error (y por qué fallaron)
- 📊 Estadísticas (tamaño, tiempo, velocidad)
- 📈 Resumen general

---

## 🛠️ Troubleshooting Rápido

**¿No funciona el venv?**
```bash
cd /home/dev/leo/hydra-clone
rm -rf venv/
bash install.sh
```

**¿Quieres cambiar el directorio de clonación?**
Edita `main.py`, línea ~40:
```python
self.clone_manager = CloneManager(
    base_dir=Path("/tu/ruta/personalizada"),
    max_concurrent=8
)
```

**¿Más de 8 repos simultáneos?**
Edita en `main.py`:
```python
max_concurrent=16  # Aumenta según tu conexión
```

---

## 📖 Documentación Completa

**Para más detalles, lee:**
```bash
cat USAGE.md
```

O abre el archivo directamente en tu editor favorito.

---

## 💡 Ejemplos Rápidos

### Clonar 3 repos de GitHub
```
URL 1: https://github.com/pallets/flask
URL 2: https://github.com/psf/requests
URL 3: https://github.com/tornadoweb/tornado
URL 4: done
```

### Clonar de múltiples plataformas
```
URL 1: https://github.com/facebook/react
URL 2: https://gitlab.com/gitlab-org/gitlab
URL 3: https://bitbucket.org/tutorials/tutorials.bitbucket.io
URL 4: done
```

---

## ✨ Animaciones que Verás

**Inicio:**
```
╔════════════════════════════════════════╗
║   🤖 HydraClone v1.0                 ║
║   Clonación Masiva de Repositorios     ║
╚════════════════════════════════════════╝
```

**Durante clonación:**
```
📦 Clonando... [████████░░░░] 62% (31/50)

Repositorios activos:
  · github.com/repo1 [✓]
  · · gitlab.com/repo2 [████░░░░]
  · · · bitbucket.org/repo3 [██░░░░░░]
```

---

## 🎓 Aprender Más

1. **Conocer el flujo:** Lee `USAGE.md`
2. **Ver ejemplos:** Lee `EXAMPLE_URLS.md`
3. **Entender código:** Revisa `main.py`
4. **Configuración avanzada:** Edita `config.py`

---

## ✅ Verificación Rápida

Para verificar que todo está instalado:
```bash
cd /home/dev/leo/hydra-clone
bash test.sh
```

Debe mostrar:
```
✓ Animaciones importadas
✓ Auth importada
✓ Clone importada
✓ Reports importada
✅ Todos los módulos se cargan correctamente
```

---

## 🚀 ¡Listo para Usar!

Ejecuta ahora:
```bash
cd /home/dev/leo/hydra-clone
bash run.sh
```

---

**HydraClone v1.0** - Clonación masiva hecha simple ✨

Última actualización: 2026-03-24

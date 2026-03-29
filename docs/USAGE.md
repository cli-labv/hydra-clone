# 📖 GUÍA COMPLETA DE USO

## Tabla de Contenidos
1. [Instalación Rápida](#instalación-rápida)
2. [Primer Uso](#primer-uso)
3. [Autenticación Detallada](#autenticación-detallada)
4. [Ejemplos Prácticos](#ejemplos-prácticos)
5. [Solución de Problemas](#solución-de-problemas)

---

## 🚀 Instalación Rápida

### Opción 1: Script Automático (Recomendado)
```bash
cd hydra-clone
bash install.sh
bash run.sh
```

### Opción 2: Manual
```bash
cd hydra-clone
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

---

## 🎯 Primer Uso

### Paso 1: Pantalla de Bienvenida
La aplicación te mostrará una pantalla de bienvenida animada.

```
╔════════════════════════════════════════╗
║                                        ║
║   Clonación Masiva de Repositorios     ║
║   Ultra Ligero • Multi-plataforma      ║
║                                        ║
╚════════════════════════════════════════╝

¡Bienvenido a HydraClone!
✓ Python 3.8+
✓ Git detectado
✓ Conectividad de red
✓ Validando configuración

✨ Listo para clonar repositorios
```

### Paso 2: Ingresa URLs
```
📥 Ingresa las URLs de los Repositorios
════════════════════════════════════════

Instrucciones:
  • Pega una URL por línea
  • La coma se agregará automáticamente
  • Escribe 'done' cuando termines

URL 1: https://github.com/pallets/flask
  ✓ Agregada: https://github.com/pallets/flask
URL 2: https://github.com/psf/requests
  ✓ Agregada: https://github.com/psf/requests
URL 3: done
```

### Paso 3: Escaneo Automático
La herramienta detecta las plataformas:

```
🔍 Escaneo de Plataformas
════════════════════════════════════════
  🐙 https://github.com/pallets/flask → GITHUB
  🐙 https://github.com/psf/requests → GITHUB

Total de repositorios: 2 | Plataformas: GitHub
```

### Paso 4: Autenticación (si es necesaria)
Si necesita credenciales, solicitará automáticamente:

```
🔐 Verificación de Credenciales
════════════════════════════════════════
✓ GitHub: Autenticado
⚠ GitLab: Sin autenticar

Se requiere autenticación para continuar
```

### Paso 5: Confirmación y Clonación
```
¿Deseas continuar con la clonación de 2 repositorios?
Confirma (s/n): s

🚀 Iniciando Clonación Masiva
════════════════════════════════════════

📦 Clonando repositorios... [████████░░░░] 40% (2/5)

Repositorios activos:
  · flask [✓]
  · · requests [████░░░░] 40%
  · · · otra-repo [⏳ esperando]

⏱️  Tiempo: 1m 23s | 🔋 RAM: ~145 MB | 📊 CPU: 35%
```

### Paso 6: Reporte Final
Se genera automáticamente un archivo `.md`:

```
📄 Reporte Generado
════════════════════════════════════════
Ubicación: reports/clone-report_2024-03-24_00-30-15.md

✓ Exitosos: 5
✗ Fallidos: 0
📦 Tamaño Total: 1,234.56 MB
⏱️  Tiempo Total: 5m 42s
```

---

## 🔐 Autenticación Detallada

### GitHub

#### Token PAT (Recomendado)
1. Ve a https://github.com/settings/tokens
2. Click en "Generate new token" → "Personal access tokens"
3. Dale un nombre (ej: "hydra-clone")
4. Selecciona permisos:
   - ✓ `repo` - Acceso a repositorios
   - ✓ `read:user` - Leer perfil
5. Click "Generate token"
6. **Copia el token** (solo se muestra una vez)
7. Pégalo en HydraClone cuando lo solicite

#### Qué token usar:
```
Opción 1: Token (Recommended) ← Selecciona esta
Opción 2: OAuth (abrir navegador)

Ingresa tu token de GitHub: ghp_xxxxxxxxxxxxxxxxxxxx
✓ Autenticación GitHub exitosa
```

### GitLab

#### Token PAT
1. Ve a https://gitlab.com/profile/personal_access_tokens
2. Crea nuevo token con nombre "hydra-clone"
3. Selecciona permisos:
   - ✓ `read_api` - Leer API
   - ✓ `read_user` - Leer usuario
   - ✓ `read_repository` - Leer repositorios
4. Copia el token
5. Pégalo en HydraClone

**Si usas GitLab on-premise:**
```
Ingresa tu token de GitLab: glpat-xxxxxxxxxx
URL de GitLab (por defecto: gitlab.com): gitlab.tu-empresa.com
✓ Autenticación GitLab exitosa
```

### Bitbucket

#### App Password
1. Ve a https://bitbucket.org/account/settings/app-passwords/
2. Click "Create app password"
3. Nombre: "hydra-clone"
4. Permisos: `account:read`, `repository:read`
5. Copia la contraseña
6. Ingresa en HydraClone:

```
Usuario de Bitbucket: tu-usuario
App Password: **********************
✓ Autenticación Bitbucket exitosa
```

---

## 💡 Ejemplos Prácticos

### Ejemplo 1: Clonar Proyectos Python Populares
```bash
URL 1: https://github.com/pallets/flask
URL 2: https://github.com/psf/requests
URL 3: https://github.com/tornadoweb/tornado
URL 4: https://github.com/apache/airflow
URL 5: done
```

**Resultado:**
- 4 repositorios clonados
- En `clones/FECHA_HORA/github/`
- Reporte con estadísticas

### Ejemplo 2: Mix de Plataformas
```bash
URL 1: https://github.com/facebook/react
URL 2: https://gitlab.com/gitlab-org/gitlab
URL 3: https://bitbucket.org/tutorials/tutorials.bitbucket.io
URL 4: done
```

**Resultado:**
- Detecta 3 plataformas automáticamente
- Solicita credenciales de cada una
- Clona concurrentemente
- Reporte detallado por plataforma

### Ejemplo 3: 100+ Repositorios
```bash
# Copiar lista de URLs y pegarla
# HydraClone maneja hasta 1000+ repos
# Concurrencia: 8 simultáneos (configurable)
```

---

## 🐛 Solución de Problemas

### Error: "Could not resolve host"
```
❌ Problema: No se pudo conectar a internet

Solución:
1. Verifica tu conexión a internet
2. Si usas proxy, configúralo en git:
   git config --global http.proxy http://proxy:puerto
```

### Error: "Permission denied"
```
❌ Problema: Repositorio privado o acceso denegado

Solución:
1. Verifica que tengas acceso al repositorio
2. Recrea el token con permisos correctos
3. Elimina credenciales guardadas: rm config/.credentials/credentials.json
```

### Error: "Repository not found"
```
❌ Problema: La URL es incorrecta o el repo no existe

Solución:
1. Verifica la URL completa
2. Asegúrate que sea pública (si no tienes acceso)
3. Copia la URL desde la página del repositorio
```

### Error: "Timeout"
```
❌ Problema: El repositorio tardó más de 5 minutos en clonarse

Solución:
1. Verifica tu velocidad de conexión
2. Intenta clonar repositorios más pequeños
3. Reduce la concurrencia (máximo 8, por defecto)
```

### Las credenciales no se guardan
```
❌ Problema: Al reiniciar pierdes las credenciales

Solución (Normal):
Las credenciales se guardan en config/.credentials/credentials.json
Si no se guardan automáticamente:
1. Verifica permisos de carpeta: config/.credentials/
2. Intenta crear la carpeta manualmente
3. Verifica permisos de lectura/escritura
```

---

## 📁 Estructura de Carpetas Generadas

```
clones/FECHA_HORA/            # Directorio base (dentro del repo)
├── github/
│   ├── flask/
│   ├── requests/
│   └── ...
├── gitlab/
│   └── ...
└── bitbucket/

config/.credentials/          # Config y credenciales
└── credentials.json          # ⚠️ No compartir

reports/                      # Reportes
├── clone-report_2024-03-24_00-30-15.md
└── ...
```

---

## ⚙️ Configuración Avanzada

### Cambiar directorio de clonación
Edita `main.py`:
```python
self.clone_manager = CloneManager(
    base_dir=Path("clones/personalizado"),  # Por defecto usa clones/FECHA_HORA/
    max_concurrent=8
)
```

### Cambiar concurrencia
```python
self.clone_manager = CloneManager(
    max_concurrent=16  # Aumentar a 16 simultáneos
)
```

### Usar git con SSH en lugar de HTTPS
Las URLs SSH funcionan automáticamente:
```
git@github.com:usuario/repo.git
git@gitlab.com:usuario/repo.git
```

---

## 📞 Soporte

- **Documentación:** Ver `README.md`
- **Ejemplos:** Ver `EXAMPLE_URLS.md`
- **GitHub Issues:** Reporta bugs y solicita features

---

**HydraClone v1.0** - Hecho con ❤️ para desarrolladores

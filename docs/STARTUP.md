# 🚀 Guía de Inicio - HydraClone

## 📌 Punto de Entrada Único

Ahora el proyecto tiene un **único archivo de inicio**: `start.sh`

Este archivo consolida todas las opciones de inicio en un menú interactivo.

## ▶️ Cómo Usar

### Opción 1: Ejecución Directa (Recomendado)
```bash
./start.sh
```

### Opción 2: Con Bash
```bash
bash start.sh
```

## 📋 Menú Principal

Al ejecutar `start.sh`, verás:

```
╔════════════════════════════════════════════════════════════╗
║         🐉 HydraClone - Mass Repository Cloner           ║
╚════════════════════════════════════════════════════════════╝

¿Qué deseas hacer?

  1) 📦 Instalar dependencias     (primera vez)
  2) ▶️  Ejecutar aplicación       (usar HydraClone)
  3) 🧪 Ejecutar pruebas           (testing)
  4) ❌ Salir

Selecciona opción: ) 
```

## 🎯 Opciones Disponibles

### 1️⃣ Instalar Dependencias
```
Opción: 1
```
- Instala Python 3 + venv
- Descarga dependencias (colorama, tqdm, wcwidth, etc.)
- Crea estructura de carpetas (`clones/`, `reports/`, `logs/`)
- **Usar**: Primera vez antes de ejecutar la app

### 2️⃣ Ejecutar Aplicación
```
Opción: 2
```
- Inicia el CLI de HydraClone
- Muestra banner animado con la hydra
- Permite clonar repositorios masivamente
- **Usar**: Después de instalar

### 3️⃣ Ejecutar Pruebas
```
Opción: 3
```
- Ejecuta suite de pruebas
- Valida que todo funciona correctamente
- **Usar**: Opcional, para verificación

### 4️⃣ Salir
```
Opción: 4
```
- Cierra el menú y sale
- **Atajo**: Ctrl+C también funciona

## 🔄 Flujo Típico de Uso

```
┌─────────────────────────────────┐
│   ./start.sh                    │
│   ↓                             │
│   ¿Instalar? → Opción 1 ✓       │
│   ↓                             │
│   ¿Ejecutar? → Opción 2 ✓       │
│   ↓                             │
│   [Usa HydraClone]              │
│   ↓                             │
│   ¿Salir? → Opción 4 ✓          │
└─────────────────────────────────┘
```

## ✅ Requisitos Previos

El script verifica automáticamente:
- ✓ Python 3 instalado
- ✓ Git instalado
- ✓ Conexión a internet (para git clone)

Si falta algo, mostrará instrucciones de instalación.

## 🛠️ Scripts Internos

`start.sh` es un wrapper que ejecuta scripts en `scripts/`:

```
start.sh
├── → scripts/install.sh   (opción 1)
├── → scripts/run.sh       (opción 2)
├── → scripts/test.sh      (opción 3)
└── → exit                 (opción 4)
```

Puedes ejecutarlos directamente si lo prefieres:
```bash
bash scripts/install.sh    # Instalar
bash scripts/run.sh        # Ejecutar
bash scripts/test.sh       # Pruebas
```

## 🎨 Características del Menú

- ✨ Colores ANSI para mejor legibilidad
- 🔄 Menú recurrente (vuelve después de cada acción)
- ⚡ Validación de requisitos automática
- 📍 Banner decorativo con la hydra
- ❌ Validación de opciones inválidas

## 📝 Ejemplo Interactivo

```bash
$ ./start.sh
╔════════════════════════════════════════════════════════════╗
║         🐉 HydraClone - Mass Repository Cloner           ║
╚════════════════════════════════════════════════════════════╝

✓ Requisitos cumplidos

¿Qué deseas hacer?

  1) 📦 Instalar dependencias     (primera vez)
  2) ▶️  Ejecutar aplicación       (usar HydraClone)
  3) 🧪 Ejecutar pruebas           (testing)
  4) ❌ Salir

Selecciona opción: ) 1

→ Ejecutando instalación...
🚀 HydraClone CLI - Setup
════════════════════════════
✓ Python 3 detectado: Python 3.12.3
✓ Git detectado: git version 2.43.0
✓ Entorno virtual creado
📚 Instalando dependencias...
✓ Instalación completada

Presiona Enter para continuar...

¿Qué deseas hacer?

  1) 📦 Instalar dependencias     (primera vez)
  2) ▶️  Ejecutar aplicación       (usar HydraClone)
  3) 🧪 Ejecutar pruebas           (testing)
  4) ❌ Salir

Selecciona opción: ) 2

→ Iniciando HydraClone...
[Inicia la aplicación...]

Presiona Enter para continuar...

Selecciona opción: ) 4
👋 ¡Hasta luego!
```

## 🚨 Solución de Problemas

### "Permission denied" al ejecutar ./start.sh
```bash
chmod +x start.sh
./start.sh
```

### "python3: comando no encontrado"
```bash
sudo apt update
sudo apt install python3 python3-venv
```

### "git: comando no encontrado"
```bash
sudo apt install git
```

## 🎯 Ventajas de Este Sistema

✅ **Un solo punto de entrada**: No hay confusión sobre qué archivo ejecutar
✅ **Menú intuitivo**: Opciones claras para cada acción
✅ **Verificaciones automáticas**: Detecta problemas antes de empezar
✅ **Reutilizable**: Cada opción llama a scripts en `scripts/`
✅ **Escalable**: Fácil agregar más opciones al menú

## 📚 Referencias

- Ver: [STRUCTURE.md](STRUCTURE.md) - Arquitectura del proyecto
- Ver: [QUICKSTART.md](QUICKSTART.md) - Guía rápida
- Ver: [USAGE.md](USAGE.md) - Uso detallado de la app

---

**HydraClone v3.1.0** - Startup unificado 🐉

#!/bin/bash

# HydraClone CLI - Script de ejecución rápida

# Obtener directorio del proyecto (un nivel arriba del directorio scripts)
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="$PROJECT_DIR/venv"

# Verificar si venv existe
if [ ! -d "$VENV_DIR" ]; then
    echo "⚠️  Entorno virtual no encontrado"
    echo "Ejecuta primero: bash scripts/install.sh"
    exit 1
fi

# Verificar .env
if [ ! -f "$PROJECT_DIR/.env" ]; then
    echo "⚠️  Archivo .env no encontrado"
    echo "Copia .env.example a .env y configura tus tokens (opcional)"
fi

# Activar venv y ejecutar
source "$VENV_DIR/bin/activate"
cd "$PROJECT_DIR"
python3 src/main.py

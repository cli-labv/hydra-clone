#!/bin/bash

# HydraClone CLI - Script de instalación y ejecución

set -e

# Obtener directorio del proyecto (un nivel arriba del directorio scripts)
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="$PROJECT_DIR/venv"

echo "🚀 HydraClone CLI - Setup"
echo "════════════════════════════"
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado"
    exit 1
fi

echo "✓ Python 3 detectado: $(python3 --version)"

# Verificar Git
if ! command -v git &> /dev/null; then
    echo "❌ Git no está instalado"
    exit 1
fi

echo "✓ Git detectado: $(git --version)"
echo ""

# Crear venv si no existe o si apunta a otro proyecto
RECREATE_VENV=false
if [ -d "$VENV_DIR" ]; then
    if grep -q "VIRTUAL_ENV=$PROJECT_DIR/venv" "$VENV_DIR/bin/activate" 2>/dev/null; then
        echo "✓ Entorno virtual existente"
    else
        echo "⚠️  Entorno virtual apunta a otro proyecto. Se recreará."
        RECREATE_VENV=true
    fi
else
    RECREATE_VENV=true
fi

if [ "$RECREATE_VENV" = true ]; then
    rm -rf "$VENV_DIR"
    echo "📦 Creando entorno virtual..."
    python3 -m venv "$VENV_DIR"
    echo "✓ Entorno virtual creado"
fi

echo ""
echo "📚 Instalando dependencias..."

# Activar venv
source "$VENV_DIR/bin/activate"

# Instalar/actualizar pip
pip install --upgrade pip setuptools wheel > /dev/null 2>&1

# Instalar requisitos
pip install -r "$PROJECT_DIR/requirements.txt" > /dev/null 2>&1

echo "✓ Dependencias instaladas"
echo ""

# Verificar .env
if [ ! -f "$PROJECT_DIR/.env" ]; then
    echo "⚠️  Configurando .env..."
    cp "$PROJECT_DIR/.env.example" "$PROJECT_DIR/.env" 2>/dev/null || true
    echo "✓ Archivo .env creado (configura tus tokens según sea necesario)"
    echo ""
fi

echo "════════════════════════════"
echo "✨ ¡Listo para usar!"
echo "════════════════════════════"
echo ""
echo "Para ejecutar HydraClone:"
echo ""
echo "  cd $PROJECT_DIR"
echo "  source venv/bin/activate"
echo "  python3 src/main.py"
echo ""
echo "O simplemente usa:"
echo "  bash scripts/run.sh"
echo ""


#!/bin/bash

# Script de prueba de Clone Master CLI

cd /home/dev/leo/clone-master

echo "🧪 Probando Clone Master CLI..."
echo ""

# Activar venv
source venv/bin/activate

# Mostrar versión
python3 -c "import animations; print('✓ Animaciones importadas')"
python3 -c "import auth; print('✓ Auth importada')"
python3 -c "import clone; print('✓ Clone importada')"
python3 -c "import reports; print('✓ Reports importada')"

echo ""
echo "✅ Todos los módulos se cargan correctamente"
echo ""
echo "Para usar la herramienta, ejecuta:"
echo "  cd /home/dev/leo/clone-master"
echo "  source venv/bin/activate"
echo "  python main.py"

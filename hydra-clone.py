#!/usr/bin/env python3
"""
HydraClone - Herramienta de Clonación Masiva
Punto de entrada principal
"""

import sys
from pathlib import Path

# Agregar proyecto al path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "src"))

# Ejecutar main
from src.main import main

if __name__ == "__main__":
    main()

"""
HydraClone - Herramienta CLI para clonación masiva de repositorios
Autor: HydraClone Team
Versión: 2.0.0
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Estructura del proyecto
PROJECT_ROOT = Path(__file__).parent.parent
SRC_DIR = PROJECT_ROOT / "src"
MODULES_DIR = PROJECT_ROOT / "modules"
DOCS_DIR = PROJECT_ROOT / "docs"
CONFIG_DIR = PROJECT_ROOT / "config"
CLONES_BASE_DIR = PROJECT_ROOT / "clones"
REPORTS_DIR = PROJECT_ROOT / "reports"
LOGS_DIR = PROJECT_ROOT / "logs"

# Generar timestamp para clonación en bloque
CLONE_SESSION_TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
CLONES_DIR = CLONES_BASE_DIR / CLONE_SESSION_TIMESTAMP

# Crear directorios si no existen
for directory in [CONFIG_DIR, CLONES_BASE_DIR, REPORTS_DIR, LOGS_DIR, CLONES_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Configuración de plataformas
GITHUB_API = "https://api.github.com"
GITLAB_API = "https://gitlab.com/api/v4"
BITBUCKET_API = "https://api.bitbucket.org/2.0"

# Variables de entorno (tokens preconfigurados)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
GITLAB_TOKEN = os.getenv("GITLAB_TOKEN", "")
BITBUCKET_TOKEN = os.getenv("BITBUCKET_TOKEN", "")
BITBUCKET_USER = os.getenv("BITBUCKET_USER", "")

# Límites de concurrencia
MAX_CONCURRENT_CLONES = 8
REQUEST_TIMEOUT = 30
CHUNK_SIZE = 8192

__version__ = "2.0.0"
__author__ = "HydraClone Team"


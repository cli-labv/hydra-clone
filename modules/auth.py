"""
Módulo de autenticación para GitHub, GitLab y Bitbucket
"""

import os
import json
import webbrowser
from pathlib import Path
from typing import Optional, Dict, Tuple
import requests
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text

console = Console()
CONFIG_DIR = Path.home() / ".hydra-clone"
CONFIG_DIR.mkdir(exist_ok=True)
CREDENTIALS_FILE = CONFIG_DIR / "credentials.json"

# Importar configuración
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from config import GITHUB_TOKEN, GITLAB_TOKEN, BITBUCKET_TOKEN, BITBUCKET_USER


class AuthManager:
    """Gestor de autenticación para múltiples plataformas"""
    
    def __init__(self):
        self.credentials = self._load_credentials()
    
    def _load_credentials(self) -> Dict:
        """Cargar credenciales guardadas"""
        if CREDENTIALS_FILE.exists():
            try:
                with open(CREDENTIALS_FILE, 'r') as f:
                    return json.load(f)
            except Exception as e:
                console.print(f"[red]Error al cargar credenciales: {e}[/red]")
                return {}
        return {}
    
    def _save_credentials(self) -> None:
        """Guardar credenciales"""
        try:
            with open(CREDENTIALS_FILE, 'w') as f:
                json.dump(self.credentials, f, indent=2)
            CREDENTIALS_FILE.chmod(0o600)  # Permisos seguros
        except Exception as e:
            console.print(f"[red]Error al guardar credenciales: {e}[/red]")
    
    def authenticate_github(self) -> bool:
        """Autenticar en GitHub"""
        # Primero intentar con token de .env
        if GITHUB_TOKEN and GITHUB_TOKEN.strip():
            console.print("[bright_cyan]🔐 Intentando autenticación con token de .env...[/bright_cyan]")
            if self._github_token_auth(token=GITHUB_TOKEN):
                return True
            console.print("[yellow]⚠️  Token de .env inválido, solicitar nuevo token[/yellow]")
        
        console.print()
        panel = Panel(
            "🔐 Autenticación GitHub",
            style="bold bright_cyan",
            expand=False
        )
        console.print(panel)
        
        console.print("\n¿Cómo deseas autenticarte?")
        console.print("[1] Token de acceso personal (PAT)")
        console.print("[2] OAuth (abrir navegador)")
        
        choice = Prompt.ask("Elige una opción", choices=["1", "2"], default="1")
        
        if choice == "1":
            return self._github_token_auth()
        else:
            return self._github_oauth_auth()
    
    def _github_token_auth(self, token: str = None) -> bool:
        """Autenticar GitHub con token"""
        if token is None:
            console.print()
            console.print("Obtén tu token en: https://github.com/settings/tokens", style="dim")
            console.print("(Requiere permisos: repo, read:user)")
            token = Prompt.ask("Ingresa tu token de GitHub", password=True)
        
        # Validar token
        try:
            headers = {"Authorization": f"token {token}"}
            response = requests.get("https://api.github.com/user", headers=headers, timeout=5)
            
            if response.status_code == 200:
                user_data = response.json()
                self.credentials['github'] = {
                    'token': token,
                    'username': user_data.get('login'),
                    'type': 'token'
                }
                self._save_credentials()
                console.print("[bright_green]✓ Autenticación GitHub exitosa[/bright_green]")
                return True
            else:
                console.print("[red]✗ Token inválido o expirado[/red]")
                return False
        except Exception as e:
            console.print(f"[red]✗ Error de conexión: {e}[/red]")
            return False
    
    def _github_oauth_auth(self) -> bool:
        """Autenticar GitHub con OAuth (abre navegador)"""
        console.print()
        console.print("Abriendo navegador para autenticación...")
        
        # Crear servidor local simple para recibir callback
        # (En versión simplificada, solo solicitar token)
        console.print("[yellow]Nota: Para OAuth completo, usa un token de acceso personal[/yellow]")
        return self._github_token_auth()
    
    def authenticate_gitlab(self) -> bool:
        """Autenticar en GitLab"""
        # Primero intentar con token de .env
        if GITLAB_TOKEN and GITLAB_TOKEN.strip():
            console.print("[bright_magenta]🔐 Intentando autenticación con token de .env...[/bright_magenta]")
            if self._gitlab_token_auth(token=GITLAB_TOKEN):
                return True
            console.print("[yellow]⚠️  Token de .env inválido, solicitar nuevo token[/yellow]")
        
        console.print()
        panel = Panel(
            "🔐 Autenticación GitLab",
            style="bold bright_magenta",
            expand=False
        )
        console.print(panel)
        
        console.print("\n¿Cómo deseas autenticarte?")
        console.print("[1] Token de acceso personal")
        console.print("[2] OAuth (abrir navegador)")
        
        choice = Prompt.ask("Elige una opción", choices=["1", "2"], default="1")
        
        if choice == "1":
            return self._gitlab_token_auth()
        else:
            return self._gitlab_oauth_auth()
    
    def _gitlab_token_auth(self, token: str = None) -> bool:
        """Autenticar GitLab con token"""
        if token is None:
            console.print()
            console.print("Obtén tu token en: https://gitlab.com/profile/personal_access_tokens", style="dim")
            console.print("(Requiere permisos: read_api, read_user, read_repository)")
            token = Prompt.ask("Ingresa tu token de GitLab", password=True)
        
        gitlab_url = Prompt.ask("URL de GitLab (por defecto: gitlab.com)", default="gitlab.com")
        
        try:
            headers = {"PRIVATE-TOKEN": token}
            response = requests.get(
                f"https://{gitlab_url}/api/v4/user",
                headers=headers,
                timeout=5
            )
            
            if response.status_code == 200:
                user_data = response.json()
                self.credentials['gitlab'] = {
                    'token': token,
                    'username': user_data.get('username'),
                    'url': gitlab_url,
                    'type': 'token'
                }
                self._save_credentials()
                console.print("[bright_green]✓ Autenticación GitLab exitosa[/bright_green]")
                return True
            else:
                console.print("[red]✗ Token inválido o expirado[/red]")
                return False
        except Exception as e:
            console.print(f"[red]✗ Error de conexión: {e}[/red]")
            return False
    
    def _gitlab_oauth_auth(self) -> bool:
        """Autenticar GitLab con OAuth"""
        console.print()
        console.print("[yellow]Para OAuth en GitLab, usa un token de acceso personal[/yellow]")
        return self._gitlab_token_auth()
    
    def authenticate_bitbucket(self) -> bool:
        """Autenticar en Bitbucket"""
        console.print()
        panel = Panel(
            "🔐 Autenticación Bitbucket",
            style="bold bright_blue",
            expand=False
        )
        console.print(panel)
        
        console.print("\nBitbucket usa App Passwords en lugar de tokens")
        console.print("Crea una en: https://bitbucket.org/account/settings/app-passwords/")
        
        username = Prompt.ask("Usuario de Bitbucket")
        password = Prompt.ask("App Password", password=True)
        
        try:
            import base64
            credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
            headers = {"Authorization": f"Basic {credentials}"}
            response = requests.get(
                "https://api.bitbucket.org/2.0/user",
                headers=headers,
                timeout=5
            )
            
            if response.status_code == 200:
                self.credentials['bitbucket'] = {
                    'username': username,
                    'password': password,
                    'type': 'basic_auth'
                }
                self._save_credentials()
                console.print("[bright_green]✓ Autenticación Bitbucket exitosa[/bright_green]")
                return True
            else:
                console.print("[red]✗ Credenciales inválidas[/red]")
                return False
        except Exception as e:
            console.print(f"[red]✗ Error de conexión: {e}[/red]")
            return False
    
    def get_platform_from_url(self, url: str) -> str:
        """Detectar plataforma desde URL"""
        url_lower = url.lower()
        if "github" in url_lower:
            return "github"
        elif "gitlab" in url_lower:
            return "gitlab"
        elif "bitbucket" in url_lower:
            return "bitbucket"
        return "unknown"
    
    def is_authenticated(self, platform: str) -> bool:
        """Verificar si está autenticado en una plataforma"""
        return platform.lower() in self.credentials
    
    def get_credentials(self, platform: str) -> Optional[Dict]:
        """Obtener credenciales de una plataforma"""
        return self.credentials.get(platform.lower())
    
    def check_and_authenticate(self, platforms: set) -> None:
        """Verificar y solicitar autenticación para plataformas necesarias"""
        console.print()
        console.print("═" * 50)
        console.print("[bold]🔐 Verificación de Credenciales[/bold]")
        console.print("═" * 50)
        
        missing_auth = []
        
        for platform in platforms:
            platform_lower = platform.lower()
            if self.is_authenticated(platform_lower):
                console.print(f"[bright_green]✓[/bright_green] {platform}: Autenticado")
            else:
                console.print(f"[yellow]⚠[/yellow] {platform}: Sin autenticar")
                missing_auth.append(platform_lower)
        
        if missing_auth:
            console.print()
            console.print("[bold yellow]Se requiere autenticación para continuar[/bold yellow]")
            
            for platform in missing_auth:
                if platform == "github":
                    self.authenticate_github()
                elif platform == "gitlab":
                    self.authenticate_gitlab()
                elif platform == "bitbucket":
                    self.authenticate_bitbucket()

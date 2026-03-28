"""
Módulo de clonación de repositorios
"""

import asyncio
import subprocess
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
import time
from rich.console import Console

console = Console()


@dataclass
class CloneResult:
    """Resultado de una clonación"""
    url: str
    platform: str
    success: bool
    error: Optional[str] = None
    duration: float = 0.0
    size_mb: float = 0.0
    path: Optional[Path] = None


class CloneManager:
    """Gestor de clonación de repositorios"""
    
    def __init__(self, base_dir: Path = None, max_concurrent: int = 8):
        self.base_dir = base_dir or Path.home() / "clones"
        self.max_concurrent = max_concurrent
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.results: List[CloneResult] = []
        self.active_repos: Dict[str, float] = {}  # {url: progreso%}
    
    def detect_platform(self, url: str) -> str:
        """Detectar plataforma desde URL"""
        url_lower = url.lower()
        if "github" in url_lower:
            return "github"
        elif "gitlab" in url_lower:
            return "gitlab"
        elif "bitbucket" in url_lower:
            return "bitbucket"
        elif "git" in url_lower:
            return "generic"
        return "unknown"
    
    async def clone_repository(self, url: str, credentials: Optional[Dict] = None) -> CloneResult:
        """Clonar un repositorio de forma asincrónica"""
        
        platform = self.detect_platform(url)
        repo_name = url.split("/")[-1].replace(".git", "")
        repo_path = self.base_dir / platform / repo_name
        
        # Evitar duplicados
        if repo_path.exists():
            repo_path = self.base_dir / platform / f"{repo_name}_{int(time.time())}"
        
        repo_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Preparar credenciales en la URL si es necesario
        clone_url = url
        if credentials and credentials.get('type') == 'token':
            token = credentials.get('token')
            if platform == "github":
                clone_url = url.replace("https://", f"https://x-access-token:{token}@")
            elif platform == "gitlab":
                clone_url = url.replace("https://", f"https://oauth2:{token}@")
        
        start_time = time.time()
        
        try:
            # Ejecutar git clone de forma asincrónica
            process = await asyncio.create_subprocess_exec(
                "git", "clone", "--depth", "1", clone_url, str(repo_path),
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            # Actualizar progreso
            self.active_repos[url] = 50.0
            
            # Esperar finalización
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=300)
            
            duration = time.time() - start_time
            
            if process.returncode == 0:
                # Calcular tamaño
                size_mb = self._get_dir_size(repo_path) / (1024 * 1024)
                self.active_repos[url] = 100.0
                
                return CloneResult(
                    url=url,
                    platform=platform,
                    success=True,
                    duration=duration,
                    size_mb=size_mb,
                    path=repo_path
                )
            else:
                error_msg = stderr.decode('utf-8', errors='ignore')
                if "Could not resolve host" in error_msg or "Network" in error_msg:
                    error = "Error de red: No se pudo conectar"
                elif "Permission denied" in error_msg or "403" in error_msg:
                    error = "Error de permisos: Repositorio privado o acceso denegado"
                elif "404" in error_msg or "not found" in error_msg:
                    error = "Repositorio no encontrado"
                else:
                    error = error_msg[:100]
                
                return CloneResult(
                    url=url,
                    platform=platform,
                    success=False,
                    error=error,
                    duration=time.time() - start_time
                )
        
        except asyncio.TimeoutError:
            return CloneResult(
                url=url,
                platform=platform,
                success=False,
                error="Timeout: La clonación tardó demasiado (>5 minutos)",
                duration=time.time() - start_time
            )
        except Exception as e:
            return CloneResult(
                url=url,
                platform=platform,
                success=False,
                error=str(e)[:100],
                duration=time.time() - start_time
            )
    
    async def clone_multiple(self, urls: List[str], credentials_map: Dict[str, Dict] = None) -> List[CloneResult]:
        """Clonar múltiples repositorios de forma concurrente"""
        
        if credentials_map is None:
            credentials_map = {}
        
        # Crear tasks con límite de concurrencia
        semaphore = asyncio.Semaphore(self.max_concurrent)
        
        async def bounded_clone(url):
            async with semaphore:
                platform = self.detect_platform(url)
                creds = credentials_map.get(platform)
                result = await self.clone_repository(url, creds)
                self.results.append(result)
                return result
        
        tasks = [bounded_clone(url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Filtrar excepciones
        return [r for r in results if isinstance(r, CloneResult)]
    
    def _get_dir_size(self, path: Path) -> int:
        """Calcular tamaño total de un directorio"""
        total = 0
        try:
            for entry in path.rglob("*"):
                if entry.is_file():
                    total += entry.stat().st_size
        except:
            pass
        return total
    
    def get_results_summary(self) -> Dict:
        """Obtener resumen de resultados"""
        successful = [r for r in self.results if r.success]
        failed = [r for r in self.results if not r.success]
        
        return {
            "total": len(self.results),
            "successful": len(successful),
            "failed": len(failed),
            "total_size_mb": sum(r.size_mb for r in successful),
            "total_duration": sum(r.duration for r in self.results),
            "successful_repos": successful,
            "failed_repos": failed
        }


async def clone_repos_concurrent(urls: List[str], max_concurrent: int = 8, 
                                  credentials_map: Dict[str, Dict] = None) -> List[CloneResult]:
    """Función auxiliar para clonar repos de forma concurrente"""
    manager = CloneManager(max_concurrent=max_concurrent)
    return await manager.clone_multiple(urls, credentials_map)

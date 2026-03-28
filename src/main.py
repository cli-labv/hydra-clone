"""
HydraClone CLI - Herramienta de Clonación Masiva
"""

import asyncio
import sys
from pathlib import Path
from typing import List, Set
import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

# Agregar rutas al path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Importar módulos propios
from modules.hydra_banner import show_startup_banner
from modules.hydra_progress import show_clone_progress, show_report_info
from modules.auth import AuthManager
from modules.clone import CloneManager
from modules.reports import ReportGenerator
from config import CLONES_DIR, REPORTS_DIR

console = Console()


class CloneMasterCLI:
    """Clase principal del CLI"""
    
    def __init__(self):
        self.auth_manager = AuthManager()
        self.clone_manager = CloneManager()
        self.report_generator = ReportGenerator()
        self.urls: List[str] = []
        self.credentials_map = {}
    
    def input_repositories(self) -> List[str]:
        """
        Solicitar URLs de repositorios con coma automática
        El usuario pega URLs y se agregan automáticamente con comas
        """
        console.print()
        console.print("═" * 60)
        console.print("[bold cyan]📥 Ingresa las URLs de los Repositorios[/bold cyan]")
        console.print("═" * 60)
        
        console.print()
        console.print("[dim]Instrucciones:[/dim]")
        console.print("  • Pega una URL por línea")
        console.print("  • La coma se agregará automáticamente")
        console.print("  • Escribe 'done' o 'd' cuando termines")
        console.print()
        
        urls = []
        counter = 1
        
        while True:
            prompt_text = f"[cyan]URL {counter}[/cyan]"
            url = console.input(prompt_text)
            
            if url.lower() in {"done", "d"}:
                break
            
            # Validar que sea una URL
            url = url.strip()
            if url and (url.startswith("http") or url.startswith("git@")):
                urls.append(url)
                console.print(f"  [bright_green]✓[/bright_green] Agregada: {url}")
                counter += 1
            elif url:
                console.print(f"  [red]✗ URL inválida, debe empezar con http o git@[/red]")
        
        return urls
    
    def detect_platforms(self, urls: List[str]) -> Set[str]:
        """Detectar plataformas de las URLs"""
        console.print()
        console.print("═" * 60)
        console.print("[bold cyan]🔍 Escaneo de Plataformas[/bold cyan]")
        console.print("═" * 60)
        
        platforms = set()
        
        for url in urls:
            platform = self.clone_manager.detect_platform(url)
            platforms.add(platform)
            
            platform_emoji = {
                "github": "🐙",
                "gitlab": "🦊",
                "bitbucket": "🪣",
                "generic": "📦",
                "unknown": "❓"
            }.get(platform, "❓")
            
            console.print(f"  {platform_emoji} {url[:50]:50} → {platform.upper()}")
        
        console.print()
        console.print(f"[dim]Total de repositorios: {len(urls)} | Plataformas: {', '.join(sorted(platforms))}")
        
        return platforms
    
    def check_authentication(self, platforms: Set[str]) -> None:
        """Verificar y solicitar autenticación"""
        self.auth_manager.check_and_authenticate(platforms)
        
        # Mapear credenciales
        for platform in platforms:
            creds = self.auth_manager.get_credentials(platform)
            if creds:
                self.credentials_map[platform] = creds
    
    async def start_cloning(self, urls: List[str]) -> None:
        """Iniciar el proceso de clonación masiva"""
        
        console.print()
        console.print("═" * 60)
        console.print("[bold bright_magenta]🚀 Iniciando Clonación Masiva[/bold bright_magenta]")
        console.print("═" * 60)
        console.print()
        
        total = len(urls)
        completed = 0
        
        # Configurar el gestor de clonación
        self.clone_manager = CloneManager(max_concurrent=8)
        
        # Crear tareas de clonación
        tasks = []
        for idx, url in enumerate(urls, 1):
            platform = self.clone_manager.detect_platform(url)
            creds = self.credentials_map.get(platform)
            
            # Simular que se están procesando
            self.clone_manager.active_repos[url] = 0.0
            
            task = self._clone_with_progress(url, creds, idx, total)
            tasks.append(task)
        
        # Ejecutar clonaciones de forma concurrente (máx 8)
        semaphore = asyncio.Semaphore(8)
        
        async def bounded_task(task, url):
            async with semaphore:
                await task
                nonlocal completed
                completed += 1
        
        bounded_tasks = [bounded_task(task, url) for task, url in zip(tasks, urls)]
        
        # Ejecutar con animación de progreso
        await self._run_with_animation(bounded_tasks, total)
    
    async def _clone_with_progress(self, url: str, creds, idx: int, total: int) -> None:
        """Clonar un repositorio y actualizar progreso"""
        platform = self.clone_manager.detect_platform(url)
        result = await self.clone_manager.clone_repository(url, creds)
        self.clone_manager.results.append(result)
    
    async def _run_with_animation(self, tasks, total: int) -> None:
        """Ejecutar tareas con animación de progreso"""
        
        # Ejecutar tareas
        await asyncio.gather(*tasks)
        
        # Mostrar resultados finales
        console.clear()
        
        successful = len([r for r in self.clone_manager.results if r.success])
        failed = len([r for r in self.clone_manager.results if not r.success])
        
        # Animación final
        final_bar = "█" * 20
        console.print()
        console.print(f"📦 Clonando repositorios... [{final_bar}] 100% ({total}/{total})")
        console.print()
        
        console.print("[bright_green]✓ ¡Clonación completada![/bright_green]")
        console.print()
        console.print(f"  Exitosos: [bright_green]{successful}[/bright_green]")
        console.print(f"  Fallidos: [bright_red]{failed}[/bright_red]")
        console.print()
    
    def generate_report(self) -> None:
        """Generar reporte final con estilo HydraClone"""
        
        if not self.clone_manager.results:
            return
        
        # Mostrar progreso estilizado con HydraClone
        show_clone_progress(
            self.clone_manager.results,
            len(self.clone_manager.results)
        )
        
        # Generar reporte en Markdown
        report_path = self.report_generator.generate_report(
            self.clone_manager.results,
            title="HydraClone - Reporte de Clonación"
        )
        
        # Mostrar información del reporte
        show_report_info(str(report_path))
        
        console.print("[bright_green]✨ ¡Proceso completado![/bright_green]")
        console.print()
    
    @staticmethod
    def _format_time(seconds: float) -> str:
        """Formatear tiempo"""
        if seconds < 60:
            return f"{seconds:.1f}s"
        elif seconds < 3600:
            minutes = seconds // 60
            secs = seconds % 60
            return f"{int(minutes)}m {secs:.0f}s"
        else:
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            return f"{int(hours)}h {int(minutes)}m"
    
    async def run(self) -> None:
        """Ejecutar flujo principal del CLI"""
        
        # Animación de bienvenida (nuevo banner HydraClone)
        show_startup_banner(show_help=False)
        
        # Solicitar URLs
        self.urls = self.input_repositories()
        
        if not self.urls:
            console.print("[red]❌ No se ingresaron repositorios[/red]")
            return
        
        # Detectar plataformas
        platforms = self.detect_platforms(self.urls)
        
        # Verificar autenticación
        self.check_authentication(platforms)
        
        # Confirmar antes de clonar
        console.print()
        console.print(f"[bold]¿Deseas continuar con la clonación de {len(self.urls)} repositorios?[/bold]")
        
        confirm = Prompt.ask("Confirma (s/n)", choices=["s", "n"], default="s")
        
        if confirm.lower() != "s":
            console.print("[yellow]Operación cancelada[/yellow]")
            return
        
        # Iniciar clonación
        await self.start_cloning(self.urls)
        
        # Generar reporte
        self.generate_report()


def main():
    """Punto de entrada principal"""
    cli = CloneMasterCLI()
    
    try:
        asyncio.run(cli.run())
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️  Operación cancelada por el usuario[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[red]❌ Error: {e}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()

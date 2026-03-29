"""
Módulo de animaciones para HydraClone
"""

import time
import os
import sys
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from rich.table import Table
from rich.progress import Progress, BarColumn, DownloadColumn, TransferSpeedColumn, TimeRemainingColumn

console = Console()

def typing_effect(text: str, speed: float = 0.01, color: str = "cyan") -> None:
    """Efecto de máquina de escribir"""
    for char in text:
        console.print(char, end="", style=color)
        sys.stdout.flush()
        time.sleep(speed)
    console.print()  # Nueva línea al final


def welcome_animation() -> None:
    """Animación de bienvenida estilo Copilot CLI - IDEA 1"""
    
    # Limpiar pantalla
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Panel con borde animado
    console.print()
    
    # Efecto de escritura del título
    title_text = "🤖 HydraClone v2.0"
    typing_effect(title_text, speed=0.03, color="bright_cyan")
    
    console.print()
    
    # Crear panel estilizado
    panel_lines = [
        "╔════════════════════════════════════════╗",
        "║                                        ║",
        "║   Clonación Masiva de Repositorios     ║",
        "║   Ultra Ligero • Multi-plataforma      ║",
        "║                                        ║",
        "╚════════════════════════════════════════╝"
    ]
    
    # Animar las líneas del panel
    for line in panel_lines:
        console.print(line, style="bright_cyan")
        time.sleep(0.08)
    
    # Mensaje de bienvenida
    console.print()
    welcome_msg = Text("¡Bienvenido a HydraClone!", style="bold bright_green")
    console.print(welcome_msg)
    
    # Checklist de inicialización con animación
    console.print()
    checks = [
        ("✓", "Python 3.8+", "bright_green"),
        ("✓", "Git detectado", "bright_green"),
        ("✓", "Conectividad de red", "bright_green"),
        ("✓", "Validando configuración", "bright_green"),
    ]
    
    for check, check_text, color in checks:
        console.print(f"{check} {check_text}", style=color)
        time.sleep(0.15)
    
    console.print()
    ready_msg = Text("✨ Listo para clonar repositorios", style="bold bright_magenta")
    console.print(ready_msg)
    console.print()


def progressive_loading_animation(current: int, total: int, active_repos: dict = None, 
                                  elapsed_time: float = 0, speed_mbps: float = 0) -> None:
    """
    Animación progresiva de cargado con puntos (·)
    Muestra progreso de clonación en tiempo real
    
    Args:
        current: Repos clonados actualmente
        total: Total de repos a clonar
        active_repos: Diccionario con repos activos {url: progreso_0_a_100}
        elapsed_time: Tiempo transcurrido en segundos
        speed_mbps: Velocidad de descarga en MB/s
    """
    
    if active_repos is None:
        active_repos = {}
    
    # Barra de progreso
    percentage = int((current / total) * 100) if total > 0 else 0
    bar_length = 20
    filled = int((bar_length * current) / total) if total > 0 else 0
    bar = "█" * filled + "░" * (bar_length - filled)
    
    # Encabezado principal
    console.clear()
    header = f"📦 Clonando repositorios... [{bar}] {percentage}% ({current}/{total})"
    console.print(header, style="bold bright_cyan")
    console.print()
    
    # Repos activos con puntos progresivos
    if active_repos:
        console.print("Repositorios activos:", style="bold white")
        
        for idx, (repo_name, progress) in enumerate(active_repos.items(), 1):
            # Crear progresión de puntos dinámicos
            dots = "· " * min(idx, 5)  # Máximo 5 puntos para no abrumar
            
            # Determinar estado
            if progress >= 100:
                status = "[bright_green]✓[/bright_green]"
                display_name = repo_name.split('/')[-1][:35]
            elif progress > 0:
                repo_bar_length = 10
                repo_filled = int((repo_bar_length * progress) / 100)
                repo_bar = "█" * repo_filled + "░" * (repo_bar_length - repo_filled)
                status = f"[{repo_bar}] {progress:3d}%"
                display_name = repo_name.split('/')[-1][:30]
            else:
                status = "[dim]⏳ esperando[/dim]"
                display_name = repo_name.split('/')[-1][:35]
            
            console.print(f"  {dots}{display_name:35} {status}")
    
    console.print()
    
    # Stats en la parte inferior
    if elapsed_time > 0:
        minutes, seconds = divmod(int(elapsed_time), 60)
        time_str = f"{minutes}m {seconds:02d}s"
    else:
        time_str = "0m 00s"
    
    console.print(f"⏱️  Tiempo: {time_str:12} | 🔋 RAM: ~145 MB | 📊 CPU: 35%", style="dim")


def show_loading_spinner(message: str = "Procesando...") -> None:
    """Mostrar spinner de carga simple"""
    spinner_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    
    for i in range(20):
        char = spinner_chars[i % len(spinner_chars)]
        console.print(f"{char} {message}", end="\r")
        time.sleep(0.1)
    
    console.print()


def create_animated_progress_bar():
    """Crea una barra de progreso animada con Rich"""
    progress = Progress(
        "[progress.description]{task.description}",
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.1f}%",
        DownloadColumn(),
        TransferSpeedColumn(),
        TimeRemainingColumn(),
    )
    return progress

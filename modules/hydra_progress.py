#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🐉 HydraClone - Progress Display Module
Módulo para mostrar progreso de clonado masivo con interfaz compacta y uniforme.

Uso:
    from hydra_progress import show_clone_progress
    show_clone_progress(repos_list)

Requisitos:
    pip install colorama tqdm wcwidth
"""

import sys
import time
import os
import re
from colorama import init, Fore, Style

try:
    from tqdm import tqdm
except ImportError:
    tqdm = None

try:
    from wcwidth import wcswidth
except ImportError:
    def wcswidth(s):
        return len(s)

# Inicializar colorama
init()

# ============================================================================
# CONFIGURACIÓN VISUAL
# ============================================================================
BOX_WIDTH = 70          # Ancho uniforme de todos los cuadros
BOX_INDENT = 2          # Indentación lateral de los cuadros
HYDRA_INDENT = 15       # Indentación del ASCII art de la hydra

# Hydra de 5 cabezas - Estado final (ASCII art sólido y cerrado)
HYDRA_FINAL = [
    Fore.GREEN + Style.BRIGHT + "███████         ███████         ███████" + Style.RESET_ALL,
    Fore.GREEN + Style.BRIGHT + "███████████████████████████████████████" + Style.RESET_ALL,
    Fore.GREEN + Style.BRIGHT + "████░░███████████████████████░░████████" + Style.RESET_ALL,
    Fore.GREEN + Style.BRIGHT + "████░░░░█████████████████████░░░░██████" + Style.RESET_ALL,
    Fore.GREEN + Style.BRIGHT + "████░░◉░░█████████████████░░◉░░████████" + Style.RESET_ALL,
    Fore.GREEN + Style.BRIGHT + "█████░░░░░███████████████░░░░░█████████" + Style.RESET_ALL,
    Fore.GREEN + Style.BRIGHT + " ████████████████████████████████████" + Style.RESET_ALL,
    Fore.GREEN + Style.BRIGHT + "  ██████████████████████████████████" + Style.RESET_ALL,
    Fore.GREEN + Style.BRIGHT + "   ████████████████████████████████" + Style.RESET_ALL,
    Fore.GREEN + Style.BRIGHT + "    ██████████████████████████████" + Style.RESET_ALL,
]

# ============================================================================
# FUNCIONES DE UTILIDAD
# ============================================================================

def clear_screen():
    """Limpia la pantalla de la terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def strip_ansi_codes(text: str) -> str:
    """Elimina todos los códigos ANSI de un texto."""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def get_display_width(text: str) -> int:
    """Calcula el ancho real de visualización."""
    clean = strip_ansi_codes(text)
    width = wcswidth(clean)
    return width if width >= 0 else len(clean)

def pad_to_width(content: str, target_width: int) -> str:
    """Rellena contenido con espacios para alcanzar el ancho objetivo."""
    current_width = get_display_width(content)
    padding_needed = target_width - current_width
    if padding_needed < 0:
        return strip_ansi_codes(content)[:target_width] + Style.RESET_ALL
    return content + " " * padding_needed

# ============================================================================
# FUNCIONES DE DIBUJO
# ============================================================================

def draw_uniform_box(title: str, content_lines: list = None, 
                     width: int = BOX_WIDTH, indent: int = BOX_INDENT):
    """
    Dibuja un cuadro uniforme y completamente cerrado.
    """
    indent_str = " " * indent
    
    # Caracteres de bordes
    top_border = "╔" + "═" * width + "╗"
    bottom_border = "╚" + "═" * width + "╝"
    separator = "╠" + "═" * width + "╣"
    
    # Borde superior
    print(Fore.CYAN + indent_str + top_border + Style.RESET_ALL)
    
    # Línea de título centrado
    title_width = get_display_width(title)
    total_padding = width - title_width
    left_pad = total_padding // 2
    right_pad = total_padding - left_pad
    title_line = " " * left_pad + title + " " * right_pad
    print(Fore.CYAN + indent_str + "║" + Style.RESET_ALL + title_line + Fore.CYAN + "║" + Style.RESET_ALL)
    
    # Contenido (si existe)
    if content_lines:
        print(Fore.CYAN + indent_str + separator + Style.RESET_ALL)
        for content in content_lines:
            padded = pad_to_width(content, width)
            print(Fore.CYAN + indent_str + "║" + Style.RESET_ALL + padded + Fore.CYAN + "║" + Style.RESET_ALL)
    
    # Borde inferior
    print(Fore.CYAN + indent_str + bottom_border + Style.RESET_ALL)

def print_hydra_art(indent: int = HYDRA_INDENT):
    """Imprime la hydra ASCII art."""
    print()
    indent_str = " " * indent
    for line in HYDRA_FINAL:
        print(indent_str + line)
    print()

# ============================================================================
# FUNCIÓN PRINCIPAL DE PROGRESO
# ============================================================================

def show_clone_progress(clone_results, total_repos: int):
    """
    Muestra progreso y resultados de clonación masiva.
    
    Args:
        clone_results: Lista de resultados de CloneResult
        total_repos: Total de repositorios a clonar
    
    Returns:
        dict: Resumen de resultados
    """
    try:
        successful = [r for r in clone_results if r.success]
        failed = [r for r in clone_results if not r.success]
        
        # Pantalla final
        clear_screen()
        
        # Banner de completado
        draw_uniform_box("🐉 HydraClone - Clonación Completada", width=BOX_WIDTH, indent=BOX_INDENT)
        print()
        
        # Hydra final ASCII art
        print_hydra_art()
        
        # Estadísticas principales
        total_size = sum(r.size_mb for r in successful)
        total_time = sum(r.duration for r in clone_results)
        success_rate = (len(successful) / total_repos * 100) if total_repos > 0 else 0
        
        stats = [
            f"{Fore.GREEN}✅{Style.RESET_ALL} Repositorios Clonados: {Fore.WHITE}{len(successful)}/{total_repos}{Style.RESET_ALL}",
            f"{Fore.RED}❌{Style.RESET_ALL} Repositorios Fallidos: {Fore.WHITE}{len(failed)}{Style.RESET_ALL}",
            f"{Fore.CYAN}📦{Style.RESET_ALL} Tamaño Total: {Fore.WHITE}{total_size:.2f} MB{Style.RESET_ALL}",
            f"{Fore.YELLOW}⏱️{Style.RESET_ALL} Tiempo Total: {Fore.WHITE}{format_time(total_time)}{Style.RESET_ALL}",
            f"{Fore.CYAN}📊{Style.RESET_ALL} Tasa de Éxito: {Fore.GREEN}{success_rate:.1f}%{Style.RESET_ALL}",
        ]
        
        draw_uniform_box("📊 Estadísticas de Clonación", content_lines=stats, 
                        width=BOX_WIDTH, indent=BOX_INDENT)
        print()
        
        # Mostrar repositorios exitosos
        if successful:
            print(Fore.GREEN + "  ✅ Repositorios Clonados Exitosamente:" + Style.RESET_ALL)
            for result in successful[:5]:  # Mostrar primeros 5
                repo_name = result.url.split("/")[-1].replace(".git", "")
                print(f"     {Fore.GREEN}✓{Style.RESET_ALL} {repo_name} ({result.size_mb:.2f} MB)")
            if len(successful) > 5:
                print(f"     {Fore.DIM}... y {len(successful) - 5} más{Style.RESET_ALL}")
        
        print()
        
        # Mostrar repositorios con error
        if failed:
            print(Fore.RED + "  ❌ Repositorios con Error:" + Style.RESET_ALL)
            for result in failed[:3]:  # Mostrar primeros 3
                repo_name = result.url.split("/")[-1].replace(".git", "")
                error = result.error[:40] + "..." if len(result.error) > 40 else result.error
                print(f"     {Fore.RED}✗{Style.RESET_ALL} {repo_name}: {error}")
            if len(failed) > 3:
                print(f"     {Fore.DIM}... y {len(failed) - 3} más{Style.RESET_ALL}")
        
        print()
        
        return {
            'successful': len(successful),
            'failed': len(failed),
            'total_size': total_size,
            'total_time': total_time,
            'success_rate': success_rate
        }
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}  ⚠️  Clonación interrumpida por el usuario{Style.RESET_ALL}")
        return None
    except Exception as e:
        print(f"\n{Fore.RED}  ❌ Error: {str(e)}{Style.RESET_ALL}")
        return None

def format_time(seconds: float) -> str:
    """Formatea tiempo en segundos a formato legible."""
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

def show_report_info(report_path: str):
    """Muestra información del reporte generado."""
    print(Fore.CYAN + "  📄 Reporte Generado:" + Style.RESET_ALL)
    print(f"     {Fore.WHITE}{report_path}{Style.RESET_ALL}")
    print()

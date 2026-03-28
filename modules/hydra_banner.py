#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🐉 HydraClone - Animated Banner Module (v3.1.0)
Nuevo banner con animación de cabeza de hydra y texto dual HYDRA / CLONE.

Uso:
    from modules.hydra_banner import show_startup_banner
    show_startup_banner()

Requisitos:
    pip install colorama
"""

import os
import sys
import time
from colorama import Fore, Style, init

# Inicializar colorama con autoreset para evitar fugas de color
init(autoreset=True)


# ============================================================================
# UTILIDADES DE TERMINAL
# ============================================================================

def clear_screen():
    """Limpia la pantalla de forma compatible multiplataforma."""
    os.system("cls" if os.name == "nt" else "clear")


def type_text(text: str, delay: float = 0.001):
    """Efecto máquina de escribir ultrarrápido."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# ============================================================================
# TEXTOS BASE
# ============================================================================

HYDRA_TEXT = r"""
██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗ 
██║  ██║╚██╗ ██╔╝██╔══██╗██╔══██╗██╔══██╗
███████║ ╚████╔╝ ██║  ██║██████╔╝███████║
██╔══██║  ╚██╔╝  ██║  ██║██╔══██╗██╔══██║
██║  ██║   ██║   ██████╔╝██║  ██║██║  ██║
╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
"""

CLONE_TEXT = r"""
 ██████╗██╗      ██████╗ ███╗   ██╗███████╗
██╔════╝██║     ██╔═══██╗████╗  ██║██╔════╝
██║     ██║     ██║   ██║██╔██╗ ██║█████╗  
██║     ██║     ██║   ██║██║╚██╗██║██╔══╝  
╚██████╗███████╗╚██████╔╝██║ ╚████║███████╗
 ╚═════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
"""


# ============================================================================
# CABEZA DE HYDRA (2 ESTADOS)
# ============================================================================

SNAKE_HEAD_1 = [
    "          ███████",
    "        ███████████",
    "      ███████████████",
    "     █████████████████",
    "    ████░░████████░░██",
    "   ███░░░░████████░░░░██",
    "   ███░░◉░░██████░░◉░░██",
    "   ████░░░░██████░░░░███",
    "    ███████████████████",
    "     █████████████████",
    "      ███████████████",
    "        ███████████",
    "          ███████",
]

# Ojos parpadeando
SNAKE_HEAD_2 = [line.replace("◉", "░") for line in SNAKE_HEAD_1]


def draw_snake(frame):
    """Dibuja la cabeza de la hydra en un frame."""
    for line in frame:
        print(Fore.GREEN + Style.BRIGHT + line)


# ============================================================================
# ANIMACIÓN
# ============================================================================

def animate_snake():
    """Anima la cabeza de la hydra con parpadeo."""
    for _ in range(4):
        clear_screen()
        print(Fore.CYAN + HYDRA_TEXT + Style.RESET_ALL)
        draw_snake(SNAKE_HEAD_1)
        time.sleep(0.25)

        clear_screen()
        print(Fore.CYAN + HYDRA_TEXT + Style.RESET_ALL)
        draw_snake(SNAKE_HEAD_2)
        time.sleep(0.15)


def _render_final_frame():
    """Muestra la pantalla final del banner."""
    clear_screen()
    print(Fore.CYAN + HYDRA_TEXT + Style.RESET_ALL)
    draw_snake(SNAKE_HEAD_1)

    # Efecto de escritura para el texto CLONE
    type_text(Fore.CYAN + CLONE_TEXT + Style.RESET_ALL, 0.0005)

    # Texto informativo
    print(
        Fore.GREEN
        + """
────────────────────────────────────────────────────────

  🚀 Mass repository cloner
  🐍 Watching targets...

  ✓ Multi-threaded cloning
  ✓ Progress tracking
  ✓ Error recovery
  ✓ Auth management

────────────────────────────────────────────────────────
"""
        + Style.RESET_ALL
    )

    # Prompt
    print(Fore.GREEN + "  hydra:~$ " + Style.RESET_ALL, end="")


# ============================================================================
# INTERFAZ PÚBLICA
# ============================================================================

def show_startup_banner(show_help: bool = False):
    """
    Muestra el banner animado de HydraClone.
    El parámetro show_help se ignora en esta versión (banner compacto).
    """
    try:
        clear_screen()
        # Efecto de escritura inicial
        type_text(Fore.CYAN + HYDRA_TEXT + Style.RESET_ALL, 0.0005)
        # Animación de parpadeo
        animate_snake()
        # Pantalla final
        _render_final_frame()
        # Breve pausa antes de continuar
        time.sleep(0.5)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}  Banner interrupted{Style.RESET_ALL}")
    except Exception as exc:
        print(f"\n{Fore.RED}  Error loading banner: {exc}{Style.RESET_ALL}")
        show_static_banner()


def show_static_banner():
    """Versión estática simple como fallback rápido."""
    clear_screen()
    print(Fore.CYAN + HYDRA_TEXT + Style.RESET_ALL)
    draw_snake(SNAKE_HEAD_1)
    print(Fore.CYAN + CLONE_TEXT + Style.RESET_ALL)
    print(Fore.GREEN + "  hydra:~$ " + Style.RESET_ALL, end="")


if __name__ == "__main__":
    show_startup_banner()

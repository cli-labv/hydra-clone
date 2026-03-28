#!/bin/bash
# -*- coding: utf-8 -*-
################################################################################
# 🐉 HydraClone Startup Script
# Punto de entrada único para instalar o ejecutar el proyecto
# Uso: ./start.sh
################################################################################

set -e

# Colores para la terminal
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # Sin color

# Obtener directorio del proyecto
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

################################################################################
# FUNCIONES AUXILIARES
################################################################################

show_banner() {
    clear
    echo -e "${CYAN}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${NC}         ${WHITE}🐉 HydraClone - Mass Repository Cloner${NC}           ${CYAN}║${NC}"
    echo -e "${CYAN}╚════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

show_menu() {
    echo -e "${BLUE}¿Qué deseas hacer?${NC}"
    echo ""
    echo -e "  ${GREEN}1)${NC} 📦 ${WHITE}Instalar dependencias${NC}     (primera vez)"
    echo -e "  ${GREEN}2)${NC} ▶️  ${WHITE}Ejecutar aplicación${NC}       (usar HydraClone)"
    echo -e "  ${GREEN}3)${NC} 🧪 ${WHITE}Ejecutar pruebas${NC}           (testing)"
    echo -e "  ${GREEN}4)${NC} ❌ ${WHITE}Salir${NC}"
    echo ""
}

install_dependencies() {
    echo -e "\n${CYAN}→${NC} Ejecutando instalación..."
    bash "$PROJECT_DIR/scripts/install.sh"
    echo -e "${GREEN}✓ Instalación completada${NC}\n"
}

run_application() {
    echo -e "\n${CYAN}→${NC} Iniciando HydraClone..."
    bash "$PROJECT_DIR/scripts/run.sh"
}

run_tests() {
    echo -e "\n${CYAN}→${NC} Ejecutando pruebas..."
    bash "$PROJECT_DIR/scripts/test.sh"
    echo -e "${GREEN}✓ Pruebas completadas${NC}\n"
}

check_python() {
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}✗ Python 3 no está instalado${NC}"
        echo -e "${YELLOW}  Instálalo con: sudo apt install python3 python3-venv${NC}"
        exit 1
    fi
}

check_git() {
    if ! command -v git &> /dev/null; then
        echo -e "${RED}✗ Git no está instalado${NC}"
        echo -e "${YELLOW}  Instálalo con: sudo apt install git${NC}"
        exit 1
    fi
}

check_requirements() {
    check_python
    check_git
    echo -e "${GREEN}✓ Requisitos cumplidos${NC}"
}

################################################################################
# FLUJO PRINCIPAL
################################################################################

main() {
    show_banner
    check_requirements
    
    while true; do
        show_menu
        read -p "$(echo -e ${CYAN}Selecciona opción${NC}): ) " option
        
        case $option in
            1)
                install_dependencies
                ;;
            2)
                run_application
                ;;
            3)
                run_tests
                ;;
            4)
                echo -e "\n${YELLOW}👋 ¡Hasta luego!${NC}\n"
                exit 0
                ;;
            *)
                echo -e "${RED}✗ Opción inválida${NC}"
                sleep 1
                ;;
        esac
        
        read -p "$(echo -e ${CYAN}Presiona Enter para continuar...${NC})"
        show_banner
    done
}

# Ejecutar
main

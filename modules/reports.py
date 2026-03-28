"""
Módulo de generación de reportes en Markdown
"""

from pathlib import Path
from typing import List, Dict
from datetime import datetime
import sys

# Imports relativos
from modules.clone import CloneResult

# Configuración
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from config import REPORTS_DIR


class ReportGenerator:
    """Generador de reportes en Markdown"""
    
    def __init__(self, output_dir: Path = None):
        self.output_dir = output_dir or REPORTS_DIR
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_report(self, results: List[CloneResult], title: str = "Clone Master Report") -> Path:
        """Generar reporte en Markdown"""
        
        successful = [r for r in results if r.success]
        failed = [r for r in results if not r.success]
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_path = self.output_dir / f"clone-report_{timestamp}.md"
        
        report_content = self._build_report(
            title=title,
            successful=successful,
            failed=failed,
            total=len(results),
            timestamp=datetime.now()
        )
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        return report_path
    
    def _build_report(self, title: str, successful: List[CloneResult], 
                     failed: List[CloneResult], total: int, timestamp: datetime) -> str:
        """Construir contenido del reporte"""
        
        total_size = sum(r.size_mb for r in successful)
        total_time = sum(r.duration for r in successful) + sum(r.duration for r in failed)
        success_rate = (len(successful) / total * 100) if total > 0 else 0
        
        report = f"""# {title}

**Fecha y Hora:** {timestamp.strftime("%Y-%m-%d %H:%M:%S")}

---

## 📊 Resumen General

| Métrica | Valor |
|---------|-------|
| **Total de Repositorios** | {total} |
| **Exitosos** | {len(successful)} ✅ |
| **Fallidos** | {len(failed)} ❌ |
| **Tasa de Éxito** | {success_rate:.1f}% |
| **Tamaño Total** | {total_size:.2f} MB |
| **Tiempo Total** | {self._format_duration(total_time)} |

---

## ✅ Repositorios Clonados Exitosamente ({len(successful)})

"""
        
        if successful:
            report += "| Repositorio | Plataforma | Tamaño | Tiempo | Ubicación |\n"
            report += "|-------------|-----------|--------|--------|----------|\n"
            
            for result in sorted(successful, key=lambda x: x.url):
                repo_name = result.url.split("/")[-1].replace(".git", "")
                platform = result.platform.upper()
                size = f"{result.size_mb:.2f} MB"
                duration = self._format_duration(result.duration)
                path = str(result.path)
                
                report += f"| {repo_name} | {platform} | {size} | {duration} | `{path}` |\n"
        else:
            report += "*No hay repositorios clonados exitosamente.*\n"
        
        report += f"\n---\n\n## ❌ Repositorios con Error ({len(failed)})\n\n"
        
        if failed:
            for result in sorted(failed, key=lambda x: x.url):
                repo_name = result.url.split("/")[-1].replace(".git", "")
                platform = result.platform.upper()
                error = result.error or "Error desconocido"
                
                report += f"### {repo_name}\n"
                report += f"- **Plataforma:** {platform}\n"
                report += f"- **URL:** `{result.url}`\n"
                report += f"- **Error:** {error}\n"
                report += f"- **Tiempo:** {self._format_duration(result.duration)}\n\n"
        else:
            report += "*Todos los repositorios se clonaron exitosamente.*\n"
        
        report += "\n---\n\n## 📋 Detalles Técnicos\n\n"
        report += f"- **Herramienta:** Clone Master CLI v1.0\n"
        report += f"- **Repositorios Procesados:** {total}\n"
        report += f"- **Plataformas Detectadas:** {self._get_platforms(successful + failed)}\n"
        
        return report
    
    @staticmethod
    def _format_duration(seconds: float) -> str:
        """Formatear duración en segundos a string legible"""
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
    
    @staticmethod
    def _get_platforms(results: List[CloneResult]) -> str:
        """Obtener lista única de plataformas"""
        platforms = set(r.platform.upper() for r in results)
        return ", ".join(sorted(platforms)) if platforms else "N/A"

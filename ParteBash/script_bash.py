import argparse
import subprocess

# Función para ejecutar los scripts de Bash correspondientes
def ejecutar_comando(bash_comando):
    try:
        subprocess.run(bash_comando, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")

def main():
    parser = argparse.ArgumentParser(description="Script para monitoreo, tráfico de red, escaneo y análisis de rendimiento.")
    
    # Argumentos
    parser.add_argument("--monitoreo", action="store_true", help="Iniciar monitoreo de ancho de banda.")
    parser.add_argument("--trafico", action="store_true", help="Registrar tráfico de red.")
    parser.add_argument("--escaneo", action="store_true", help="Detectar dispositivos en la red.")
    parser.add_argument("--rendimiento", action="store_true", help="Analizar rendimiento de la red.")
    
    args = parser.parse_args()
    
    # Verificar las opciones seleccionadas
    if args.monitoreo:
        print("Ejecutando monitoreo de ancho de banda...")
        ejecutar_comando("bash monitoreo.sh")
    
    if args.trafico:
        print("Registrando tráfico de red...")
        ejecutar_comando("bash trafico_red.sh")
    
    if args.escaneo:
        print("Detectando dispositivos en la red...")
        ejecutar_comando("bash escaneo.sh")
    
    if args.rendimiento:
        print("Analizando rendimiento de la red...")
        ejecutar_comando("bash rendimiento.sh")
    
    if not (args.monitoreo or args.trafico or args.escaneo or args.rendimiento):
        print("Error: No se seleccionó ninguna opción válida. Usa --help para más detalles.")

if __name__ == "__main__":
    main()

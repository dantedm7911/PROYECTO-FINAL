import argparse
import subprocess
import sys

def ejecutar_script_powershell(path, api_key, limit, hidden_files_path):
    # Construimos el comando de PowerShell que se ejecutará
    powershell_script = ".\\script_principal.ps1"  # Asegúrate de poner la ruta correcta del script principal de PowerShell

    # Creamos los parámetros que pasaremos al script de PowerShell
    cmd = [
        "powershell", 
        "-ExecutionPolicy", "Bypass",  # Permite la ejecución de scripts
        "-File", powershell_script, 
        "-path", path, 
        "-apiKey", api_key, 
        "-limit", str(limit), 
        "-hiddenFilesPath", hidden_files_path
    ]
    
    try:
        # Ejecutamos el script de PowerShell
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el script de PowerShell: {e}")
        sys.exit(1)

def main():
    # Crear el parser para los argumentos
    parser = argparse.ArgumentParser(description="Ejecutar scripts de ciberseguridad.")
    
    parser.add_argument("-p", "--path", type=str, required=True, help="Ruta de los archivos para análisis.")
    parser.add_argument("-k", "--api_key", type=str, required=True, help="API Key de VirusTotal.")
    parser.add_argument("-l", "--limit", type=int, default=5, help="Número de procesos a mostrar en el script de PowerShell.")
    parser.add_argument("-hf", "--hidden_files_path", type=str, required=True, help="Ruta donde buscar archivos ocultos.")
    parser.add_argument("-o", "--option", type=int, choices=[1, 2, 3, 4], required=True, help="Selecciona la opción: 1 para ejecutar PowerShell, 2 para Bash, 3 para Python, 4 para salir.")

    args = parser.parse_args()

    # Ejecutar opción 1: PowerShell
    if args.option == 1:
        print(f"Ejecutando el script de PowerShell con los siguientes parámetros:")
        print(f"Ruta: {args.path}, API Key: {args.api_key}, Límite: {args.limit}, Ruta de Archivos Ocultos: {args.hidden_files_path}")
        ejecutar_script_powershell(args.path, args.api_key, args.limit, args.hidden_files_path)

if __name__ == "__main__":
    main()

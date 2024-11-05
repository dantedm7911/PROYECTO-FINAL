import subprocess
import sys

def ejecutar_script(script):
    try:
        subprocess.run(script, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el script: {e}")

def menu():
    while True:
        print("\nMenu de Opciones:")
        print("1. Correr script de Bash")
        print("2. Correr script de PowerShell")
        print("3. Correr script de Python")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            ejecutar_script("bash tu_script.sh")  # Cambia 'tu_script.sh' por el nombre correcto del script Bash
        elif opcion == '2':
            ejecutar_script("pwsh -File script.pia.ps1")  # Cambia 'tu_script.ps1' por la ruta correcta del script de PowerShell
        elif opcion == '3':
            ejecutar_script(f"{sys.executable} tu_script.py")  # Cambia 'tu_script.py' por la ruta correcta del script de Python
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

menu()

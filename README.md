# PROYECTO-FINAL

<span style="font-size: 1555px;">Texto con tamaño 20px</span>


## Herramienta de Ciberseguridad Multiplataforma

### Descripción
Este proyecto es una herramienta de ciberseguridad desarrollada para ejecutar y coordinar scripts en tres lenguajes distintos (Python, PowerShell y Bash) desde un solo menú en Python. La herramienta proporciona información útil sobre la seguridad de un sistema, permitiendo al usuario realizar diferentes análisis y consultas en función del sistema operativo o del lenguaje de script.

### Funcionalidades
La herramienta permite seleccionar entre las siguientes opciones:

Ejecutar un Script de Bash
Realiza una tarea de ciberseguridad mediante un script en Bash. Esta opción está orientada a sistemas basados en Unix/Linux, y brinda información específica sobre la seguridad del sistema.

### Requisitos previos
Antes de ejecutar el script, asegúrese de tener los siguientes archivos en el mismo directorio que el script principal:

**monitoreo.bash**
**trafico_red.sh**
**dispositivos.bash**
**rendimiento_red.sh**

 Cada uno de estos scripts realiza una tarea específica dentro del menú de opciones.
 Esto mostrará un menú interactivo en tu terminal con las siguientes opciones:

**1.Monitoreo de uso de ancho de banda**
Inicia el monitoreo en tiempo real del uso de ancho de banda en tu red.

**2.Registro de tráfico de red**
Comienza a registrar el tráfico de red en tu dispositivo.

**3.Detección de dispositivos en la red**
Detecta los dispositivos conectados a tu red local.

**4.Análisis de rendimiento de la red**
Realiza un análisis detallado del rendimiento de tu red.

       Explicación de las funciones
monitoreo: Esta función inicia el monitoreo en tiempo real del uso de ancho de banda, mostrando estadísticas sobre el tráfico de la red.

trafico_red: Registra los datos de tráfico de la red en un archivo o base de datos, lo que permite un análisis posterior del tráfico.

escaneo: Escanea la red local para detectar dispositivos conectados. Esto puede incluir ordenadores, teléfonos, routers, entre otros dispositivos.

analizar_rendimiento_red: Realiza un análisis del rendimiento de la red, proporcionando métricas como la velocidad de conexión, latencia y posibles cuellos de botella.

Notas
Requisitos del sistema: Este script debe ejecutarse en un entorno Linux o Unix que tenga soporte para Bash. Asegúrate de tener permisos de administrador (root) si algunas funciones requieren acceso elevado (por ejemplo, escanear dispositivos en la red).
Dependencias: Algunos de los scripts auxiliares (monitoreo.bash, trafico_red.sh, etc.) pueden requerir herramientas adicionales (como netstat, iftop, o nmap) instaladas en tu sistema.


Ejecutar un Script de PowerShell
Esta opción permite ejecutar un script de PowerShell que brinda información o realiza análisis de seguridad. Es útil en entornos Windows o en sistemas multiplataforma que cuentan con PowerShell Core.

Ejecutar un Script de Python
Proporciona un análisis de seguridad adicional o información relacionada con la seguridad mediante un script en Python, siendo esta una opción multiplataforma y compatible con la mayoría de sistemas operativos.

Cada uno de estos scripts tiene como objetivo ofrecer una visión integral sobre la seguridad del sistema desde diferentes ángulos y utilizando diversas herramientas que ofrece cada lenguaje.

Requisitos
Python 3.x: Asegúrate de tener Python instalado para ejecutar el script principal y la opción de Python.
Bash: Para ejecutar el script de Bash en sistemas basados en Unix/Linux.
PowerShell: PowerShell 5.1 o superior en Windows, o PowerShell Core en sistemas multiplataforma para la opción de PowerShell.

TRABAJO EN PROCESOOOO

# PROYECTO-FINAL

<span style="font-size: 20px;">Texto con tamaño 20px</span>


## Herramienta de Ciberseguridad Multiplataforma

### Descripción
Este proyecto es una herramienta de ciberseguridad desarrollada para ejecutar y coordinar scripts en tres lenguajes distintos (Python, PowerShell y Bash) desde un solo menú en Python. La herramienta proporciona información útil sobre la seguridad de un sistema, permitiendo al usuario realizar diferentes análisis y consultas en función del sistema operativo o del lenguaje de script.

### Funcionalidades
La herramienta permite seleccionar entre las siguientes opciones:

## Ejecutar un Script de Bash
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

### Explicación de las funciones
**monitoreo:** Esta función inicia el monitoreo en tiempo real del uso de ancho de banda, mostrando estadísticas sobre el tráfico de la red.

**trafico_red:** Registra los datos de tráfico de la red en un archivo o base de datos, lo que permite un análisis posterior del tráfico.

**escaneo:** Escanea la red local para detectar dispositivos conectados. Esto puede incluir ordenadores, teléfonos, routers, entre otros dispositivos.

**analizar_rendimiento_red:** Realiza un análisis del rendimiento de la red, proporcionando métricas como la velocidad de conexión, latencia y posibles cuellos de botella.

### Ejemplo de salida
Cuando seleccionas una opción, el script generará un archivo de reporte con la fecha y hora actuales en el siguiente formato:

      2024-11-05_14-30-25_Reporte_HashView.txt

Este archivo de reporte contendra los resultados de la tarea seleccionada 

### Notas
#### Requisitos del sistema: 
Este script debe ejecutarse en un entorno Linux o Unix que tenga soporte para Bash. Asegúrate de tener permisos de administrador (root) si algunas funciones requieren acceso elevado (por ejemplo, escanear dispositivos en la red).

### Dependencias: 
Algunos de los scripts auxiliares (monitoreo.bash, trafico_red.sh, etc.) pueden requerir herramientas adicionales (como netstat, iftop, o nmap) instaladas en tu sistema.


## Ejecutar un Script de PowerShell
Esta opción proporciona un menú interactivo para realizar diversas tareas de administración y monitoreo de sistemas. Está diseñado para ayudar a los administradores de sistemas y profesionales de seguridad a realizar acciones como la revisión de hashes de archivos, la detección de archivos ocultos, el monitoreo de recursos del sistema y la visualización de los procesos que consumen más recursos. A continuación, se describe cómo utilizarlo y qué hace cada opción del menú.

### Requisitos previos
Este script depende de varios módulos de PowerShell que debes tener instalados o disponibles en tu entorno. Asegúrate de tener los siguientes archivos en el mismo directorio que el script principal:

**Recursos.psm1:** Proporciona funciones relacionadas con el monitoreo de uso de recursos.
**TopProcess.psm1:** Contiene funciones para listar los procesos que están utilizando más recursos del sistema.
**BuscarArchivosOcultos.psm1:** Incluye funciones para buscar archivos ocultos en el sistema.
**API_VIRUSTOTAL_2.psm1:** Contiene funciones para la consulta de hashes de archivos a través de la API de VirusTotal.

### Menú interactivo

Una vez ejecutado, el script presenta un menú con las siguientes opciones:

#### 1: Revisión de hashes de archivos y consulta de API de VirusTotal

Permite revisar los hashes de archivos y consultar la API de VirusTotal para obtener información sobre ellos.
Si se proporciona un archivo de entrada, se utiliza para realizar la revisión de los hashes.

#### 2: Listado de archivos ocultos

Muestra una lista de archivos ocultos en el sistema.
Si se proporciona un archivo de entrada, se utiliza para buscar archivos ocultos en él.

#### 3: Listado de uso de recursos

Muestra información sobre el uso de recursos del sistema, como la memoria y el uso de la CPU.

#### 4: Ver proceso con más recursos

Muestra el proceso que está utilizando más recursos en el sistema.

### Explicación de las funciones
Revisión de hashes y consulta API de VirusTotal: Esta opción permite realizar la revisión de hashes de archivos y consultar la API de VirusTotal para obtener detalles sobre los archivos, como su estado de seguridad (por ejemplo, si están infectados o no).

**Listado de archivos ocultos:** Permite listar los archivos ocultos en el sistema. Esto puede ser útil para detectar archivos sospechosos que pueden estar ocultos deliberadamente.

**Listado de uso de recursos:** Muestra información sobre el uso de recursos del sistema, como la memoria y el uso de la CPU, lo que te permite monitorear el rendimiento del sistema.

**Ver proceso con más recursos:** Muestra el proceso que está utilizando más recursos en el sistema, lo que puede ayudarte a identificar procesos que están consumiendo una cantidad excesiva de memoria o CPU.

### Ejemplo de salida
Cuando seleccionas una opción, el script generará un archivo de reporte con la fecha y hora actuales en el siguiente formato:

      2024-11-05_14-30-25_Reporte_HashView.txt

Este archivo de reporte contendra los resultados de la tarea seleccionada 

### Notas
### Requisitos del sistema
Este script debe ejecutarse en una máquina que tenga PowerShell instalado. Es compatible con PowerShell 5.1 y versiones superiores, por lo que no deberías tener problemas para ejecutarlo en la mayoría de las instalaciones de Windows.

### Dependencias
Este script depende de los siguientes módulos de PowerShell:

**Recursos.psm1:** Para el monitoreo de recursos del sistema.
**TopProcess.psm1:** Para la visualización de los procesos con mayor uso de recursos.
**BuscarArchivosOcultos.psm1:** Para la detección de archivos ocultos.
**API_VIRUSTOTAL_2.psm1:** Para realizar consultas sobre archivos en VirusTotal.
Asegúrate de tener estos módulos disponibles y de importarlos correctamente.

## Ejecutar un Script de Python
Proporciona un análisis de seguridad adicional o información relacionada con la seguridad mediante un script en Python, siendo esta una opción multiplataforma y compatible con la mayoría de sistemas operativos.

Cada uno de estos scripts tiene como objetivo ofrecer una visión integral sobre la seguridad del sistema desde diferentes ángulos y utilizando diversas herramientas que ofrece cada lenguaje.

Requisitos
Python 3.x: Asegúrate de tener Python instalado para ejecutar el script principal y la opción de Python.
Bash: Para ejecutar el script de Bash en sistemas basados en Unix/Linux.
PowerShell: PowerShell 5.1 o superior en Windows, o PowerShell Core en sistemas multiplataforma para la opción de PowerShell.

TRABAJO EN PROCESOOOO

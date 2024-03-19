



# VoiceGPT
  
Envía un audio y recibe la data según el template creado en VoiceGPT.  
  
![banner](imgs/Banner_VoiceGPT.png o jpg)

## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Obtener template de audio
  
Obtiene de un audio los datos indicados en el template de VoiceGPT
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|API Key|Key generada en la sección Perfil de VoiceGPT.|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ey...|
|ID del Template|El ID del template a ocupar. Puede sacarse de la url https//voicegpt.rocketbot.com/#/template/{template}|83540b69bb195851896cd3881555c222|
|Seleccione el audio|URL de la ubicación y nombre del audio a enviar|C:/Users/user/Downloads/file.mp3|
|Asignar resultado a variable|Variable donde se almacenará el resultado.|Variable|

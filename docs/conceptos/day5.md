## Image
- Es la plantilla o imagen literal de lo que se quiere trabajar, no necesariamente postgres pero cualquier app, para poder levantarla desde ahi

## Container
- Es la instancia donde se ejecuta la imagen, cada vez que se ejecuta se crea un nuevo container, separados uno de otro

## Volumes
- El volumen es el almacenamiento por fuera del contender, lo que nos mayuda a tener una instacia fuera del container

## Networks
- La conexion entre contenedores desde diferentes computadoras como si estuvieran en la misma red local

## Dockerfile
- Es el archivo de texto con los pasos a seguir bien estructurados para crear nuestra propia imagen

## Docker Compose
- Cuando querramos usar muchos contenedores distintos para un proyecto y no tengamos que abrir un comando para cada uno, un compose se encarga de ello, corriendo todos los comandos desde un archivo YAML
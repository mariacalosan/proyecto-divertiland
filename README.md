# Divertiland
requerido tener python y pipenv para correr la aplicacion 
## Comandos
- `pipenv run start` comando para correr el servidor
- `pipenv run makemigrations` comando para correr las migraciones de el models
- `pipenv run migrate` comando para crear las migracion
- `pipenv run createadmin` crear un usuario administrador
## Crear nueva aplicación
1. Crear carpeta con el `nombreModulo` (en singular) en la carpeta `modulos`
2. Correr el comando `pipenv run python manage.py startapp nombreModulo ./modulos/nombreModulo`
3. Cuando la apliaccion este creada ir a el archivo de el settings y registrarla en el  installed.apps
4. en el archivo apps.py que se encuentra en la carpeta que se acabo de generar  agregarle el nombre de la aplicacion creada junto con la carpeta donde esta
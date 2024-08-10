onlyflans
- crear entorno virtual <virtualenv venv>
- Activo entorno virtual <source venv/Scripts/activate>
- Instalamos Django <pip install django>
- Creamos nuestro <.gitignore> y copiamos base existente
- validar lista de dependencias activas <pip list>
- Luego <pip freeze>
- Creamos nuestro txt de requerimientos <pip freeze > requirements.txt>
- Luego podremos iniciar o crear nuestro proyecto <django-admin startproject onlyflans .>
- <py manage.py> para ver nuestro repertorio
- Hacemos las marcas de nustras migraciones:
    <py manage.py makemigrations>
    <py manage.py migrate>
- Luego creamos nuestro usuario/password del admin <py manage.py createsuperuser>
- Creamos luego nuestra app llamada web <py manage.py startapp web>
- Agregamos la app "web" a setting.py 
- Creamos estructura y creamos en nuestra aplicación "web" las carpetas: templates y static
- En carpeta "static" se deja seteada la carpeta con las carpetas css, js e img
- En carpeta "templates" creamos carpeta index.html
- Tambien en nuestra app "web" creamos "urls.py"
- Al lado de .gitignore creamos ".env"
- Validamos que proyecto corra con <py manage.py runserver>
- desactivamos el entorno virtual <deactivate>
- subimos nuestro proyecto a GitHub
- 
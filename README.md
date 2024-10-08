onlyflans

--HITO 1--

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
    git init
    creamos en GitHub nuestro repositorio
    git status
    git add .
    git commit -m "comentario"
    git push origin master
    **git remote -v (para ver las rutas creadas)** 

-- HITO 2-- 

Creación de un sitio web responsive con Bootstrap: en este Hito se crearán las primeras estructuras que permitirán mostrar datos en nuestro sitio web.
Implementar

    BOOTSTRAP: Crear sitio web responsive con Bootstrap
    STATIC: Implementa un proyecto Django para servir contenido estático dando solución a los requerimientos. Implementar load static a todo el documento y marcar sintaxis de static cual: {% static 'path' %}
    TEMPLATES: Utiliza templates para la renderización de contenido dinámico en un proyecto Django para dar solución a un requerimiento.
        VARIABLES
        CONDICIONALES
        HERENCIA: Utiliza herencia de plantillas en un proyecto Django para dar solución a un requerimiento. Django permite la reutilización de una plantilla dentro de otra.
        LOOP (bucle FOR)
    LOGIN-isActivate: Utiliza instrucciones de control en plantillas de un proyecto Django para dar solución a un requerimiento.
        Filtro if + | filter UPERCASE

PASOS

    Crear una plantilla o template base que tendrá los elementos comunes de la interfaz de nuestro sitio web OnlyFlans.

    about
    index
    base
    navbar
    header
    footer
    welcome

    Habilitar las rutas o url: /, /acerca y /bienvenido, creando las vistas y plantillas necesarias que extiendan la plantilla base para mostrar diferentes contenidos para cada vista.

    Como elementos transversales mínimos que deberán mostrarse en todas las rutas se encuentran: - header, que contenga un logo para nuestra web - navbar, que permita la navegación entre las distintas rutas de nuestra web - footer, que entregue la información de “desarrollado por” incluyendo tu nombre y la frase “para Desafío Latam”, ejemplo: “desarrollado por Juan Perez para Desafío Latam”

    Adicionalmente cada ruta deberá mostrar lo siguiente:
        ruta /: deberá mostrar una lista de productos disponibles para la venta en la tienda de la PYME.
        ruta /acerca: deberá mostrar una descripción de la utilidad del sitio web, junto con la descripción de la PYME y datos como la fecha de creación, entre otros que se dispongan.
        ruta /bienvenido: deberá mostrar un mensaje de “bienvenido cliente” genérico en caso de no contar con los datos de un usuario y un mensaje de “bienvenido Juan Perez”(nombre variable) en el caso de contar con los datos del mismo.

Para la mejor visualización del sitio web que estamos creando se debe utilizar tanto la “grilla” de bootstrap como sus componentes, permitiendo al sitio web “acomodarse” a distintos tamaños de pantalla y resoluciones, además de permitir su rápido desarrollo. Puedes valerte de componentes de bootstrap como navbar, tarjetas o cards, entre otros según desees.

-- HITO 3 --

- Para el Hito 3, crearemos en carpeta <models.py> la clase <class Flan>
    ```py
    class Flan(models.Model):
        flan_uuid = models.UUIDField()
        name = models.CharField(max_length=64)
        description = models.TextField()
        image_url = models.URLField()
        slug = models.SlugField()
        is_private = models.BooleanField()

- Luego, importamos la clase Flan en carpeta <admin.py>
    <from.models import Flan>
- Luego registramos el módelo: 
    <admin.site.register(Flan)>

- Luego de ello, creamos una marcamos y creamos una Migración:
<py manage.py makemigrations>
-> Creará archivo <000X_initial.py> en carpeta migrations
<py manage.py migrate>
-> nos creara una tabla llamada <web_flan> en db.sqlite3

- Una vez creada la tabla en sqlite, corremos el proyecto <py manage.py runserver> y accedemos a http://127.0.0.1:8000/admin
- Dentro de http://127.0.0.1:8000/admin podemos ver la tabla y agregar los flanes llenando los datos que tenemos disponibles en nuestro JSON dentro de carpeta <utils> la cual debe ser creada previamente.
- Para obtener nuetro UUID podemos ingresar a la herramienta https://www.uuidgenerator.net/version4
- En <views.py> ahora obtendremos data desde el model con los datos que entrega nuestro JSON, debiendo quedar:
    ```py
    def home(req):
        flanes_all = Flans.objects.all() 
        flanes_publicos = Flans.objects.filter(is_private=False) 
        return render(req, 'index.html', {"flanes_publicos": flanes_publicos})
-  

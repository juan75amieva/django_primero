Crear carpeta del directorio
inicializar git
crear el entorno virtual con virtual env
instalo virtualenv   pip install virtualenv
creo el proyecto     virtualenv carpetaProyecto
inicializ            .\carpetaEntorno\Scripts\activate


desde VC abrir la carpeta
presionar f1
escribir selecionar interprete
elejir la opcion de virtual env ( el nombre de la carpeta)



********************************************************
Instalar django

pip install django


comprobar la instalacion 
django-admin --version


comprobar desde la shell de python la version de django
django.get_version()

*********************************************************
Crear proyecto nuevo
 django-admin startproject miSitio .
*********************************************************
ejecutar python manage.py , una vez que lo ejecute puere recibir parametros entonces le envio runserver

python manage.py runserver
**********************************************************
se puede ver que tambien creo una base de datos
**********************************************************
de la siguiente manera podemos elegir el puerto 

python manage.py runserver 3000

**********************************************************

Crear una app
python manage.py startapp miplicacion 
**********************************************************

Primer hola mundo

en la carpeta miplicacion (me equivoque al tipear)
en el archivo views.py

importar HttpResponse

from django.http import HttpResponse

luego crear una funcion

def hello(request):
	return HttpResponse("Hola Mundo")


ahora en el archivo urls.py de la carpeta miSitio

importar la funcion recien creada

from miaplicacion.views import hola


establecer la nueva ruta

path('', hola )


*********************************
Include

si la aplicacion se vuelve mas grande no es recomendable tener todas las urls en el directorio principal
sino que cada app tenga su urls para eso se procede de la siguiente manera

crear un archivo dentro de miplicacion 

urls.py

dentro de ese  archivo 

				from django.urls import path
				from . import views

exportamos una lista nueva que se va a llamar 

				urlpatterns = [
					path('', views.hola),
					path('about/', views.about)
				]

en el archivo urls de miSitio eliminamos el from import miaplicacion.views
y en las urls colocamos la siguiente

 path('', include('miaplicacion.urls'))

 el string vacio significa que ants de las urls no va nada

 ************************************************************

 DATABASE

 instalar db browser sql3


 python manage.py makemigration

 python manage.py migrate

 en el archivo models.py de miaplicacion crear una clase

 class Project(models.Model):
    name = models.CharField(max_length=200)

en el archivo setting de miSitio agregar a la lista INSTALLED_APPS

el nombre de la aplicacion en este caso miplicacion (si lo escribi mal)


ejecutar python manage.py makemigrations miplicacion

python manage.py migrate miplicacion


**************************************************

Como interactuar con las tablas que creamos

Abriendo la consola
python manage.py shell



**********************************

>>> from miplicacion.models import Project, Task
>>> p  =   Project(name="aplicacion movil")     
>>> p
<Project: Project object (None)>
>>> p.save
<bound method Model.save of <Project: Project object (None)>>
>>> p.save()
>>> 

Mostrar los elementos
>>> Project.objects.all()


*************************

Render

Utilizar Template o Plantillas

En  la carpeta de la aplicacion crear una carpeta que se llame Template
dentro de la carpeta creamos una archivo index.html
crear un archivo html

para que responda con este archivo en lugar de con el texto hay que hacer algunos cambios

importar render en views

from django.shortcuts import render

se cambia la funcion de la siguiente manera

def index(request):
    return HttpResponse("index")


por esta otra

def index(request):
    return render (request,'index.html')






python manage.py shell


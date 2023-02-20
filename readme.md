
## API Reference
Steps to replicate project:

1. Make sure you have python 3^7 and venv(virtualenv) installed and in your PATH

2. Then create a new directory and virutual env using the following commands:

### Windows
```bash
> cd onedrive\desktop\code
> mkdir library
> cd library
> python -m venv .venv
> .venv\Scripts\Activate.ps1
> (.venv) > python -m pip install django~=4.0.0
```
### macOS/linux
```bash
> % cd desktop/desktop/code
> % mkdir library
> % cd library 
> % python3 -m venv .venv
> % source .venv/bin/activate
> (.venv) % python3 -m pip install django~=4.0.0
```
## 3. Clone this repository

Now you should have the following structure:

├── doorvelapi
│   ├── __init__.py
|   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
|   ├──apis
|   ├── Codigos.xml
|   ├──requirements.txt
|   ├──runtime.txt
|   ├──scripts
|   ├──static
|   ├──staticfiles
|   ├──zipcodes
|   ├──.ebextensions
|   ├──.elasticbeanstalk
└── .venv/

## 4. Install the requirements with the following commands

### Windows
```bash
(.venv) > python -m pip install -requirements.txt
```

### macOS/linux
```bash
(.venv) % python3 -m pip install -r requirements.txt
```

## 5. Change the db connections settings:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<database_name>',
        'USER': '<database_user>',
        'PASSWORD': '<database_password>',
        'HOST': '<database_endpoint>',
        'PORT': '3306',
    }
}
```
## 6. Run migrations

### Windows
```bash
> (.venv) > python manage.py migrate
> (.venv) > python manage.py runserver
```
### macOS/linux
```bash
> (.venv) > python3 manage.py migrate
> (.venv) > python3 manage.py runserver
```

--Note : if getting the "no such table exists error", comment out the url paths in the 
doorvelapi/urls.py file before running the Scripts

## 7. Start the application
### Windows
```bash
> (.venv) > python manage.py runserver
```

### macOS/linux
```bash
> (.venv) > python3 manage.py runserver
```
## 8. Go to the base path

http://127.0.0.1:8000/

if its the first time and the db tables are empty, it will run a script to bulk insert all of the zipcodes in the zipcode table.

Otherwise, it should give you a welcome text.

## 9. Create super user:
We can start entering extra data into the zipcodes model if needed via the built-in Django app. To use it we need to create a superuser account.

Start with the superuser account. On the command line run the following command:

# Windows
(.venv) > python manage.py createsuperuser

# macOS/linux
(.venv) > python3 manage.py createsuperuser


#### Get zipcode by zipcode number

```http
  GET /api/zipcodes/{zipcode}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `zipcode_number` | `number` | **Required**. |

Returns the zipcode information in the following structure:
```
{
    "Data": {
        "locality": "Monterrey",
        "zip_code": 64130,
        "settlement": [
            {
                "key": 66,
                "name": "Villa Alegre",
                "zone_type": "Urbano",
                "settlement_type": {
                    "name": "Colonia"
                }
            },
            {
                "key": 4459,
                "name": "Lomas de Villa Alegre",
                "zone_type": "Urbano",
                "settlement_type": {
                    "name": "Colonia"
                }
            }
        ],
        "federal_entity": {
            "key": 19,
            "name": "Nuevo León",
            "code": 0
        },
        "municipality": {
            "key": 39,
            "name": "Monterrey"
        }
    }
}
```

La manera en la que aborde el problema fue viendo primero videos y articulos de django en tiempos libres, ya 
que nunca lo habia utilizado, solo habia escuchado del framework.
Lo segundo que hice fue darle una lectura breve a la documentacion en la pagina web oficial
Lo tercero fue leer un libro llamado Django for Apis, Build web apis with python.

Leyendo ese libro entendi mas del framework y empece a construir una aplicacion simple de libros, para
familiarizarme, despues cambie la estructura del proyecto para crear el modelo de zipcode y los endpoints.
Estuve probando con el xml, el excel y el txt que tenia los codigos postales y decidi utilzar el xml, para hacer
una carga inicial con los datos del archivo hacia la tabla, asi que defini el modelo, y los campos que iba a utilizar
del xml, asi como los tipos de datos y las excepciones al leer el archivo.
Estuve buscando una manera de correr un script desde el shell para iniciar la carga de datos pero ya que no tengo
mucha familiarizacion con el framework no encontre una manera eficiente de hacerlo al inicio.
(Estuve buscando en foros pero ninguna opcion me llego a funcionar, al hacer deploy me di cuenta que existe una 
clase llamada Basecommand con la que se puede implementar eso desde el .config de elastic beanstalk)

Al lograr la carga inicial de los datos a la tabla, hice el enpoint y estuve probando con serializers para la
respuesta, pero me di cuenta que tal vez no era la mejor opcion debido a la estructura requerida de la respuesta del api
entonces opte por usar APIView y contruir la respuesta en formato JSON.
Tal vez si hubiera definido de manera diferente el modelo, o modelos, hubiera podido utilizar un serializer para 
mejor eficiencia.

Despues busque la manera de reemplazar sqlite3 por MySQL, opte por utilizar Amazon RDS con una instancia gratis
de MySQL, asi que levante una instancia y agregue los permisos necesarios en la IAM, y en los inbound rules para
poder conectarme desde mi Ip.

Despues instale EB Cli (Elastic beanstalk Cli), Asigne las IAM necesarias y levante una instancia con Python 3.7
desde la consola, en la region correcta donde se encuentra la BD MySQL, Asigne un repositorio de CodeCommit y el branch
indicado. Al crear el proyecto tamnien fue necesario crear y modifcar los archivos .ebextensions y .elasticbeanstalk para
el deploy correcto. De nuevo tuve problemas con permisos en Code Commit, git, y Elastic beanstalk.
Lo solucione cambiando policies en IAM y configuracion de git.

No levantaba correctamente asi que me conecte por ssh a la instancia de Eb para iniciar el virtualenv manualmente.
Esto se podria solucionar con un script en el archivo config de .ebextensions. Tambien se pueden utilizar 
variables de entorno de eb que agregare en un futuro.
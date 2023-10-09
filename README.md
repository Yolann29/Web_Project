First commit # T-WEB-501-TLS_9

Pour la base de données: utilisation de postgreSQL
Pour le back-end API: utilisation de Jango

Documentation sur Django :
https://docs.djangoproject.com/en/4.2/

Installation de Django:
sudo apt install python3-pip
python3 -m pip install Django


version de python utilisée: Python 3.10.12
version de Django utilisée: 4.2.6


On établit notre dosssier pour mettrre tous nos fichiers liés avec Django pour l'API :
django-admin startproject Back

Création de la première app :
python manage.py startapp polls

Installer psycopg pour que Django puisse intéragir avec notre base de données en postgreSQL : 
https://www.psycopg.org/install/

sudo apt install python3-dev libpq-dev
pip install psycopg2

Dans Back/Back/settings.py :
Changer le database avec le bon 'username' et 'password'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jobboardbdd',
        "USER": "'username'",
        "PASSWORD": "'password'",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
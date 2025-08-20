
import os
from pathlib import Path
import dj_database_url
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY","dev-secret")
DEBUG = os.getenv("DJANGO_DEBUG","1")=="1"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS","*").split(",")
INSTALLED_APPS=["django.contrib.admin","django.contrib.auth","django.contrib.contenttypes","django.contrib.sessions","django.contrib.messages","django.contrib.staticfiles","ops"]
MIDDLEWARE=["django.middleware.security.SecurityMiddleware","whitenoise.middleware.WhiteNoiseMiddleware","django.contrib.sessions.middleware.SessionMiddleware","django.middleware.common.CommonMiddleware","django.middleware.csrf.CsrfViewMiddleware","django.contrib.auth.middleware.AuthenticationMiddleware","django.contrib.messages.middleware.MessageMiddleware","django.middleware.clickjacking.XFrameOptionsMiddleware"]
ROOT_URLCONF="serafina.urls"
TEMPLATES=[{"BACKEND":"django.template.backends.django.DjangoTemplates","DIRS":[],"APP_DIRS":True,"OPTIONS":{"context_processors":["django.template.context_processors.debug","django.template.context_processors.request","django.contrib.auth.context_processors.auth","django.contrib.messages.context_processors.messages"]}}]
WSGI_APPLICATION="serafina.wsgi.application"
DATABASE_URL=os.getenv("DATABASE_URL")
DATABASES={"default":dj_database_url.parse(DATABASE_URL,conn_max_age=600)} if DATABASE_URL else {"default":{"ENGINE":"django.db.backends.sqlite3","NAME":BASE_DIR/"db.sqlite3"}}
LANGUAGE_CODE="en-us"; TIME_ZONE="Asia/Karachi"; USE_I18N=True; USE_TZ=True
STATIC_URL="static/"; STATIC_ROOT=BASE_DIR/"staticfiles"; DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"

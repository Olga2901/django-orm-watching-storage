import os
from environs import Env
import dj_database_url


env = Env()
env.read_env()


DATABASES = {'default': dj_database_url.config(conn_max_age=600)}
INSTALLED_APPS = ["datacenter"]
DEBUG = env.bool("DEBUG", default=False)
SECRET_KEY = env("SECRET_KEY")
ROOT_URLCONF = 'project.urls'
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]
USE_L10N = env.bool("USE_L10N", True)
LANGUAGE_CODE = env("LANGUAGE_CODE")
TIME_ZONE = env("TIME_ZONE")
USE_TZ = env.bool("USE_TZ", True)
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

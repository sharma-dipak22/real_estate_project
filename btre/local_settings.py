# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-y%#$9z%jobjspuk&o^hv6v^ynvz=@=t7eh+^9@jrn$!g2b3h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1','rel-estate-app.herokuapp.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd469mca50gth0r',
        'USER': 'auuzbvtqbjvtqy',
        'PASSWORD': '7d6dc97bcce55999ccc93dfb5198ad73d288cc1d53975fa3f7d5904927085ee9',
        'HOST': 'ec2-54-159-176-167.compute-1.amazonaws.com',
        'PORT' : '5432'
    }
}

# Email config
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'dipaksharma22897@gmail.com'
EMAIL_HOST_PASSWORD = 'Dbs@22897'
EMAIL_USE_TLS = True
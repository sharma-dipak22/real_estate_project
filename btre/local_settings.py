# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-y%#$9z%jobjspuk&o^hv6v^ynvz=@=t7eh+^9@jrn$!g2b3h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['rel-estate-app.herokuapp.com']
# ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db69mktqcu64ui',
        'USER': 'tadafiejcmsauy',
        'PASSWORD': '8847a78d0f1b3ffe7ca0dd61328f2ad982516e379c294028bb7fe01036a9edaa',
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
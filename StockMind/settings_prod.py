# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stock_mind',
        'USER': 'simplenet2016',
        'PASSWORD': 'password@123',
        'HOST': 'simplenet2016.mysql.pythonanywhere-services.com',
        'PORT': '3306',
        'ATOMIC_REQUESTS': True,
    }
}

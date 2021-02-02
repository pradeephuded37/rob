import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abs.path(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

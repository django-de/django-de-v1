from django_de.conf.settings import *

SECRET_KEY = 'zn21qir!46chgugeyn!0d&7&kl184b_l$pke_ozi!hwi7tju8)'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Martin Mahner', 'martin@mahner.org'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_ROOT, 'dev.db'),
    }

#   'default': {
#       'ENGINE': 'django.db.backends.mysql',
#       'NAME': 'dbname',
#       'USER': 'root',
#       'PASSWORD': '',
#   }
}
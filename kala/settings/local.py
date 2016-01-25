try:
    from common import *
except ImportError as e:
    pass

INSTALLED_APPS = INSTALLED_APPS + (
    'django_extensions',
)

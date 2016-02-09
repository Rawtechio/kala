from configurations import Configuration
from .common import Common


class Local(Common):
    # Only enable locally
    DEBUG = True
    TEMPLATE_DEBUG = True

    # Well this is super secure
    SECRET_KEY = "CHANGEME!!CHANGEME!!CHANGEME!!CHANGEME!!CHANGEME!!"

    # Allow all host headers
    ALLOWED_HOSTS = ['*']

    INSTALLED_APPS = Common.INSTALLED_APPS + (
        'django_extensions',
    )

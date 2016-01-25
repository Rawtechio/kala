from configurations import Configuration
import os
from .common import Common


class Production(Common):
    # Well this is super secure
    SECRET_KEY = os.environ['SECRET_KEY']

    DEBUG = True

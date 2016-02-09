# -*- coding: utf-8 -*-
# Created on 29 Jan 2016 at 16:11
from __future__ import unicode_literals, absolute_import

# Django
from django.db import models

# 3rd Party
from authtools.models import AbstractNamedUser
from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractNamedUser):
    """
    Custom user model
    """

    slug = AutoSlugField(populate_from='name')
    job_title = models.CharField(max_length=75)
    phone_number = PhoneNumberField(blank=True)
    fax_number = PhoneNumberField(blank=True)

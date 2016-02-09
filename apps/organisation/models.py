# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

# Native
import uuid

# Django
from django.db import models
from django.conf import settings

# 3rd Party
from autoslug import AutoSlugField
from sorl.thumbnail import ImageField

# Custom
from apps.utils.models import TimeStampedUUIDModel
from apps.utils.images import logo_upload_path


class Organisation(TimeStampedUUIDModel):
    """
    Tries to follow schema.org/LocalBusiness where it makes sense for
    our purposes.
    """

    # Basic information
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name")
    description = models.TextField()
    logo = ImageField(upload_to=logo_upload_path)

    # contactPoints
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="organisation_owned_by"
    )
    maintained_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="organisation_maintained_by"
    )

    dissolution_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return u"{name} ({uuid})".format(
            name=self.name,
            uuid=self.uuid
        )

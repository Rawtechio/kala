# -*- coding: utf-8 -*-
# Created on 30 Jan 2016 at 16:01

# Django
from django.db import models
from django.conf import settings

# 3rd Party
from model_utils.models import TimeStampedModel
from hashids import Hashids


class TimeStampedUUIDModel(TimeStampedModel):
    """
    TimeStampedModel provides self-updating created and modified fields
    on any model that inherits from it.
    https://django-model-utils.readthedocs.org/en/latest/models.html#timestampedmodel

    As well as a "Youtube style" URL safe hash of the ID. The hash is for public
    display only. It should be decoded back to the pk integer before any DB lookups
    take place.
    """

    # Use an UUID instead of integer for primary key
    uuid = models.CharField(
        editable=False,
        max_length=50,
        blank=True
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super(TimeStampedUUIDModel, self).save(*args, **kwargs)

        if self.pk and not self.uuid:
            hashids = Hashids(salt=settings.SECRET_KEY, min_length=5)
            hashid = hashids.encode(self.pk)
            self.uuid = hashid
            self.save()

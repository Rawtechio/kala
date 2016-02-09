# -*- coding: utf-8 -*-
# Created on 5 Feb 2016 at 16:29
from __future__ import unicode_literals, absolute_import


# Django
from django.db import models
from django.conf import settings

# 3rd Party
from autoslug import AutoSlugField


# Custom
from apps.utils.models import TimeStampedUUIDModel


class Review(TimeStampedUUIDModel):
    """
    Store reviews for pretty much anything.
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    body = models.TextField()

    def __unicode__(self):
        return u"{title}".format(
            title=self.title
        )

    def save(self, *args, **kwargs):
        super(Review, self).save(args, kwargs)

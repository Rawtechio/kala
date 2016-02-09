# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

# Django
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings

# 3rd Party
from autoslug import AutoSlugField
from sorl.thumbnail import ImageField
from phonenumber_field.modelfields import PhoneNumberField
from star_ratings.models import Rating

# Custom
from apps.organisation.models import Organisation
from apps.address.models import Address
from apps.utils.models import TimeStampedUUIDModel
from apps.utils.images import logo_upload_path


class Place(TimeStampedUUIDModel):
    """
    Tries to follow schema.org/LocalBusiness where it makes sense for
    our purposes.
    """

    # Basic information
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name")
    description = models.TextField()
    logo = ImageField(upload_to=logo_upload_path)

    # ***** - Would rate again A+++++
    ratings = GenericRelation(Rating, related_query_name='thing_ratings')

    # contactPoints
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="place_owner"
    )

    # Contact details
    address = models.ForeignKey(Address, null=True, blank=True)
    email = models.EmailField(blank=True)
    phone_number = PhoneNumberField(blank=True)
    fax_number = PhoneNumberField(blank=True)

    # Geo
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    # Extras
    parent_organisation = models.ForeignKey(Organisation, null=True, blank=True)
    duns = models.CharField(max_length=9, blank=True)

    # Has this location closed / is active?
    dissolution_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)
    published = models.BooleanField(default=False)

    @property
    def branch_code(self):
        return self.id

    def __unicode__(self):
        return u"{name} ({uuid})".format(
            name=self.name,
            uuid=self.uuid
        )

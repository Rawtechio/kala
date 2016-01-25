# -*- coding: utf-8 -*-

# Django
from django.db import models

# 3rd Party
from model_utils.models import TimeStampedModel


class Address(TimeStampedModel):
    """
    Not every address will look like this. This only deals with UK
    addresses, or countries that have the same address format as the UK.

    https://www.mjt.me.uk/posts/falsehoods-programmers-believe-about-addresses/
    """

    street_address = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    county = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    postal_code = models.CharField(max_length=60)

    def one_line(self):
        # Why no county or country? See
        # http://www.royalmail.com/personal/help-and-support/How-do-I-address-my-mail-correctly
        return u"{}, {}, {}".format(
            self.street_address,
            self.city,
            self.postal_code
        )

    def __unicode__(self):
        return self.one_line()

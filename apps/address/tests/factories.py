# -*- coding: utf-8 -*-
# Created on 9 Feb 2016 at 09:34
from __future__ import unicode_literals, absolute_import

# 3rd Party
import factory
from faker import Factory as FakerFactory

# Custom
from apps.utils.testing.faker import UKAddressProvider
from ..models import Address

faker = FakerFactory.create()
faker.add_provider(UKAddressProvider)


class AddressFactory(factory.django.DjangoModelFactory):
    """
    Creates a valid faked address
    """

    street_address = factory.LazyAttribute(lambda x: faker.street_address())
    city = factory.LazyAttribute(lambda x: faker.city())
    county = factory.LazyAttribute(lambda x: faker.county())
    country = factory.LazyAttribute(lambda x: faker.country())
    postal_code = factory.LazyAttribute(lambda x: faker.postcode())

    class Meta:
        model = Address

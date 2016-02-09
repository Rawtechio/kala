# -*- coding: utf-8 -*-
# Created on 9 Feb 2016 at 09:34
from __future__ import unicode_literals, absolute_import

# Native
import random
from datetime import date, timedelta

# 3rd Party
import factory
import factory.fuzzy
from faker import Factory as FakerFactory

# Custom
from apps.utils.testing.fuzzy import in_percentage
from apps.users.tests.factories import UserFactory
from apps.address.tests.factories import AddressFactory
from apps.organisation.tests.factories import OrganisationFactory
from ..models import Place

faker = FakerFactory.create()


class PlaceFactory(factory.django.DjangoModelFactory):
    """
    Creates a valid Place as well as all the ForeignKeys
    Optional fields are fuzzy
    """

    class Meta:
        model = Place

    name = factory.LazyAttribute(lambda x: faker.company())
    description = factory.LazyAttribute(lambda x: faker.catch_phrase())
    logo = factory.django.ImageField(color='green')
    owner = factory.SubFactory(UserFactory)
    address = factory.SubFactory(AddressFactory)
    email = factory.LazyAttribute(lambda x: faker.email())
    phone_number = factory.LazyAttribute(lambda x: faker.phone_number())
    fax_number = factory.LazyAttribute(lambda x: faker.phone_number() if in_percentage(20) else "")
    latitude = factory.LazyAttribute(lambda x: faker.latitude())
    longitude = factory.LazyAttribute(lambda x: faker.longitude())
    active = factory.LazyAttribute(lambda x: faker.boolean(chance_of_getting_true=80))
    published = factory.LazyAttribute(lambda x: faker.boolean(chance_of_getting_true=60))

    @factory.post_generation
    def populate_complex_fields(self, create, extracted, **kwargs):

        # If not active has a high chance of adding a dissolution date
        if not self.active and in_percentage(90):  # 90% of the time
            self.dissolution_date = factory.fuzzy.FuzzyDate(
                date.today() - timedelta(weeks=312)  # 6 years in weeks
            ).fuzz()

        # 10% chance of having a DUNS number (mostly used in the USA)
        if in_percentage(10):
            self.duns = factory.fuzzy.FuzzyInteger(123456789, 999999999).fuzz()

        if create:
            # 80% chance of being assigned to a Parent Org
            if in_percentage(80):
                self.parent_organisation = OrganisationFactory()

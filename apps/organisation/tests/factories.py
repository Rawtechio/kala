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
from apps.utils.testing.fuzzy import coinflip, in_percentage
from apps.users.tests.factories import UserFactory
from ..models import Organisation

faker = FakerFactory.create()


class OrganisationFactory(factory.django.DjangoModelFactory):
    """
    Creates a valid organisation as well as the neccessary
    foreign key objects
    """

    class Meta:
        model = Organisation

    name = factory.LazyAttribute(lambda x: faker.company())
    description = factory.LazyAttribute(lambda x: faker.catch_phrase())
    logo = factory.django.ImageField(color='blue')
    owner = factory.SubFactory(UserFactory)
    active = factory.LazyAttribute(lambda x: faker.boolean(chance_of_getting_true=80))
    published = factory.LazyAttribute(lambda x: faker.boolean(chance_of_getting_true=60))

    @factory.post_generation
    def populate_complex_fields(self, create, extracted, **kwargs):

        if create:
            # If not active has a high chance of adding a dissolution date
            if not self.active and in_percentage(90):  # 90% of the time
                self.dissolution_date = factory.fuzzy.FuzzyDate(
                    date.today() - timedelta(weeks=312)  # 6 years in weeks
                ).fuzz()

            # Add maintainers
            #  - 50/50 chance of only being owner
            #  - If owner not sole maintainer 80% chance of owner being included
            if coinflip():
                self.maintained_by.add(self.owner)
            else:
                if in_percentage(80):
                    self.maintained_by.add(self.owner)

                for z in range(1, random.randint(2, 6)):
                    maintainer = UserFactory()
                    self.maintained_by.add(maintainer)

# -*- coding: utf-8 -*-
# Created on 9 Feb 2016 at 09:34
from __future__ import unicode_literals, absolute_import

# 3rd Party
import factory
from faker import Factory as FakerFactory

# Custom
from apps.utils.testing.fuzzy import in_percentage
from ..models import User

faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.LazyAttribute(lambda x: faker.name())
    email = factory.LazyAttribute(lambda x: faker.email())
    password = factory.LazyAttribute(lambda x: faker.password())
    job_title = factory.LazyAttribute(lambda x: faker.job())
    phone_number = factory.LazyAttribute(lambda x: faker.phone_number())
    fax_number = factory.LazyAttribute(lambda x: faker.phone_number() if in_percentage(20) else "")

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call."""
        manager = cls._get_manager(model_class)
        # The default would use ``manager.create(*args, **kwargs)``
        return manager.create_user(*args, **kwargs)

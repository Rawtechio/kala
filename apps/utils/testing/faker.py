    # -*- coding: utf-8 -*-
# Created on 9 Feb 2016 at 09:55
from __future__ import unicode_literals, absolute_import

# 3rd Party
from faker.providers.address.en_GB import Provider as FakerAddressProvider


class UKAddressProvider(FakerAddressProvider):

    countries = ('England', 'Northern Ireland', 'Scotland', 'Wales')

    county_prefixes = ('City of', 'North', 'South', 'East', 'West', 'Isle of', 'Greater')
    county_roots = ('Bed', 'Cam', 'Che', 'Dur', 'Suff', 'Sus', 'Ess', 'Ham', 'Here', 'Hert',
                    'Glouce', 'Ham', 'Hamp', 'Hum', 'Humb', 'Humber', 'Hunt', 'Pete', 'Peter',
                    'El', 'Kent', 'Lan', 'Lin', 'Lon', 'Mersey', 'Middle', 'Nor', 'North',
                    'South', 'West', 'East', 'Nott', 'Notting', 'Ox', 'Rut', 'Shrop', 'Som',
                    'Somer', 'Staff', 'Surr', 'Tyne', 'War', 'Wick', 'Warwick', 'Wilt', 'Ant',
                    'Arm', 'Fer', 'Ferm', 'Ferman', 'London', 'Ty', 'Tyr', 'Abe', 'Aber',
                    'Ang', 'Arg', 'Ayr', 'Banff', 'Ber', 'Berw', 'Bu', 'Caith', 'Clark',
                    'Crom', 'Dum', 'Dumf', 'Dunb', 'Dunbar', 'Ed', 'Edin', 'Fi', 'Inv',
                    'Inver', 'Kin', 'Kincar', 'Kinross', 'Kirk', 'Lan', 'Lanar', 'Mor',
                    'Nairn', 'Ork', 'Peeble', 'Gla', 'Glas', 'Per', 'Pert', 'Perth', 'Ren',
                    'Ross', 'Rox', 'Selk', 'Shet', 'Stir', 'Suth', 'Lot', 'Wig', 'Breck',
                    'Bre', 'Caer', 'Card', 'Carma', 'Clw', 'Den', 'Dyf', 'Flint', 'Glam',
                    'Gwe', 'Gwyn', 'Merion', 'Mon', 'Monmouth', 'Mont', 'Pem', 'Pow', 'Rad',
                    'Wrex', 'Av', 'An')
    county_suffixes = ('on', 'ford', 'shire', 'tol', 'stol', 'ly', 'land', 'wall', 'ria', 'bria',
                       'by', 'set', 'ham', 'sex', 'ster', 'side', 'nt', 'hol', 'olk',
                       'folk', 'borough', 'wear', 'ing', 'rim', 'trim', 'own', 'nagh',
                       'derry', 'erry', 'one', 'rone', 'een', 'deen', 'us', 'gus',
                       'ute', 'ness', 'mannan', 'mann', 'an', 'arty', 'ife', 'ray',
                       'ney', 'ian', 'sey', 'wyd', 'yd', 'fed', 'organ', 'org', 'ent', 'edd',
                       'nedd')

    county_formats = (
        '{{county_prefix}} {{county_root}}{{county_suffix}}{{county_suffix}}',
        '{{county_prefix}} {{county_root}}{{county_suffix}}',
        '{{county_root}}{{county_suffix}}{{county_suffix}}',
        '{{county_root}}{{county_suffix}}',
    )

    @classmethod
    def county_prefix(cls):
        """
        :example 'North'
        """
        return cls.random_element(cls.county_prefixes)

    @classmethod
    def county_root(cls):
        """
        :example 'Somer'
        """
        return cls.random_element(cls.county_roots)

    @classmethod
    def county_suffix(cls):
        """
        :example 'ford'
        """
        return cls.random_element(cls.county_suffixes)

    def county(self):
        """
        :example 'City of Selkshire'
        """
        pattern = self.random_element(self.county_formats)
        return self.generator.parse(pattern)

# -*- coding: UTF-8 -*-
# Copyright 2022 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

from lino.api import dd, _

from django_measurement.models import MeasurementField
from measurement.measures import Distance, Area, Volume, Mass, Time

from .choicelists import *
from .choicelists import __all__ as CHOICELISTS

__all__ = ['Weighted', 'Volumed', 'Distanced', 'Zoned', 'Timed'] + CHOICELISTS

MIXINS = {
    'Weighted': {
        'measurement': Mass,
        'verbose_name': _('Weight'),
        'verbose_name_plural': _('Weights'),
        'unit_choices': WeightUnits,
        'default_unit': Mass.STANDARD_UNIT
    },
    'Volumed': {
        'measurement': Volume,
        'verbose_name': _('Volume'),
        'verbose_name_plural': _('Volumes'),
        'unit_choices': VolumeUnits,
        'default_unit': Volume.STANDARD_UNIT
    },
    'Timed': {
        'measurement': Time,
        'verbose_name': _('Time'),
        'verbose_name_plural': _('Times'),
        'unit_choices': TimeUnits,
        'default_unit': Time.STANDARD_UNIT
    },
    'Distanced': {
        'measurement': Distance,
        'verbose_name': _('Distance'),
        'verbose_name_plural': _('Distances'),
        'unit_choices': DistanceUnits,
        'default_unit': Distance.STANDARD_UNIT
    },
    'Zoned': {
        'measurement': Area,
        'verbose_name': _('Area'),
        'verbose_name_plural': _('Areas'),
        'unit_choices': AreaUnits,
        'default_unit': Area.STANDARD_UNIT
    },
    'Volumed': {
        'measurement': Volume,
        'verbose_name': _('Volume'),
        'verbose_name_plural': _('Volumes'),
        'unit_choices': VolumeUnits,
        'default_unit': Volume.STANDARD_UNIT
    }
}

class DummyClass:
    pass

for mixin, attrs in MIXINS.items():
    locals()[mixin] = type(mixin, (dd.Model, ), {

        # needed by django.db.models.base.ModelBase
        # the __module__ info is attacted to a class when creating it by (lower level) C.
        '__module__': DummyClass.__dict__.get('__module__'),

        'Meta': type('Meta', (type, ), {
            'abstract': True,
            'verbose_name': attrs.pop('verbose_name'),
            'verbose_name_plural': attrs.pop('verbose_name_plural')
        }),
        'value': MeasurementField(measurement=attrs.pop('measurement')),
        'unit': attrs.pop('unit_choices').field(default=attrs.pop('default_unit'))
    })

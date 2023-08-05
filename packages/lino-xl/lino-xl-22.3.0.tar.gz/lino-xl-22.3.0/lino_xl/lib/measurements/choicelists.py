# -*- coding: UTF-8 -*-
# Copyright 2022 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

from lino.api import dd, _
from measurement.measures import Distance, Area, Volume, Mass, Time

__all__ = [
    'TimeUnits', 'WeightUnits', 'DistanceUnits', 'AreaUnits', 'VolumeUnits',
    'UnitTypes'
]

ALL_UNITS = dict(
    TimeUnits=Time,
    WeightUnits=Mass,
    DistanceUnits=Distance,
    AreaUnits=Area,
    VolumeUnits=Volume
)


class Units(dd.ChoiceList):
    verbose_name = _("Unit")
    verbose_name_plural = _("Units")


for choicelist, measurement in ALL_UNITS.items():
    locals()[choicelist] = type(choicelist, (Units, ), {})
    add = locals()[choicelist].add_item

    TEMP_DICT = dict()
    for alias, symbol in measurement.get_aliases().items():
        if symbol in TEMP_DICT and len(TEMP_DICT[symbol]) > len(alias):
                continue
        TEMP_DICT[symbol] = alias

    for symbol, alias in TEMP_DICT.items():
        add(symbol, _(alias), symbol)

    TEMP_DICT.clear()


class UnitTypes(dd.ChoiceList):
    verbose_name = _("Unit type")
    verbose_name_plural = _("Unit Types")

add = UnitTypes.add_item

add('100', _('Simple'), 'simple')
add('200', _('Compound'), 'compound')

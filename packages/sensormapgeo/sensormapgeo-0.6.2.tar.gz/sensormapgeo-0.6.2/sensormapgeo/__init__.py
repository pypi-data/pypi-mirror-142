# -*- coding: utf-8 -*-

# sensormapgeo, Transform remote sensing images between sensor and map geometry.
#
# Copyright (C) 2020-2021
# - Daniel Scheffler (GFZ Potsdam, daniel.scheffler@gfz-potsdam.de)
# - Helmholtz Centre Potsdam - GFZ German Research Centre for Geosciences Potsdam,
#   Germany (https://www.gfz-potsdam.de/)
#
# This software was developed within the context of the EnMAP project supported
# by the DLR Space Administration with funds of the German Federal Ministry of
# Economic Affairs and Energy (on the basis of a decision by the German Bundestag:
# 50 EE 1529) and contributions from DLR, GFZ and OHB System AG.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Top-level package for sensormapgeo."""

from osgeo import gdal as _gdal

from .transformer_2d import SensorMapGeometryTransformer
from .transformer_3d import SensorMapGeometryTransformer3D
from .version import __version__, __versionalias__   # noqa (E402 + F401)

__all__ = [
    'SensorMapGeometryTransformer',
    'SensorMapGeometryTransformer3D'
]
__author__ = """Daniel Scheffler"""
__email__ = 'daniel.scheffler@gfz-potsdam.de'

# enable GDAL exceptions in the entire project
_gdal.UseExceptions()

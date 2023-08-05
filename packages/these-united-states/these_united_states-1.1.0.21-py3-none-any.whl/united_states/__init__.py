# BSD 3-Clause License
#
# Copyright (c) 2020, 8minute Solar Energy LLC
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Library for performing reverse geocoding of the United States.

Shapefiles come from the United States Census Bureau and are read using pyshp.

    https://www.census.gov/programs-surveys/geography.html

To use, create an instance of UnitedStates and use the methods and attributes
to query or iterate over states. UnitedStates and State objects are read-
only.
"""

# Technical information on the data file can be found at the following URL:
#
# https://www.census.gov/programs-surveys/geography/technical-documentation/complete-technical-documentation/tiger-geo-line.html

import enum
import functools
try:
    from importlib import resources
except ImportError:
    import importlib_resources as resources  # type: ignore[no-redef]
import math
from typing import Any, Callable, Iterator, List, Mapping, overload, Sequence, TypeVar, Union
import types
import zipfile

import shapefile

from .frozenlist import FrozenList, ReadOnlyMixin
from . import geometry


_T = TypeVar('_T')


class Region(enum.Enum):
    """Regions of the United States of America."""
    value: int
    northeast = 1
    midwest = 2
    south = 3
    west = 4
    other = 9


class State(ReadOnlyMixin):
    """A state or territory of the United States of America.

    State objects are read-only and have the following attributes:

        - region:      Region of the U.S. the state falls within
        - division:    Further division of region
        - abbr:        State abbreviation
        - name:        State name
        - area_land:   Total land area in m^2
        - area_water:  Total water area in m^2
        - point:       An internal point (useful for placing labels)
        - bbox:        Bounding box (rectangle) covering all points
        - parts:       Start indices of polygons in the points list
        - points:      Points of all polygons defining state boundaries
    """

    __slots__ = 'region', 'division', 'abbr', 'name', 'area_land', 'area_water', 'bbox', 'point', 'parts', 'points'

    region: Region
    division: int
    abbr: str
    name: str
    area_land: int
    area_water: int
    point: geometry.Point
    bbox: geometry.BBox
    parts: Sequence[int]
    points: Sequence[geometry.Point]

    def __init__(self, shape_record: shapefile.ShapeRecord) -> None:
        record = shape_record.record
        shape = shape_record.shape
        set = lambda name, value: object.__setattr__(self, name, value)
        set('region', Region(int(record[0])))
        set('division', int(record[1]))
        set('abbr', record[5])
        set('name', record[6])
        set('area_land', record[10])
        set('area_water', record[11])
        set('point', (float(record[13]), float(record[12])))
        set('bbox', geometry.BBox(*shape.bbox))
        set('parts', FrozenList(shape.parts))
        set('points', FrozenList(shape.points))

    def __hash__(self) -> int:
        return hash(self.abbr)

    def __repr__(self) -> str:
        return f'{self.__class__.__qualname__}(abbr={self.abbr!r}, name={self.name!r}, bbox={self.bbox!r})'

    def __contains__(self, point: geometry.Point) -> bool:
        points = self.points
        for start, end in zip(self.parts, [*self.parts[1:], 0]):
            if geometry.contains(points[start:end - 1], point):
                return True
        return False


class UnitedStates(Sequence['State'], ReadOnlyMixin):
    """Container for States objects.

    UnitedStates objects are read-only and have the following attributes:

        - bbox:     Bounding box (rectangle) covering all points
        - states:   List of all states and territories in the U.S.
        - by_abbr:  Mapping of state abbreviations to states
        - by_name:  Mapping of state names to states

    Additional, the UnitedStates object may be accessed as a sequence. The
    from_coords() method may be used to find states by lattitude and longitude.
    """

    __slots__ = 'bbox', 'states', 'by_abbr', 'by_name'

    bbox: geometry.BBox
    states: Sequence[State]
    by_abbr: Mapping[str, State]
    by_name: Mapping[str, State]

    def __init__(self, filter: Callable[[State], bool] = None) -> None:
        if filter is None:
            filter = lambda _: True

        with resources.open_binary(__package__, 'shapes.zip') as fp, zipfile.ZipFile(fp) as zipper:
            shape_name, *_ = zipper.filelist[0].filename.rsplit('.', 1)
            with zipper.open(f'{shape_name}.dbf') as dbf, zipper.open(f'{shape_name}.shp') as shp, \
                    zipper.open(f'{shape_name}.shx') as shx, shapefile.Reader(dbf=dbf, shp=shp, shx=shx) as reader:
                assert [name for name, *_ in reader.fields] == [
                    'DeletionFlag', 'REGION', 'DIVISION', 'STATEFP', 'STATENS', 'GEOID', 'STUSPS',
                    'NAME', 'LSAD', 'MTFCC', 'FUNCSTAT', 'ALAND', 'AWATER', 'INTPTLAT', 'INTPTLON']
                states = [st for st in (State(sr) for sr in reader.iterShapeRecords()) if filter(st)]

        if states:
            # Sort from southwest to northeast
            states.sort(key=lambda st: math.sqrt((180 + st.bbox.left) ** 2 + st.bbox.bottom ** 2))
            bbox = functools.reduce(geometry.BBox.__or__, (st.bbox for st in states))
        else:
            bbox = geometry.BBox(0.0, 0.0, 0.0, 0.0)
        set = lambda name, value: object.__setattr__(self, name, value)
        set('bbox', bbox)
        set('states', FrozenList(states))
        set('by_abbr', types.MappingProxyType({st.abbr: st for st in states}))
        set('by_name', types.MappingProxyType({st.name: st for st in states}))

    def __repr__(self) -> str:
        return f'{self.__class__.__qualname__}()'

    def __len__(self) -> int:
        return len(self.states)

    def __iter__(self) -> Iterator[State]:
        return iter(self.states)

    def __contains__(self, point: Any) -> bool:
        try:
            if point in self.bbox:
                self.from_coords(*point)
                return True
        except Exception:
            pass
        return False

    @overload
    def __getitem__(self, item: int) -> State:
        pass
    @overload
    def __getitem__(self, item: slice) -> Sequence[State]:
        pass
    def __getitem__(self, item: Union[int, slice]) -> Union[State, Sequence[State]]:
        return self.states.__getitem__(item)

    def from_coords(self, lat: float, lon: float) -> List[State]:
        """Return a list of states containing the given coordinates.

        Typically, the returned list will contain a single state which contains
        the given decimal latitude/longitude point. The list may be empty for
        coordinates that lie outside the United States or it may contain two or
        three points for coordinates that lie on a boundary line.
        """
        point = lon, lat
        return [st for st in self if point in st.bbox and point in st]

# -*- coding: utf-8 -*-

# Copyright (C) 2022 Luis López <luis@cuarentaydos.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
# USA.


import datetime
import json
from typing import List, Optional, Tuple, Dict, Any, Iterable

import haversine
import requests

from .consts import PRODUCTS
import dataclasses

BASE_URL = (
    "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes"
    "/PreciosCarburantes"
    "/EstacionesTerrestres/{filters}#response-json"
)


@dataclasses.dataclass
class Location:
    address: str
    city: str
    latitude: float
    longitude: float
    province: str
    distance: Optional[float] = None


@dataclasses.dataclass
class Station:
    name: str
    code: str
    products: Dict[str, float]
    location: Location
    misc: Dict[str, Any]


@dataclasses.dataclass
class QueryResult:
    date: datetime.datetime
    stations: List[Station]
    advisory: Optional[str] = None


class CarbuAPI:
    def build_url(self, *, codprov: Optional[str] = None) -> str:
        filters = {}

        if codprov:
            filters["FiltroProvincia"] = codprov

        filters_fragment = "/".join([f"{k}/{v}" for (k, v) in filters.items()])

        return BASE_URL.format(filters=filters_fragment)

    def _query_from_buffer(
        self,
        buffer,
        *,
        codprov: Optional[str] = None,
        products: Optional[List[str]] = None,
        max_distance: Optional[float] = None,
        user_lat_lng: Optional[Tuple[float, float]],
    ):

        data = self.parse(buffer)

        if products is None and max_distance is None:
            return data

        tmp: Iterable[Station] = data.stations

        # Filter products
        if products:
            tmp = self._filter_by_products(tmp, products=products)

        # Filter by distances
        if max_distance and user_lat_lng:
            tmp = self._filter_by_distance(
                tmp, max_distance=max_distance, user_lat_lng=user_lat_lng
            )

        data.stations = list(tmp)
        return data

    def query(
        self,
        *,
        codprov: Optional[str] = None,
        products: Optional[List[str]] = None,
        max_distance: Optional[float] = None,
        user_lat_lng: Optional[Tuple[float, float]],
    ):
        url = self.build_url(codprov=codprov)
        buffer = self.fetch(url)
        return self._query_from_buffer(
            buffer,
            codprov=codprov,
            products=products,
            max_distance=max_distance,
            user_lat_lng=user_lat_lng,
        )

    def _filter_by_products(
        self, collection: Iterable[Station], *, products: Iterable[str]
    ) -> Iterable[Station]:
        wanted = set(products)

        for item in collection:
            known = {x for x in item.products if item.products[x]}
            matches = wanted.intersection(known)
            if matches:
                tmp = {k: item.products[k] for k in matches}
                item.products = tmp
                yield item

    def _filter_by_distance(
        self,
        collection: Iterable[Station],
        *,
        max_distance: float,
        user_lat_lng: Tuple[float, float],
    ) -> Iterable[Station]:
        def _transform(item):
            distance = haversine.haversine(
                (item.location.latitude, item.location.longitude),
                user_lat_lng,
                unit=haversine.Unit.KILOMETERS,
            )
            item.location.distance = distance
            return item

        def _filter(item):
            return item.location.distance <= max_distance

        for item in collection:
            item = _transform(item)
            if _filter(item):
                yield item

    def fetch(self, url: str) -> str:
        return requests.get(url).text

    def parse(self, buff: str) -> QueryResult:
        data = json.loads(buff)

        resultcode = data.get("ResultadoConsulta", "").upper()
        if resultcode != "OK":
            raise DataError(f"ResultadoConsulta: {resultcode}")

        ret = QueryResult(
            date=datetime.datetime.strptime(data["Fecha"], "%d/%m/%Y %H:%M:%S"),
            advisory=data.get("Nota"),
            stations=[self.parse_item(x) for x in data["ListaEESSPrecio"]],
        )
        return ret

    def parse_item(self, item: Dict[str, Any]) -> Station:
        def _float(s):
            return float(s.replace(",", "."))

        products = {name: item.get(f"Precio {name}", None) for (name, _) in PRODUCTS}
        for k in list(item.keys()):
            if k.startswith("Precio "):
                del item[k]

        # Get longitude keys
        lng_keys = [k for k in item if k.lower().startswith("longitud")]
        lng_keys = list(sorted(lng_keys, key=lambda x: len(x)))
        longitude = item[lng_keys[0]]

        for k in lng_keys:
            del item[k]

        ret = Station(
            name=item.pop("Rótulo"),
            code=item.pop("IDEESS"),
            products=dict(products),
            location=Location(
                latitude=_float(item.pop("Latitud")),
                longitude=_float(longitude),
                city=item.pop("Municipio").capitalize(),  # Localidad?
                province=item.pop("Provincia").capitalize(),
                address=item.pop("Dirección").capitalize(),
                distance=None,
            ),
            misc=item,
        )

        return ret


class _BaseError(Exception):
    pass


class DataError(_BaseError):
    pass

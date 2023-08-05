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
from typing import List, Optional, Tuple

import haversine
import requests

from .consts import PRODUCTS

BASE_URL = (
    "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes"
    "/PreciosCarburantes"
    "/EstacionesTerrestres/{filters}#response-json"
)


class CarbuAPI:
    def build_url(self, *, codprov: Optional[str] = None):
        filters = {}
        if codprov:
            filters["FiltroProvincia"] = codprov

        filtersstr = "/".join([f"{k}/{v}" for (k, v) in filters.items()])

        return BASE_URL.format(filters=filtersstr)

    def fetch(self, url):
        return requests.get(url).text

    def parse(self, buff):
        data = json.loads(buff)

        resultcode = data.get("ResultadoConsulta", "").upper()
        if resultcode != "OK":
            raise DataError(f"ResultadoConsulta: {resultcode}")

        meta = {
            "Date": datetime.datetime.strptime(data["Fecha"], "%d/%m/%Y %H:%M:%S"),
            "Advisory": data.get("Nota"),
        }

        prices = [self.parse_item(x) for x in data["ListaEESSPrecio"]]

        return {"Meta": meta, "Prices": prices}

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
        data = self.parse(buffer)

        if products is None and max_distance is None:
            return data

        prices = data["Prices"]

        if products:
            prices = self._filter_by_products(prices, products=products)

        # Filter by distances
        if max_distance and user_lat_lng:
            prices = self._filter_by_distance(
                prices, max_distance=max_distance, user_lat_lng=user_lat_lng
            )

        data["Prices"] = list(prices)
        return data

    def _filter_by_products(self, collection, *, products: List[str]):
        wanted = set(products)

        for item in collection:
            known = {x for x in item["Products"] if item["Products"][x]}
            matches = wanted.intersection(known)
            if matches:
                tmp = {k: item["Products"][k] for k in matches}
                item["Products"] = tmp
                yield item

    def _filter_by_distance(
        self, collection, *, max_distance: float, user_lat_lng: Tuple[float, float]
    ):
        def _transform(item):
            distance = haversine.haversine(
                (item["Location"]["Latitude"], item["Location"]["Longuitude"]),
                user_lat_lng,
                unit=haversine.Unit.KILOMETERS,
            )

            item["Location"]["Distance"] = distance
            return item

        def _filter(item):
            return item["Location"]["Distance"] <= max_distance

        for item in collection:
            item = _transform(item)
            if _filter(item):
                yield item

    def parse_item(self, item):
        def _float(s):
            return float(s.replace(",", "."))

        products = {name: item.get(f"Precio {name}", None) for (name, _) in PRODUCTS}
        for k in list(item.keys()):
            if k.startswith("Precio "):
                del item[k]

        # Get longuitude keys
        lng_keys = [k for k in item if k.lower().startswith("longitud")]
        lng_keys = list(sorted(lng_keys, key=lambda x: len(x)))
        longuitude = item[lng_keys[0]]

        for k in lng_keys:
            del item[k]

        ret = {
            "Station": item.pop("Rótulo", None),
            "Products": dict(products),
            "Location": {
                "Latitude": _float(item.pop("Latitud")),
                "Longuitude": _float(longuitude),
                "City": item.pop("Municipio").capitalize(),  # Localidad?
                "Province": item.pop("Provincia").capitalize(),
                "Address": item.pop("Dirección").capitalize(),
                "Distance": None,
            },
            "Misc": item,
        }

        return ret


class _BaseError(Exception):
    pass


class DataError(_BaseError):
    pass

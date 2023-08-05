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


import argparse
import sys
from pprint import pprint as pp

from . import CarbuAPI
from .consts import PRODUCTS


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--codprov", required=False)
    parser.add_argument(
        "--product",
        action="extend",
        dest="products",
        nargs="+",
        choices=[slug for (name, slug) in PRODUCTS],
        required=False,
    )
    parser.add_argument(
        "--max-distance",
        type=float,
        help="Max distance in km.",
        required=False,
    )
    parser.add_argument(
        "--user-lat",
        type=str,
        help="User latitude",
        required=False,
    )
    parser.add_argument(
        "--user-lng",
        type=str,
        help="User longuitude",
        required=False,
    )

    args = parser.parse_args()

    products = []
    if args.products:
        m = {slug: name for (name, slug) in PRODUCTS}
        products = [m[slug] for slug in args.products]

    if args.max_distance:
        if not args.user_lat and args.user_lng:
            print("User lat/lng is required", file=sys.stderr)
            return 1

        user_lat_lng = (float(args.user_lat), float(args.user_lng))

    else:
        user_lat_lng = None

    api = CarbuAPI()
    pp(
        api.query(
            codprov=args.codprov,
            products=products,
            max_distance=args.max_distance,
            user_lat_lng=user_lat_lng,
        )
    )


if __name__ == "__main__":
    main()

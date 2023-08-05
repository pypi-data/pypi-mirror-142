import os
import datetime
import glob
import tarfile
import statistics
import hashlib
import urllib.parse

import requests
from cached_property import cached_property
import pandas as pd

from eircode.address import Address
from property_price_register.utils import isnan


class Sales():

    def __init__(self, *args, **kwargs):
        self._data = kwargs.get('data', [])

    def contains(self, sale):
        return sale.content_hash in self.content_hashes

    def __getitem__(self, i):
        return self._data[i]

    def __iter__(self):
        return (i for i in self._data)

    def __len__(self):
        return len(self._data)

    def append(self, data):
        self._data.append(data)

    def extend(self, data):
        self._data.extend(data)

    def serialize(self):
        return [
            d.serialize() for d in self
        ]

    @cached_property
    def content_hashes(self):
        return set([d.content_hash for d in self._data])

    @staticmethod
    def from_file(filepath):
        data = None

        ext = os.path.splitext(filepath)[-1]
        if ext in {'.tgz', '.gz'}:
            tar = tarfile.open(filepath, 'r:gz')
            tar.extractall(path=os.path.dirname(filepath))
            tar.close()

            data = []
            for sub_file in glob.iglob(
                os.path.dirname(filepath) + '/**',
                recursive=True
            ):
                ext = os.path.splitext(sub_file)[-1]
                if ext == '.csv':
                    csv_data = pd.read_csv(
                        sub_file.replace('.csv.tgz', '.csv'),
                        encoding='ISO-8859-1'
                    ).to_dict(orient='records')
                    data.extend(csv_data)
        elif ext in {'.csv'}:
            data = pd.read_csv(
                filepath,
                encoding='ISO-8859-1'
            ).to_dict(orient='records')
        else:
            raise Exception()

        sales = Sales()
        for sales_dict in data:
            obj = Sale.parse(
                sales_dict
            )
            sales.append(obj)

        return sales

    @staticmethod
    def from_dir(dirpath):
        sales = Sales()
        search_dir = f'{dirpath}/**'
        for filename in glob.iglob(search_dir, recursive=True):
            if os.path.splitext(filename)[-1] not in {'.tgz', '.gz'}:
                continue
            sales.extend(
                Sales.from_file(
                    filename
                )
            )

        return sales

    def load():
        import property_price_register
        return Sales.from_dir(
            os.path.join(property_price_register.__path__[0], 'resources')
        )

    def save(self, filepath):
        df = pd.DataFrame(self.serialize())
        df = df.drop_duplicates(subset=['date', 'address', 'price', 'county'])
        df.to_csv(filepath)

    @property
    def average_price(self):
        return statistics.mean([s.price for s in self])


class Sale():

    def __init__(self, *args, **kwargs):

        if 'date' in kwargs:
            self.date = kwargs['date']
            self.address = kwargs['address']
            self.postal_code = kwargs['postal_code']
            self.county = kwargs['county']
            self.price = float(kwargs['price'])
            self.not_full_market_price = kwargs['not_full_market_price']
            self.vat_exclusive = kwargs['vat_exclusive']
            self.description_of_property = kwargs['description_of_property']
            self.description_of_property_size = kwargs['description_of_property_size']

            self._lat = kwargs['lat'] if not isnan(kwargs['lat']) else None
            self._lon = kwargs['lon'] if not isnan(kwargs['lon']) else None
            self._full_address = kwargs['full_address'] if not isnan(kwargs['full_address']) else None
            self._match_score = kwargs['match_score'] if not isnan(kwargs['match_score']) else None

            self._eircode_display_name = kwargs['eircode_display_name'] if 'eircode_display_name' in kwargs and not isnan(kwargs['eircode_display_name']) else None
            self._eircode_unique_id = kwargs['eircode_unique_id'] if 'eircode_unique_id' in kwargs and not isnan(kwargs['eircode_unique_id']) else None
            self._eircode_routing_key = kwargs['eircode_routing_key'] if 'eircode_routing_key' in kwargs and not isnan(kwargs['eircode_routing_key']) else None

        else:
            self.date = kwargs['Date of Sale (dd/mm/yyyy)']
            self.address = kwargs['Address']
            self.postal_code = kwargs['Postal Code'].replace('Baile Átha Cliath', 'Dublin').replace('Baile ?tha Cliath', 'Dublin') if not str(kwargs['Postal Code']) == 'nan' else None
            self.county = kwargs['County']
            self.price = float(kwargs['Price (\x80)'].replace('\x80', '').replace(',', ''))
            self.not_full_market_price = kwargs['Not Full Market Price']
            self.vat_exclusive = kwargs['VAT Exclusive']
            self.description_of_property = kwargs['Description of Property']
            self.description_of_property_size = kwargs['Property Size Description']

            self._lat = None
            self._lon = None
            self._full_address = None
            self._match_score = None

            self._eircode_display_name = None
            self._eircode_unique_id = None
            self._eircode_routing_key = None

        if self.description_of_property not in [
            'Second-Hand Dwelling house /Apartment',
            'New Dwelling house /Apartment',
            'New Dwelling house /'
        ]:
            self.description_of_property = None

    @staticmethod
    def parse(data):
        if isinstance(data, Sale):
            return data

        return Sale(
            **data
        )

    def serialize(self):
        return {
            'date': self.date,
            'address': self.address,
            'postal_code': self.postal_code,
            'county': self.county,
            'price': self.price,
            'not_full_market_price': self.not_full_market_price,
            'vat_exclusive': self.vat_exclusive,
            'description_of_property': self.description_of_property,
            'description_of_property_size': self.description_of_property_size,
            'lat': self.lat,
            'lon': self.lon,
            'full_address': self.full_address,
            'match_score': self.match_score,
            'eircode_routing_key': self.eircode_routing_key,
            'eircode_unique_id': self.eircode_unique_id,
            'eircode_display_name': self.eircode_display_name
        }

    @property
    def eircode_routing_key(self):
        if self._eircode_routing_key is None:
            return self._eircode_routing_key

        if self._eircode_routing_key != 'BAD':
            return self._eircode_routing_key

        if self.eircode_address == 'BAD':
            return 'BAD'

        if self.eircode_address.eircode.routing_key not in {'BAD', None}:
            return self.eircode_address.eircode.routing_key

        return self.eircode_address.eircode.routing_key

    @property
    def eircode_unique_id(self):
        if self._eircode_unique_id is None:
            return self._eircode_unique_id

        if self._eircode_unique_id != 'BAD':
            return self._eircode_unique_id

        if self.eircode_address == 'BAD':
            return 'BAD'

        if self.eircode_address.eircode.unique_identifier not in {'BAD', None}:
            return self.eircode_address.eircode.unique_identifier

        return self.eircode_address.eircode.unique_identifier

    @property
    def eircode_display_name(self):
        if self._eircode_display_name is None:
            return self._eircode_display_name

        if self._eircode_display_name != 'BAD':
            return self._eircode_display_name

        if self.eircode_address == 'BAD':
            return 'BAD'

        if self.eircode_address.display_name not in {'BAD', None}:
            return self.eircode_address.display_name

        return self.eircode_address.display_name

    @cached_property
    def eircode_address(self):
        if self.match_score is None:
            return 'BAD'

        if 'BAD' in self.match_score:
            return 'BAD'

        if float(self.match_score) < 0.6:
            return Address(None, eircode=None, skip_set=True)

        #if float(self.match_score) < 0.8:
        #    return 'BAD'

        return Address(self.full_address, throw_ex=True, proxy=True)

    @property
    def timestamp(self):
        return datetime.datetime.strptime(
            self.date,
            '%d/%m/%Y'
        )

    @cached_property
    def geo(self):
        if not os.environ.get('MAPBOX_TOKEN', None):
            return {
                'full_address': 'BAD',
                'lat': 'BAD',
                'lon': 'BAD',
                'match_score': 'BAD'
            }

        location = urllib.parse.quote(self.address + ', ' + self.county)

        if len(location) > 100:
            return {
                'full_address': 'BAD',
                'lat': 'BAD',
                'lon': 'BAD',
                'match_score': 'BAD'
            }

        try:
            data = requests.get('https://api.mapbox.com/geocoding/v5/mapbox.places/' + location + '.json?access_token=' + os.environ.get('MAPBOX_TOKEN', None) + '&country=ie').json()
            return {
                'full_address': data['features'][0]['place_name'],
                'lat': data['features'][0]['center'][1],
                'lon': data['features'][0]['center'][0],
                'match_score': data['features'][0]['relevance']
            }
        except:
            return {
                'full_address': 'BAD',
                'lat': 'BAD',
                'lon': 'BAD',
                'match_score': 'BAD'
            }

    @property
    def lat(self):
        if self._lat is None:
            return self._lat

        if self._lat not in {'BAD', None}:
            return float(self._lat)

        if self.geo['lat'] not in {'BAD', None}:
            return float(self.geo['lat'])

        return self.geo['lat']

    @property
    def lon(self):
        if self._lon is None:
            return self._lon

        if self._lon not in {'BAD', None}:
            return float(self._lon)

        if self.geo['lon'] not in {'BAD', None}:
            return float(self.geo['lon'])

        return self.geo['lon']

    @property
    def full_address(self):
        if self._full_address is None:
            return self._full_address

        if self._full_address not in {'BAD', None}:
            return self._full_address

        if self.geo['full_address'] not in {'BAD', None}:
            return self.geo['full_address']

        return self.geo['full_address']

    @property
    def match_score(self):
        if self._match_score is None:
            return self._match_score

        if self._match_score not in {'BAD', None}:
            return self._match_score

        if self.geo['match_score'] not in {'BAD', None}:
            return self.geo['match_score']

        return self.geo['match_score']

    @property
    def content_hash(self):
        return hashlib.md5(
            f'{self.date}___{self.address}'.encode()
        ).hexdigest()

"""
imports
"""
import os
import requests
import json
import asyncio
import aiohttp
from kraken_entity_client.kraken_entity_client import Kraken_entity_client as Entity

"""
Configure logging
"""
import logging
logging.basicConfig(filename='logs.log',  format='%(asctime)s  | %(levelname)s | %(filename)s | %(funcName)s | line %(lineno)s | %(message)s | %(exc_info)s', level=logging.DEBUG)
logging.info('Logging initialized')





class Kraken_entities_client:

    def __init__(self, record_type = None, record_id = None):

        self._entities = []

        self.offset = None
        self.limit = None

        
        # Configuration of api data
        self.api_url = os.environ.get('KRAKEN_API')
        self.api_headers = {'content-type': 'application/json'}
        self.api_error = None
    
    def set_api_url(self, value):
        """
        Set url for kraken api and make it available to other classes instances
        """
        os.environ['KRAKEN_API'] = value
        self.api_url = value

    
    def get(self, params):
        """
        Retrieves record from database
        """

        return self._get(params)

    
    def post(self):
        """
        Store record to database
        """

        return self._post()

    async def get_async(self, params):
        """
        Retrieves record from database
        """

        return await self._get_async(params)

    
    async def post_async(self):
        """
        Store record to database
        """

        return await self._post_async()

    """
    Properties
    """

    @property
    def entities(self):
        return self._entities
        
    
    @property
    def records(self):

        records = []
        for i in self._entities:
            records.append(i.record)
        return records

    @records.setter
    def records(self, values):

        if not isinstance(values, list):
            values = [values]

        # Convert values to entities
        for i in values:
            e = Entity()
            e.record = i
            self._entities.append(e)
        
        return

    
    @property
    def json(self):
        return json.dumps(self.records, default = str)
        

    """
    I/O
    """

    def _get(self, params):
        """
        Retrieves record from database
        """

        try:
            r = requests.get(self.api_url, headers = self.api_headers, params = params)
            self.records = r.json()
            return True

        except Exception as e:
            self.api_error = e
            return False

    
    def _post(self):
        """
        Store record to database
        """
        try:
            r = requests.post(self.api_url, headers = self.api_headers, data = self.json)
            return True

        except Exception as e:
            self.api_error = e
            return False



    """
    async I/O
    """

    async def _get_async(self, params):
        """
        Retrieves record from database
        """

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.api_url, headers = self.api_headers, params = params) as response:
                    self.records = await response.json()
                    
            return True

        except Exception as e:
            self.api_error = e
            return False

    
    async def _post_async(self):
        """
        Store record to database
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.api_url, headers = self.api_headers, data = self.json) as response:
                    result = await response.text()
            return True

        except Exception as e:
            self.api_error = e
            return False

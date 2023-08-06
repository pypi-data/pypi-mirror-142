"""
imports
"""
import os
import requests
import json
import asyncio
import aiohttp


"""
Configure logging
"""
import logging
logging.basicConfig(filename='logs.log',  format='%(asctime)s  | %(levelname)s | %(filename)s | %(funcName)s | line %(lineno)s | %(message)s | %(exc_info)s', level=logging.DEBUG)
logging.info('Logging initialized')





class Kraken_entity_client:

    def __init__(self, record_type = None, record_id = None):

        self.record_type = record_type
        self.record_id = record_id
        self._record = None
        self.observations = []

        # Metadata
        self.datasource = None
        self.credibility = None

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

    
    
    def get(self):
        """
        Retrieves record from database
        """
        return self._get()

    
    def post(self):
        """
        Store record to database
        """
        return self._post()

    
    async def get_async(self):
        """
        Retrieves record from database
        """
        return await self._get_async()

    
    async def post_async(self):
        """
        Store record to database
        """
        return await self._post_async()

    def get_observations(self):
        """
        Retrieves record from database
        """
        return self._get_observations()

    
    async def get_observations_async(self):
        """
        Retrieves record from database
        """
        return await self._get_observations_async()
    
    """
    Properties
    """

    @property
    def record(self):
        """
        Returns record. Add type and id if missing
        """
        record = self._record
        if not record.get('@type', None):
            record['@type'] = self.record_type
        if not record.get('@id', None):
            record['@id'] = self.record_id
        return record

    @record.setter
    def record(self, value):
        self._record = value
        self.record_type = self._record.get('@type', self.record_type)
        self.record_id = self._record.get('@id', self.record_id)

    @property
    def record_meta(self):
        """
        Returns record with metadata
        """
        record = self.record

        if self.datasource:
            record['datasource'] = self.datasource
            
        if self.credibility:
            record['credibility'] = self.credibility
        return record
    
    @property
    def record_ref(self):
        return {'@type': self.record_type, '@id': self.record_id}
    
    @property
    def json(self):
            
        return json.dumps(self.record_meta, default = str)

    @property
    def schema_org(self):
        """
        Returns json schema.org
        """
        record = self.record
        record['@context'] = "https://schema.org"
        return record
        
    """
    Record properties
    """

    @property
    def url(self):
        return self.record.get('schema:url', None)

    @url.setter
    def url(self, value):
        self.record['schema:url'] = value

    @property
    def contenturl(self):
        return self.record.get('schema:contentUrl', None)

    @contenturl.setter
    def contenturl(self, value):
        self.record['schema:contentUrl'] = value

        
    @property
    def name(self):
        return self.record.get('schema:name', None)

    @name.setter
    def name(self, value):
        self.record['schema:name'] = value


    
    """
    I/O
    """

    def _get(self):
        """
        Retrieves record from database
        """
        try:
            r = requests.get(self.api_url, headers = self.api_headers, params = self.record_ref)
            records = r.json()    
            if len(records) == 1:
                self.record = records[0]
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
        
        return True

    def _get_observations(self):
        """
        Retrieves observations for record
        """
        try:
            r = requests.get(self.api_url + '/observations', headers = self.api_headers, params = self.record_ref)
            self.observations = r.json()    
            return True
            
        except Exception as e:
            self.api_error = e
            return False


    

    """
    async I/O
    """

    async def _get_async(self):
        """
        Retrieves record from database
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.api_url, headers = self.api_headers, params = self.record_ref) as response:
                    records = await response.json()
                    
            if len(records) == 1:
                self.record = records[0]
        
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
        
    
    async def _get_observations_async(self):
        """
        Retrieves record from database
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.api_url + '/observations', headers = self.api_headers, params = self.record_ref) as response:
                    self.observations = await response.json()
                    
            return True
            
        except Exception as e:
            self.api_error = e
            return False
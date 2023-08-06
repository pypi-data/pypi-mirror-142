import re

from dnastack import CollectionServiceClient
from dnastack.configuration import ServiceEndpoint
from dnastack.helpers.environments import env
from dnastack.helpers.logger import get_logger
from dnastack.tests.exam_helper import ExtendedBaseTestCase


class TestSmoke(ExtendedBaseTestCase):
    _logger = get_logger('lib/smoke_test')

    def test_demo(self):
        """
        This is based on the public documentation.

        .. note:: This test is specifically designed for a certain deployment.
        """
        self.skip_until("2022-03-15", "As of 03-14, All collections point to publisher_azure.")

        client = CollectionServiceClient.make(ServiceEndpoint(adapter_type='collections',
                                                              url='https://viral.ai/api/',
                                                              mode='explorer'))
        self._logger.debug('Listing collections...')
        collections = client.list_collections()
        self.assertGreater(len(collections), 0, 'Should have at least ONE collection')

        re_azure_catalog = re.compile(r"FROM publisher_azure\.", re.I)
        re_table_type = re.compile(r"type\s*=\s*'table'")
        from pprint import pprint
        print('-----')
        pprint(collections)
        filtered_collections = [
            c
            for c in collections
            if re_table_type.search(c.itemsQuery) and not re_azure_catalog.search(c.itemsQuery)
        ]
        print('-----')
        pprint(filtered_collections)
        target_collection = filtered_collections

        self._logger.warning(f'C/{target_collection.itemsQuery}')

        data_connect = client.get_data_connect_client(target_collection)

        self._logger.debug('Listing tables...')
        tables = data_connect.list_tables()
        self.assertGreater(len(tables), 0, 'Should have at least ONE table')

        self._logger.debug('Querying...')
        query = f'SELECT * FROM {tables[0].name} LIMIT 20000'
        row_count = 0
        for row in data_connect.query(query):
            row_count += 1
            if row_count % 10000 == 0:
                self._logger.debug(f'Receiving {row_count} rows...')
            self.assertGreater(len(row.keys()), 0)
        self._logger.debug(f'Received {row_count} row(s)')

        self.assertGreater(row_count, 0, 'Should have at least ONE row')

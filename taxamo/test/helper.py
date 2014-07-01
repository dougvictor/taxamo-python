TEST_TOKEN='SamplePrivateTestKey1'
TEST_ADDRESS='https://preprod.taxamo.com'

import taxamo.swagger
import taxamo.api
import unittest

class TaxamoTest(unittest.TestCase):
    api_client = taxamo.swagger.ApiClient(TEST_TOKEN, TEST_ADDRESS)
    api = taxamo.api.ApiApi(api_client)

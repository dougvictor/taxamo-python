import os
import sys
import unittest

from helper import *

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import taxamo.error
import taxamo.http_client
import taxamo.swagger
import taxamo.api

class TaxamoApiConnectivityTest(TaxamoTest):

    def test_validate(self):
        api_client = taxamo.swagger.ApiClient(TEST_TOKEN, TEST_ADDRESS)
        api = taxamo.api.ApiApi(api_client)
        self.assertRaises(
            taxamo.error.ValidationError,
            lambda: api.calculateTax(
                {
                    '__transaction': {
                        'currency_code': 'USD',
                        'buyer_ip': '127.0.0.1',
                        'billing_country_code': 'IE',
                        'force_country_code': 'FR',
                        'transaction_lines': [{'amount': 200,
                                               'custom_id': 'line1'},
                                              {'amount': 100,
                                               'product_type': 'e-book',
                                               'custom_id': 'line2'}
                        ]
                    }}))
        api_client.client = taxamo.http_client.Urllib2Client()

        api = taxamo.api.ApiApi(api_client)
        self.assertRaises(
            taxamo.error.ValidationError,
            lambda: api.calculateTax(
                {
                    '__transaction': {
                        'currency_code': 'USD',
                        'buyer_ip': '127.0.0.1',
                        'billing_country_code': 'IE',
                        'force_country_code': 'FR',
                        'transaction_lines': [{'amount': 200,
                                               'custom_id': 'line1'},
                                              {'amount': 100,
                                               'product_type': 'e-book',
                                               'custom_id': 'line2'}
                        ]
                    }}))


    def test_auth(self):
        api_client = taxamo.swagger.ApiClient(TEST_TOKEN + "!", TEST_ADDRESS)
        api = taxamo.api.ApiApi(api_client)

        self.assertRaises(
            taxamo.error.AuthenticationError,
            lambda: api.getTransaction("non-existent"))

        api_client.client = taxamo.http_client.Urllib2Client()
        api = taxamo.api.ApiApi(api_client)

        self.assertRaises(
            taxamo.error.AuthenticationError,
            lambda: api.getTransaction("non-existent"))

    def test_timeout(self):
        api_client = taxamo.swagger.ApiClient(TEST_TOKEN + "!", "http://i-dont-exist.taxamo.com.nonexistent:123")
        api = taxamo.api.ApiApi(api_client)

        self.assertRaises(
            taxamo.error.APIConnectionError,
            lambda: api.getCurrenciesDict())

        api_client.client = taxamo.http_client.Urllib2Client()
        api = taxamo.api.ApiApi(api_client)

        self.assertRaises(
            taxamo.error.APIConnectionError,
            lambda: api.getCurrenciesDict())

    def test_urllib2(self):
        api_client = taxamo.swagger.ApiClient(TEST_TOKEN, TEST_ADDRESS)
        api_client.client = taxamo.http_client.Urllib2Client()
        api = taxamo.api.ApiApi(api_client)

        resp = api.calculateTax(
            {
                'transaction': {
                    'currency_code': 'USD',
                    'buyer_ip': '127.0.0.1',
                    'billing_country_code': 'IE',
                    'force_country_code': 'FR',
                    'transaction_lines': [{'amount': 200,
                                           'custom_id': 'line1'},
                                          {'amount': 100,
                                           'product_type': 'e-book',
                                           'custom_id': 'line2'}
                    ]
                }})
        self.assertEqual(resp.transaction.countries.detected.code, "IE")
        self.assertEqual(resp.transaction.amount, 300)
        self.assertEqual(resp.transaction.tax_amount, 44.7)
        self.assertEqual(resp.transaction.total_amount, 344.7)






#!/usr/bin/env python
"""
Copyright 2014 Wordnik, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
class Countries:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'by_ip': 'country_schema',
            'forced': 'country_schema',
            'guessed_from_ip': 'country_schema',
            'by_billing': 'country_schema',
            'by_cc': 'country_schema',
            'by_tax_number': 'country_schema',
            'by_token': 'country_schema',
            'detected': 'country_schema'

        }


        #Country detected by IP
        self.by_ip = None # country_schema
        #Country forced by paramters
        self.forced = None # country_schema
        #Country guessed from IP due to lack of other evidence
        self.guessed_from_ip = None # country_schema
        #Country detected by billing country code
        self.by_billing = None # country_schema
        #Country detected by credit card number prefix
        self.by_cc = None # country_schema
        #Country detected from EU TAX number
        self.by_tax_number = None # country_schema
        #Country detected from SMS token
        self.by_token = None # country_schema
        #Country detected from other evidence
        self.detected = None # country_schema
        
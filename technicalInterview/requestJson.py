#!/bin/python3

import math
import os
import random
import re
import sys
import requests

def getDiscountedPrice(barcode: int) -> int:
    # forming the correct URL
    apiURL: str = "https://jsonmock.hackerrank.com/api/inventory?barcode=" + str(barcode)
    # making an HTTP request to the API using requests library and expecting an HTTP response
    response = requests.get(apiURL)
    # checking the HTTP response code
    # in case of success
    if response.status_code == 200:
        # extracting the price and discount from data, since the parsed json is a dictionary, we can retrieve them this way:
        # accessing data and getting the first item

        # check if data is empty or not
        data = response.json().get('data', [])
        if data:
            data = response.json()['data'][0]
            price = data['price']
            discount = data['discount']
            #calculating discounted price
            discounted = round(price - ((discount / 100) * price))
            return (discounted)
        else:
            return (-1)
    # in case of failure
    return (-1) 
if __name__ == '__main__':
    result = getDiscountedPrice(74001755)
    print(result)

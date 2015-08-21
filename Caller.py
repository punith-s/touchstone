__author__ = 'punith'

from config import *

from SignedAPICall import CloudByte
import config

api = CloudByte(api_url, apiKey)

# list TSM
result = api.listTsm(listTsmRequest)
#print result
count = result['listTsmResponse']['count']
print "TSM ID: ", result['listTsmResponse']['listTsm'][count - 1]['id']


# volume group tests


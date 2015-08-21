__author__ = 'punith'

from config import *

from SignedAPICall import CloudByte
import config
import yaml

api = CloudByte(api_url, apiKey)

stream = file('config.yaml', 'r')

yamlconfig = yaml.load(stream)

# list TSM
result = api.listTsm(yamlconfig['listTsmRequest'])
#print result
count = result['listTsmResponse']['count']
print "TSM ID: ", result['listTsmResponse']['listTsm'][count - 1]['id']


# volume group tests

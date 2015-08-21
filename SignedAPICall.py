#!/usr/bin/env python
__author__ = 'punith'

import hashlib, hmac, string, base64, urllib
import json, urllib
 
class SignedAPICall(object):
    def __init__(self, api_url, apiKey):
        self.api_url = api_url
        self.apiKey = apiKey
 
    def request(self, args):
        args['apiKey'] = self.apiKey
 
        self.params = []
        self._sort_request(args)
        self._build_post_request()
 
    def _sort_request(self, args):
        keys = sorted(args.keys())
 
        for key in keys:
            self.params.append(key + '=' + urllib.quote_plus(args[key]))

    def _build_post_request(self):
        self.query = '&'.join(self.params)
        self.value = self.api_url + '?' + self.query
        print 'URL - ' + self.value
 
class CloudByte(SignedAPICall):
    def __getattr__(self, name):
        def handlerFunction(*args, **kwargs):
            print 'command : ' + name
            print args[0]
            if kwargs:
                return self._make_request(name, kwargs)
            return self._make_request(name, args[0])
        return handlerFunction
 
    def _http_get(self, url):
        response = urllib.urlopen(url)
        return response.read()
 
    def _make_request(self, command, args):
        args['response'] = 'json'
        args['command'] = command
        self.request(args)
        data = self._http_get(self.value)
        # The response is of the format {commandresponse: actual-data}
        #print data
        #key = command + "Response"
        return json.loads(data)

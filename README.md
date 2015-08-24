# touchstone

Touchstone will try to be the smart software that will test, regress various components of CloudByte's storage.
Eventually, it shall be tried to replicate these regressions across various OS & ZFS based filesystems.

Current features:
* A python tool that can test CloudByte's REST APIs.

Dependencies :
* YAML parser. ref - http://pyyaml.org/wiki/PyYAML
          
Pre setup w.r.t CloudByte REST testing:
* Install cloudbyte elasticenter
* Set the ElastiCenter url and admin API key. 
        
Usage:
* git clone http://pyyaml.org/wiki/PyYAML
* cd ~/touchstone
* edit config.yaml
* python Caller.py

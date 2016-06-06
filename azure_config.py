#!/bin/python2.7

import os
import sys
from ConfigParser import ConfigParser

class AzureConfig():
    def __init__(self, filepath):
        if not os.path.isfile(filepath):
            print("Error: %s is not a file." % sys.argv[1])
            sys.exit()
        try:
            
            config = ConfigParser()
            config.read(filepath)
            
            self.subscription_id = config.get('Config', 'subscription_id')
            self.username = config.get('Config', 'username')
            self.password = config.get('Config', 'password')
            self.group_name = config.get('Config', 'group_name')
            self.storage_name = config.get('Config', 'storage_name')
            self.virtual_network_name = config.get('Config', 'virtual_network_name')
            self.subnet_name = config.get('Config', 'subnet_name')
            self.region = config.get('Config', 'region')
            self.admin_username = config.get('Config', 'admin_username')
            self.image_publisher = config.get('Config', 'image_publisher')
            self.image_offer = config.get('Config', 'image_offer')
            self.image_sku = config.get('Config', 'image_sku')
            self.image_version = config.get('Config', 'image_version')
            
        except Exception as e:
            print e
            print("Could not read the configuration file '%s'." % filepath)
            sys.exit()
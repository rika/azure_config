#!/bin/python2.7

import os
import sys
from ConfigParser import ConfigParser

import logging
logger = logging.getLogger('azure_config')
if not logger.handlers:
    # log to the console
    console = logging.StreamHandler()
    
    # default log level - make logger/console match
    logger.setLevel(logging.DEBUG)
    console.setLevel(logging.DEBUG)
    
    # formatter
    formatter = logging.Formatter("%(asctime)s %(levelname)7s:  %(message)s", "%Y-%m-%d %H:%M:%S")
    console.setFormatter(formatter)
    logger.addHandler(console)

class AzureConfig():
    def __init__(self, filepath):
        if not os.path.isfile(filepath):
            print("Error: %s is not a file." % sys.argv[1])
            sys.exit()
            
        config = ConfigParser()
        config.read(filepath)
        logger.debug("reading: %s" % filepath) 
        
        self.subscription_id = config.get('Config', 'subscription_id')
        self.username = config.get('Config', 'username')
        self.password = config.get('Config', 'password')
        self.group_name = config.get('Config', 'group_name')
        self.storage_name = config.get('Config', 'storage_name')
        self.virtual_network_name = config.get('Config', 'virtual_network_name')
        self.subnet_name = config.get('Config', 'subnet_name')
        self.region = config.get('Config', 'region')
        self.admin_username = config.get('Config', 'admin_username')
        self.vm_size = config.get('Config', 'vm_size')
        self.key_path = config.get('Config', 'key_path')
        
        try:
            self.template_image_vhd = config.get('Config', 'template_image_vhd')
        except Exception as e:
            logger.debug(e)
            self.template_image_vhd = None
                
        if self.template_image_vhd is None:
            self.image_publisher = config.get('Config', 'image_publisher')
            self.image_offer = config.get('Config', 'image_offer')
            self.image_sku = config.get('Config', 'image_sku')
            self.image_version = config.get('Config', 'image_version')    
            
    def try_get(self, config, section, option, default=None, raw=False, vars=None):
            try:
                value = config.get(config, section, option, raw=raw, vars=vars)
            except Exception:
                logger.debug('%s failed' % option)
                return default
            return value

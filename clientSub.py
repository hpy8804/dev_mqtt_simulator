#author: sven
#date: 2020/03/09
#

#!/usr/bin/python
# -*- coding: UTF-8 -*-

from config import *
import json
import sys
import os
import time
import paho.mqtt.client as mqtt
import ssl

"""
消息解析
"""
def decode_msg(client, topic, msg):
    print("手机端收到topic :" + str(topic))
    print("手机端收到消息:" + str(msg))


def on_subscribe(client, userdata, mid, granted_qos):
    print("On subscribed: qos = %d" %granted_qos)

 
def on_connect(client, userdata, flags, rc):
    print('connected to mqtt with resurt code ', rc)
    client.subscribe(SUB_TOPIC_RSP) 
 
 
def on_message(client, userdata, msg):
    print("\n")
    print("On message!")
    payload = json.loads(msg.payload.decode('utf-8'))
    topic = msg.topic
    decode_msg(client, topic, payload)
 
 
def server_conenet(client):
    client.on_connect = on_connect
    client.on_message = on_message 
    client.on_subscribe = on_subscribe
    client.username_pw_set(USER_NAME, PASS_WORD)
    context = ssl._create_unverified_context()
    client.tls_set_context(context)
    client.connect(SERVER_ADDR, SERVER_PORT, TIME_INTERVAL) 
    client.loop_forever() 
 
 
def server_stop(client):
    client.loop_stop() 
    sys.exit(0)
 
 
def server_main():
    client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + "Sub"
    client = mqtt.Client(client_id, transport='tcp')
    server_conenet(client)
 
 
if __name__ == '__main__':
    server_main()


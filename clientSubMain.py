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


#read json respond file
def read_rsp_json(path):
    with open(path, 'r', encoding='utf8') as fp:
        json_data = json.load(fp)
        return json_data

"""
消息解析
"""
def parser_msg(client, topic, msg):
    print("设备端收到topic :" + str(topic))
    print("设备端收到消息 :" + str(decode_msg(msg)))

    actionReceive = decode_msg(msg)["a"]

    msgCallback = {}
    json_rsp = read_rsp_json("./rsp.json")
    rsp_all_keys = json_rsp.keys()
    for action in rsp_all_keys:
        if action == actionReceive:
            msgCallback = json_rsp[action]
    dicMsgToSend = {"m":{"req":msgCallback}}
    print("设备端发出消息:" + str(dicMsgToSend))
    client.publish(PUB_TOPIC_RSP, json.dumps(dicMsgToSend, ensure_ascii=False))

def on_subscribe(client, userdata, mid, granted_qos):
    print("On subscribed: qos = %d" %granted_qos)

 
def on_connect(client, userdata, flags, rc):
    print('connected to mqtt with resurt code ', rc)
    client.subscribe(SUB_TOPIC) 
 
 
def on_message(client, userdata, msg):
    print("\n")
    print("On message!")
    payload = json.loads(msg.payload.decode('utf-8'))
    topic = msg.topic
    parser_msg(client, topic, payload)
 
 
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
    client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + "SubMain"
    client = mqtt.Client(client_id, transport='tcp')
    server_conenet(client)
 
 
if __name__ == '__main__':
    server_main()


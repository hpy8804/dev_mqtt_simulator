#author: sven
#date: 2020/03/09
#

#!/usr/bin/python
# -*- coding: UTF-8 -*-

from config import *
import json
import paho.mqtt.client as mqtt
import time
import ssl
 
client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
client = mqtt.Client(client_id, transport='tcp')
client.username_pw_set(USER_NAME, PASS_WORD)
context = ssl._create_unverified_context()
client.tls_set_context(context)
client.connect(SERVER_ADDR, SERVER_PORT, TIME_INTERVAL)
client.loop_start()

def send_msg(msg:{}):
    client.publish(PUB_TOPIC, json.dumps(msg, ensure_ascii=False))
    print("手机端发出的请求 : %s" % str(msg))
 
 
if __name__ == '__main__':
    msg = {"a":"testAction2"}
    send_msg(pack_msg(msg))
    time.sleep(0.5)
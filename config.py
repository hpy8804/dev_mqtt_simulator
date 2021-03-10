#author: sven
#date: 2020/03/09
#

#dev ID
DEV_ID = '00000100000120010705'

#topic
SUB_TOPIC = 'smart/{}/dc/1/din/#'.format(DEV_ID)
PUB_TOPIC = 'smart/{}/dc/1/din/config'.format(DEV_ID)
SUB_TOPIC_RSP = 'smart/{}/dc/1/dout/#'.format(DEV_ID)
PUB_TOPIC_RSP = 'smart/{}/dc/1/dout/config'.format(DEV_ID)

#username and pwd
USER_NAME = 'dev_' + DEV_ID
PASS_WORD = 'wiU_UzlAgUxbX1SJkAQ7KBbWAOX-5YWl1bu2L3Qngy4'

#server addr & port
SERVER_ADDR = 'dc03.iotdreamcatcher.net.cn'
SERVER_PORT = 8883

#time interval
TIME_INTERVAL = 60

#pack msg
def pack_msg(msg:{}):
	dicMsgToSend = {"m":{"req":msg}}
	return dicMsgToSend

#decode msg
def decode_msg(msg:{}):
	msg_decode = msg["m"]["req"]
	return msg_decode



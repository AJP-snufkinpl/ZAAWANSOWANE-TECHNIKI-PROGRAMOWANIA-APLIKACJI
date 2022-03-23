import paho.mqtt.client as mqtt
import time

client = mqtt.Client('xXx')
client.username_pw_set('lwpfmkvp:lwpfmkvp', 'ONy0uB8sESyinHD2hRrJ-5Q9hqnUp-4M')
client.connect('goose.rmq2.cloudamqp.com')

while True:

    time.sleep(10)
    msg = client.publish('student/Snufkin PL', f'{time.time()}')
    if msg[0] == 0:
        print("Msg sent")
    else:
        print("msg not sent.....")
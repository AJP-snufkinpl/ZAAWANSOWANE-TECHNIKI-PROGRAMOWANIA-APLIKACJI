import paho.mqtt.client as mqtt


client = mqtt.Client('Pawel Balbierz')
client.username_pw_set('lwpfmkvp:lwpfmkvp', 'ONy0uB8sESyinHD2hRrJ-5Q9hqnUp-4M')
client.connect('goose.rmq2.cloudamqp.com')
client.on_message = lambda client, userdata, msg: print(f'{msg.topic}: {msg.payload.decode()}')
client.subscribe('#')
client.loop_forever()
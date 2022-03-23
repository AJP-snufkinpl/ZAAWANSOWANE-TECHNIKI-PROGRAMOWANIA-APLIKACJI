import time
import pika

#HostName = "goose.rmq2.cloudamqp.com",
#UserName = "lwpfmkvp",
#VirtualHost = "lwpfmkvp",
#Password = "ONy0uB8sESyinHD2hRrJ-5Q9hqnUp-4M"


params = pika.URLParameters('amqp://lwpfmkvp:ONy0uB8sESyinHD2hRrJ-5Q9hqnUp-4M@goose.rmq2.cloudamqp.com/lwpfmkvp')
params.socket_timeout = 5
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='student', durable=True)

while True:
    channel.basic_publish(exchange='', routing_key='student', body='Paweł Balbierz')
    time.sleep(5)

connection.close()

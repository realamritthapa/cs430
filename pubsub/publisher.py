import datetime
from google.cloud import pubsub_v1

google_cloud_project = 'cloud-thapachhetri-amrit'
topic_name = f'projects/{google_cloud_project}/topics/my_topic'

publisher = pubsub_v1.PublisherClient()
try:
    publisher.get_topic(topic=topic_name)
except:
    publisher.create_topic(name=topic_name)

while True:
    msg = input('Enter a message to send: ')
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f'{now} ({topic_name}) : {msg}'
    message_id = publisher.publish(topic_name, data=message.encode('utf-8')).result()
    print(f'Published {message_id} to topic {topic_name}')



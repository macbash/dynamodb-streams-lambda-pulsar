import json
import pulsar
import os

print('Pulsar Producer Started')


def lambda_handler(event, context):
    _pulsar_cluster = os.environ['CLUSTER_IP_PORT'] ## lambda environment variable sample format : pulsar://172.31.76.93:6650
    client = pulsar.Client(_pulsar_cluster)
    _pulsar_topic = os.environ['PULSAR_TOPIC'] ## lambda environment variable for pulsar topic
    producer = client.create_producer(_pulsar_topic)
    for record in event['Records']:
        print(record['eventID'])
        print(record['eventName'])
        print("DynamoDB Record: " + json.dumps(record['dynamodb'], indent=2))
        producer.send((json.dumps(record['dynamodb'], indent=2)).encode('utf-8'))
    client.close()
    return 'Successfully processed {} records.'.format(len(event['Records']))

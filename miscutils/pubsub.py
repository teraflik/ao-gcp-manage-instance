import base64
import json

def json_decode(pubsub_message):
    if 'data' in pubsub_message:
        data = base64.b64decode(pubsub_message['data']).decode('utf-8')
        json_data = json.loads(data)
        return json_data, pubsub_message['attributes']
    else:
        raise ValueError('Missing attribute \'data\' in Pub/Sub Message!')

def json_encode(data):
    pubsub_message = base64.b64encode(json.dumps(data).encode('utf-8'))
    return pubsub_message
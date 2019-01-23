from manage_gcp_instance import manage
from miscutils import pubsub

'''
Sample JSON Message for Pub/Sub: 
{
    "action": "start|stop|create|delete",
    "project": "project-name",
    "zone": "us-central1-a",
    "instance": "instance-name",
    "size": "f1-micro",
    "image-project": "ubuntu-os-cloud",
    "image_family": "ubuntu-1604-lts",
    "metadata": {
       "email" : "someone@somewhere.com
    }
}
'''

def cf_manage_instance(event, context):
    '''
    Function to be executed by the Cloud Function, triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    '''
    json_data, _ = pubsub.json_decode(event)
    
    print(manage.manage_instance(json_data))
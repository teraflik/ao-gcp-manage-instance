from manage_gcp_instance import manage
from miscutils import pubsub

def cf_manage_instance(event, context):
    '''
    Function to be executed by the Cloud Function, triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    '''
    json_data, _ = pubsub.json_decode(event)
    
    print(manage.manage_instance(json_data))
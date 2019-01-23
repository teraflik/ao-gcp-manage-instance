from manage_gcp_instance import manage
from miscutils import pubsub

def cf_manage_instance(data, context):
    '''
    Function to be executed by the Cloud Function
    @params:
        data
        context
    '''
    json_data, _ = pubsub.json_decode(data)
    
    print(manage.manage_instance(json_data))
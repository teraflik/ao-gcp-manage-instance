import os

from oauth2client.client import GoogleCredentials
from manage_instance import manage_instance

KEY_PATH = '/home/user/dev/athenas-owl-dev-70052b87d9c5.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = KEY_PATH

def list_instance():
    credentials = GoogleCredentials.get_application_default()
    service = googleapiclient.discovery.build('compute', 'v1', credentials=credentials)

    PROJECT = 'quantiphi'
    ZONE = 'us-central1-a'
    request = service.instances().list(project=PROJECT, zone=ZONE)
    response = request.execute()
    print(response)
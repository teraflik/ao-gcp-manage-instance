import json
import googleapiclient.discovery

def start_instance(data, compute):
    project = data['project']
    zone = data['zone']
    instance = data['instance']

    return compute.start(project=project, zone=zone, instance=instance).execute()

def stop_instance(data, compute):
    project = data['project']
    zone = data['zone']
    instance = data['instance']

    return compute.stop(project=project, zone=zone, instance=instance).execute()

def delete_instance(data, compute):
    project = data['project']
    zone = data['zone']
    instance = data['instance']

    return compute.delete(project=project, zone=zone, instance=instance).execute()

def create_instance(data, compute):
    pass

# def create_instance(data):
#     project = message['project']
#     zone = message['zone']
#     instance = message['instance'] 
#     size = message['size']
#     image_project = message['image_project']
#     image_family = message['image_family']
#     metadata_email = message['metadata_email']
#     metadata_estimate = message['metadata_estimate']
#     metadata_officetime = message['metadata_officetime']
#     metadata_startupscript = message['metadata_startupscript']

#     image_response = compute.images().getFromFamily(project=image_project, family=image_family).execute()
#     source_disk_image = image_response['selfLink']

#     # Configure the machine
#     machine_type = ("zones/{zone:s}/machineTypes/{size:s}").format(zone, size)
#     #startup_script = open(os.path.join(os.path.dirname(__file__), 'startup-script.sh'), 'r').read()
#     config = {
#         'name': name,
#         'machineType': machine_type,

#         # Specify the boot disk and the image to use as a source.
#         'disks': [
#             {
#                 'boot': True,
#                 'autoDelete': True,
#                 'initializeParams': {
#                     'sourceImage': source_disk_image,
#                 }
#             }
#         ],

#         # Specify a network interface with NAT to access the public
#         # internet.
#         'networkInterfaces': [{
#             'network': 'global/networks/default',
#             'accessConfigs': [
#                 {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
#             ]
#         }],

#         # Allow the instance to access cloud storage and logging.
#         'serviceAccounts': [{
#             'email': 'default',
#             'scopes': [
#                 'https://www.googleapis.com/auth/devstorage.read_write',
#                 'https://www.googleapis.com/auth/logging.write'
#             ]
#         }],

#         # Metadata is readable from the instance and allows you to
#         # pass configuration from deployment scripts to instances.
#         'metadata': {
#             'items': [{
#                 # Startup script is automatically executed by the
#                 # instance upon startup.
#                 'key': 'startup-script',
#                 'value': 'cd ~ && touch "mast_file"'
#             }, {
#                 'key': 'office-time',
#                 'value': 'mumbai-12'
#             }, {
#                 'key': 'estimate',
#                 'value': '2019-01-18'
#             }, {
#                 'key': 'email',
#                 'value': 'raghav.khandelwal@quantiphi.com'
#             }]
#         }
#     }

   

#     print( compute.instances().insert(
#         project=project,
#         zone=zone,
#         body=config).execute())

def manage_instance(data):
    compute = googleapiclient.discovery.build('compute', 'v1').instances()
    return {
        'start': start_instance,
        'stop': stop_instance,
        'create': create_instance,
        'delete': delete_instance
    }[data['action']](data, compute)
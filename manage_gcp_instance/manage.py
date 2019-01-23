import json
import googleapiclient.discovery

def start_instance(data, compute):
    project = data['project']
    zone = data['zone']
    instance = data['instance']

    return compute.instances().start(project=project, zone=zone, instance=instance).execute()

def stop_instance(data, compute):
    project = data['project']
    zone = data['zone']
    instance = data['instance']

    return compute.instances().stop(project=project, zone=zone, instance=instance).execute()

def delete_instance(data, compute):
    project = data['project']
    zone = data['zone']
    instance = data['instance']

    return compute.instances().delete(project=project, zone=zone, instance=instance).execute()

def create_instance(data, compute):
    project = data['project']
    zone = data['zone']
    config = data['config']

    return compute.instances().insert(project=project, zone=zone, body=config).execute()

def manage_instance(data):
    compute = googleapiclient.discovery.build('compute', 'v1')
    return {
        'start': start_instance,
        'stop': stop_instance,
        'create': create_instance,
        'delete': delete_instance
    }[data['action']](data, compute)
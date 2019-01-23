# ao-gcp-manage-instance
Python module that takes care of managing VM Instances on GCP, deploy-able as a Pub/Sub triggered Cloud Function

### Sample JSON Message for Pub/Sub:
```json
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
```

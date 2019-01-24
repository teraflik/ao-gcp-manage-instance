# ao-gcp-manage-instance
Python module that takes care of managing VM Instances on GCP, deploy-able as a Pub/Sub triggered Cloud Function

### Sample JSON Message for Pub/Sub:
#### For Start, Stop and Delete Commands
```json
{
    "action": "start|stop|delete",
    "project": "project-name",
    "zone": "us-central1-a",
    "instance": "instance-name"
}
```

#### For Create Command
Refer [Google Cloud Method: instance.insert()](https://cloud.google.com/compute/docs/reference/rest/v1/instances/insert) and [Google Cloud: Creating and Starting VM Instance](https://cloud.google.com/compute/docs/instances/create-start-instance)
```json
{
    "action": "create",
    "project": "athenas-owl-dev",
    "zone": "us-central1-c",
    "config": {
        "name": "i-ao-intern-deploy-destroy",
        "machineType": "zones/us-central1-c/machineTypes/f1-micro",

        "disks": [
            {
                "boot": "true",
                "autoDelete": "true",
                "initializeParams": {
                    "sourceImage": "projects/ubuntu-os-cloud/global/images/family/ubuntu-1604-lts"
                }
            }
        ],

        "networkInterfaces": [
            {
                "network": "global/networks/default",
                "accessConfigs": [
                    {
                        "type": "ONE_TO_ONE_NAT", 
                        "name": "External NAT"
                    }
                ]
            }
        ],

        "serviceAccounts": [{
        "email": "default",
        "scopes": [
        "https://www.googleapis.com/auth/devstorage.read_write",
        "https://www.googleapis.com/auth/logging.write",
	"https://www.googleapis.com/auth/pubsub"
        ]
        }],

        "metadata": {
            "items": [
                {
                    "key": "office-time",
                    "value": "mumbai-12"
                },
                {
                    "key": "estimate",
                    "value": "2019-02-10"
                },
                {
                    "key": "email",
                    "value": "john.doe@anonymous.com"
                },
                {
                    "key": "startup-script-url",
                    "value": "https://storage.googleapis.com/b-ao-intern-test2/startup-script.sh"
                }
            ]
        }
    }
}
```

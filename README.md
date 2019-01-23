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
    "project": "project-name",
    "zone": "us-central1-a",
    "config": {
        "name": "instance_name",
        "machineType": "zones/asia-south1-c/machineTypes/n1-standard-1",

        "disks": [
            {
                "boot": "true",
                "autoDelete": "true",
                "initializeParams": {
                    "sourceImage": "projects/ubuntu-os-cloud/global/images/family/ubuntu-1604-lts",
                }
            }
        ],

        "networkInterfaces": [{
            "network": "global/networks/default",
            "accessConfigs": [
                {"type": "ONE_TO_ONE_NAT", "name": "External NAT"}
            ]
        }],

        "serviceAccounts": [{
            "email": "default",
            "scopes": [
                "https://www.googleapis.com/auth/devstorage.read_write"
            ]
        }],
        
        "metadata": {
            "items": [{
                "key": "startup-script",
                "value": "cd ~ && touch mast_file"
            }, {
                "key": "office-time",
                "value": "mumbai-12"
            }, {
                "key": "estimate",
                "value": "2019-01-18"
            }, {
                "key": "email",
                "value": "john.doe@anonymous.com"
            }]
        }
    }

}
```

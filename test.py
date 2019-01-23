import os
import base64

import main
from miscutils import local_auth, pubsub

def test():
    payload = {
        "action" : "stop",
        "project" : "quantiphi-rtc",
        "zone" : "asia-south1-c",
        "instance" : "instance-1",
    }
    data = {
        "data": pubsub.json_encode(payload),
        "attributes": {
            "req_type": "local-test"
        }
    }
    local_auth.auth('/home/user/dev/quantiphi-rtc-44af003e6eaa.json')

    context = None
    main.cf_manage_instance(data, context)

if __name__ == '__main__':
    test()
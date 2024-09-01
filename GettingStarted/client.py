import boto3
from uuid import uuid4
import json

iotanalytics = boto3.client("iotanalytics")
response = iotanalytics.batch_put_message(
    channelName="channel",
    messages=[
        {
            'messageId': str(uuid4()),
            'payload': json.dumps({"attribute1": i * 10, "attribute2": i * 10 })
        } for i in range(30)
    ]
)
print(response["batchPutMessageErrorEntries"])

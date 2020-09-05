import boto3
import base64
import json
import os



#rekognition_client = boto3.client('rekognition', aws_session_token=os.getenv('aws_session_token'), aws_access_key_id=os.getenv('aws_access_key_id'), aws_secret_access_key=os.getenv('aws_secret_access_key'), region_name='us-east-1')
rekognition_client = boto3.client('rekognition')

file = open('img.jpg','rb').read()
#print(os.getenv('aws_session_token'))

response = rekognition_client.detect_faces(
    Image={
        'Bytes': file
    },
    Attributes=['ALL']
)
for face in response['FaceDetails']:
    print(json.dumps(face, indent=4, sort_keys=True))

#print(json.dumps(response['FaceDetails']))
#python facial_feature.py > output.json

import boto3
import base64
import json

file = open('text.jpg','rb').read()

rekognition_client = boto3.client('rekognition')

response = rekognition_client.detect_text(
    Image={
        'Bytes': file
    }
)
texts = []
for text in response['TextDetections']:
    if(text['Type'] == "WORD"):
        texts.append(text['DetectedText'])

print(" ".join(texts))
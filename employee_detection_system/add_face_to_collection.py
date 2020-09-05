import boto3
import base64

rekognition_client = boto3.client('rekognition')

file = open('img.jpg','rb').read()

response = rekognition_client.index_faces(
    CollectionId='sunit',
    Image={
        'Bytes': file,
    },
    ExternalImageId='sunit'
)
print(response)


















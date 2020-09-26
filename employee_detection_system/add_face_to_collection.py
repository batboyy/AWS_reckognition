import boto3
import base64
import json

rekognition_client = boto3.client('rekognition')

image_name = ['khadgi.jpg','dip.jpg','img.jpg']

for img in image_name:
    file = open( img ,'rb').read()

    response = rekognition_client.index_faces(
        CollectionId='Geneses',
        Image={
        'Bytes': file,
        },
        ExternalImageId='Geneses'
    )

#print(json.dumps(response, indent=4, sort_keys=True))

    print(img + ' ' +'face added to Geneses Collection')

















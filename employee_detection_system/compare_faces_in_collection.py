import boto3
import base64

file = open('img.jpg','rb').read()

rekognition_client = boto3.client('rekognition')

response = rekognition_client.detect_faces(
    Image={
        'Bytes': file
    }
)
#print(response['FaceDetails'])


if(len(response['FaceDetails'])>0):
    res = rekognition_client.search_faces_by_image(
        CollectionId='sunit',
        Image={
           'Bytes': file
        }
    )
    faceMatches = res['FaceMatches']
    print(res)

else:
    print("The image doesnot contain any faces.")
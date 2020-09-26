import boto3
import base64
import json

file = open('img.jpg','rb').read()

rekognition_client = boto3.client('rekognition')

response = rekognition_client.detect_faces(
    Image={
        'Bytes': file
    }
)
#print(response['FaceDetails'][0])


if(len(response['FaceDetails'])>0):
    res = rekognition_client.search_faces_by_image(
        CollectionId='Geneses',
        Image={
           'Bytes': file
        }
    )
    faceMatches = res['FaceMatches']
    #print(json.dumps(faceMatches, indent=4, sort_keys=True))
    
    if not faceMatches:
        print("Given face is not in the collection")
    else:
        Similarity = str((faceMatches[0]['Similarity']))
        print("Given face matches the collection with"+' '+ Similarity + ' ' +'Similarity')

else:
    print("The image doesnot contain any faces.")
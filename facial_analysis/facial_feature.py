import boto3
import base64
import json
import os


rekognition_client = boto3.client('rekognition')

file = open('image.jpg','rb').read()


response = rekognition_client.detect_faces(
    Image={
        'Bytes': file
    },
    Attributes=['ALL']
)
for face in response['FaceDetails']:
    print('The detected face is between ' + str(face['AgeRange']['Low']) + ' and ' + str(face['AgeRange']['High']) + ' years old')
    print('The detected face is of ' + str(face['Gender']['Value']))

    Sunglass = str(face['Sunglasses']['Value'])

    if Sunglass == 'True':
        print('The detected face is wearing Sunglasses')
    else:
        print('The detected face is not wearing Sunglasses')
        

    #print('Here are the other attributes:')
    #print(json.dumps(face, indent=4, sort_keys=True))




#python facial_feature.py > output.json
 
#  usecases:
#  Interviews detection of employee
#  missing person
#  Making Cars Safer and Personalized
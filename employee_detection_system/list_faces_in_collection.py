import boto3
import json

rekognition_client = boto3.client('rekognition')

response = rekognition_client.list_faces(
    CollectionId='Geneses'
)


print('The total number of faces in collection are' +' '+ str(len(response['Faces'])))

#print(json.dumps(response, indent=4, sort_keys=True))
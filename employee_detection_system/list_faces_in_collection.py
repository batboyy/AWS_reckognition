import boto3

rekognition_client = boto3.client('rekognition')

response = rekognition_client.list_faces(
    CollectionId='sunit'
)

print(response['Faces'])
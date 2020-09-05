import boto3

rekognition_client = boto3.client('rekognition')

response = rekognition_client.create_collection(
    CollectionId='sunit'
)

print(response)
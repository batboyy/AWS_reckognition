import boto3

rekognition_client = boto3.client('rekognition')

try:
    response = rekognition_client.create_collection(
    CollectionId='Geneses'
    )

    print(response['CollectionArn'].split("/")[1] + ' '+ 'collection has been successfully created.')

except:
    print('Collection already exists')

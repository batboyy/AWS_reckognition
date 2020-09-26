import boto3

rekognition_client = boto3.client('rekognition')

try:
    response = rekognition_client.delete_collection(
    CollectionId='Geneses'
    )

    
    status_code = response['StatusCode'] 

    if status_code == 200:
        print("Collection has been successfully deleted")

except:
    print('Collection not found')    
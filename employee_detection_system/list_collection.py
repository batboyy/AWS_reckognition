import boto3

client = boto3.client('rekognition')

response = client.list_collections(
  
)

print("The list of collections are:")
for resp in response['CollectionIds']:
    print(resp)

#print(response['CollectionIds'])
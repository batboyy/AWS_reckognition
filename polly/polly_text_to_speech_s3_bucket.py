import boto3
import time

polly_client = boto3.client('polly')

response = polly_client.start_speech_synthesis_task(VoiceId='Joanna',
                OutputS3BucketName='s3-polly-mp3-storage',
                OutputS3KeyPrefix='key',
                OutputFormat='mp3', 
                Text = 'This is a sample text to be synthesized by AWS polly.')

taskId = response['SynthesisTask']['TaskId']

#print ("Task id is {} ".format(taskId))

task_status = polly_client.get_speech_synthesis_task(TaskId = taskId)

print("MP3 output uploaded to S3 bucket")
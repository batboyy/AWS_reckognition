import boto3
import time

polly_client = boto3.client('polly')

response = polly_client.synthesize_speech(VoiceId ='Aditi',                 #'Joanna'
                OutputFormat='mp3', 
                LanguageCode = 'hi-IN',                                     #'en-US'
                Text = 'नमस्ते! मेरा नाम अदिति है। मैं आपके द्वारा यहां टाइप किए गए किसी भी वाक्य को पढ़ सकती हूं।'
                
                #'Hi, My name is Joanna and AWS Polly is a great managed service for text to speech convert.'
)

file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()


#VoiceId='Aditi'|'Amy'|'Brian'|'Cristiano'|'Dora'|'Emma'|'Ivy'|'Jan'|'Joanna'|'Joey'|'Justin'|'Raveena'
#LanguageCode = 'hi-IN','arb','en-AU','en-US'

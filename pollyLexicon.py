# This example shows regional isolation of data

import boto3
polly = boto3.client('polly',region_name="eu-west-2")
result = polly.synthesize_speech(Text='Hello david this polly with lexicon!',
                                 OutputFormat='mp3',
                                 VoiceId='Aditi',
                                 LexiconNames=["awsLexicon"])

# Read the bytes from the Audio Stream in the response
audio = result['AudioStream'].read()

with open("david_result.mp3","wb") as file:
    file.write(audio)
import io
import json
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Set up the Google Cloud client
client = speech.SpeechClient()

# Set up the output JSON file
output = {'transcriptions': []}

# Iterate over the wave files in the folder
for filename in os.listdir('data'):
    if filename.endswith('.wav'):
        # Load the audio file
        with io.open(f'data/{filename}', 'rb') as audio_file:
            content = audio_file.read()

        # Set the audio encoding and sample rate
        audio = types.RecognitionAudio(content=content)
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code='zh-TW',
            enable_word_time_offsets=True)

        # Perform the transcription
        response = client.recognize(config, audio)

        # Extract the transcription from the response
        transcription = response.results[0].alternatives[0].transcript

        # Extract the word time offsets from the response
        words = response.results[0].alternatives[0].words

        # Add the transcription and word time offsets to the output JSON
        output['transcriptions'].append({
            'filename': filename,
            'transcription': transcription,
            'words': words
        })

# Output the transcriptions to a JSON file
with open('transcriptions.json', 'w') as outfile:
    json.dump(output, outfile)

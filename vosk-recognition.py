import json
import os
import vosk
from absolutepath import MODEL_DIR

# Initialize a list to store the transcriptions
transcriptions = []

# Iterate through the wave files in the folder
for file in os.listdir('data'):
    if file.endswith('.wav'):
        # Load the audio file
        with open(f'data/{file}', 'rb') as audio_file:
            audio = audio_file.read()

        # Set up the Vosk model
        model = vosk.Model(MODEL_DIR)

        # Perform the transcription
        result = model.Decode(audio, 16000)

        # Extract the words, starting times, and ending times from the result
        for word in result['words']:
            transcription = {
                'file': file,
                'word': word['word'],
                'start_time': word['start_time'],
                'end_time': word['end_time']
            }
            transcriptions.append(transcription)

# Output the transcriptions to a JSON file
with open('transcription.json', 'w') as outfile:
    json.dump(transcriptions, outfile)

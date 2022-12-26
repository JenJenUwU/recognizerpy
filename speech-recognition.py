import json
import os
import speech_recognition as sr

# Initialize a list to store the transcriptions
transcriptions = []

# Iterate through the wave files in the folder
for file in os.listdir('data'):
    if file.endswith('.wav'):
        # Load the audio file
        audio = sr.AudioFile(f'data/{file}')

        # Set up the speech recognition object
        r = sr.Recognizer()

        # Extract the words, starting times, and ending times from the audio file
        with audio as source:
            audio = r.record(source)
            words = r.recognize_sphinx(audio, show_all=True)
            for word in words['words']:
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

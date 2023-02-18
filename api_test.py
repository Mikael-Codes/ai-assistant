
# API 
import requests
import pygame
import time
import ffmpeg

API_KEY = ''

# TTS URL with voice ID 
endpoint = 'https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM'

# GET from elevenlabs api voice with api key
# GET to https://api.elevenlabs.io/ with api key
#response = requests.get('https://api.elevenlabs.com/voice/v1/speech/synthesize/?apikey=4338afbf8283b5373ba2ea286ba19c2d&text=Hello World&voice=fr-FR-Julie&format=mp3&speed=1.0&pitch=0.0&volume=1.0')
#response = requests.get('https://api.elevenlabs.com/voice/v1/speech/synthesize/?apikey=' + API_KEY + '&text=Hello World&voice=fr-FR-Julie&format=mp3&speed=1.0&pitch=0.0&volume=1.0')

x = 1


headers = {
    'accept': 'audio/mpeg',
    'xi-api-key': '4338afbf8283b5373ba2ea286ba19c2d',
    'Content-Type': 'application/json',
}

json_data = {
    'text': 'hello worlds',
    'voice_settings': {
        'stability': 0,
        'similarity_boost': 0,
    },
}


response = requests.post('https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM', headers=headers, json=json_data)

# audio_output = ffmpeg.output(response.content, 'F:\Sounds', target='filename.wav')
# audio_output.run()

pygame.mixer.init()

speech_sound = pygame.mixer.Sound(response.content)

speech_sound.play()
time.sleep(3)
pygame.mixer.quit()
x = 5
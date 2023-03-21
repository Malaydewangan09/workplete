import requests
import pyaudio

# Set your Whisper API key
api_key = 'your_api_key'

# Set the URL for the Whisper API transcription endpoint
url = 'https://api.whisper.ai/v1/recognize'

# Define the audio recording parameters
audio_format = pyaudio.paInt16
channels = 1
sample_rate = 16000
chunk_size = 1024
record_duration = 10  # in seconds

# Create a PyAudio object
audio = pyaudio.PyAudio()

# Open a new stream for recording audio
stream = audio.open(format=audio_format,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=chunk_size)

# Start recording
print("Recording started...")
frames = []
for i in range(0, int(sample_rate / chunk_size * record_duration)):
    data = stream.read(chunk_size)
    frames.append(data)

# Stop recording
stream.stop_stream()
stream.close()
audio.terminate()
print("Recording stopped...")

# Convert the recorded audio data to bytes
audio_bytes = b''.join(frames)

# Set the request headers
headers = {'Authorization': 'Bearer ' + api_key, 'Content-Type': 'audio/wav'}

# Send the recorded audio data to the Whisper API for transcription
response = requests.post(url, headers=headers, data=audio_bytes)

# Print the transcription result
if response.ok:
    json_data = response.json()
    if 'result' in json_data:
        result = json_data['result']
        with open('transcription.txt', 'w') as f:
            f.write(result)
else:
    print("Transcription failed with HTTP status code:", response.status_code)
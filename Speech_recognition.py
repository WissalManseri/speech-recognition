import speech_recognition as sr

# Create a Recognizer object
recognizer = sr.Recognizer()

# Set the recognition language
language = 'en-US'
#This sets the language for speech recognition to English (US). 
#note:You can change this to any other language code that is supported by the SpeechRecognition library.
# Configure the microphone
microphone_index = None   # use the default microphone
sample_rate = 44100      # microphone sampling frequency
chunk_size = 2048        # audio chunk size

# Function to transcribe speech to text
#This sets the configuration for the microphone that will be used for speech recognition. By default, the code will use the default microphone of the computer. 
#The sample_rate is the frequency at which audio is sampled, and chunk_size is the number of audio frames per buffer.
def recognize_speech(audio):
    try:
        text = recognizer.recognize_google(audio, language=language)
        print(f"Transcription: {text}")
    except sr.UnknownValueError:
        print("Unable to understand audio")
    except sr.RequestError as e:
        print(f"Error requesting speech recognition: {e}")

# Function to record user's voice
#This function creates a Microphone object and waits for the user to speak. The adjust_for_ambient_noise method is used to adjust the microphone sensitivity to account for any background noise. The listen method of the Microphone object is used to record the audio input from the user.
#Finally, the recognize_speech function is called with the recorded audio input to transcribe the speech to text.
def record_audio():
    # Create a Microphone object
    microphone = sr.Microphone(device_index=microphone_index, sample_rate=sample_rate, chunk_size=chunk_size)

    # Wait for user to speak
    print("Say something...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # Transcribe speech to text
    recognize_speech(audio)

# Function to transcribe an audio file
def transcribe_audio_file(file_path):
    # Open the audio file
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)

    # Transcribe speech to text
    recognize_speech(audio)

# Example usage
if __name__ == '__main__':
    # Record user's voice
    record_audio()

    # Transcribe an audio file
    transcribe_audio_file('audio.wav')

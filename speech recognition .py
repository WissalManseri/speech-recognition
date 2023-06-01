# A basic speech recognition application using Python and the Google Speech Recognition API.
# Import the SpeechRecognition library
import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()

# Use the microphone as source
with sr.Microphone() as source:
    print("Speak Anything : ")

    # Listen for audio input from the microphone
    audio = r.listen(source)

    # Use Google Speech Recognition to transcribe audio
    try:
        # Transcribe the audio to text using Google's speech recognition API
        text = r.recognize_google(audio)

        # Print the transcribed text
        print("You said : {}".format(text))

    # If the speech recognition fails, catch the exception and print an error message
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

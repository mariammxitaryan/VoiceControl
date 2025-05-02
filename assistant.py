import speech_recognition as sr
import pyttsx3
import time
from voicey.config import load_commands, load_settings  # fixed import path
from voicey.commands import dispatch_command

class Voicey:
    def __init__(self):
        # 1. Initialize the speech recognizer and TTS engine
        self.recognizer = sr.Recognizer()
        self.tts = pyttsx3.init()

        # 2. Load your spoken‑command → intent mappings, and settings (like folders, API keys)
        self.commands = load_commands("config/commands.json")
        self.settings = load_settings("config/settings.yaml")

    def speak(self, text: str):
        """Convert text to speech and print it for the user."""
        print(f"Voicey: {text}")
        self.tts.say(text)
        self.tts.runAndWait()

    def listen(self) -> str:
        """Listen on the microphone and return a lowercased string (or empty)."""
        with sr.Microphone() as mic:
            # reduce ambient noise for 0.5s, then capture
            self.recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            audio = self.recognizer.listen(mic)
        try:
            return self.recognizer.recognize_google(audio, language="en-US").lower()
        except sr.UnknownValueError:
            return ""

    def run(self):
        """Main loop: greet once, then continuously listen and dispatch."""
        self.speak("Hello! I’m listening...")
        while True:
            query = self.listen()
            if not query:
                continue

            # iterate all intents → keyword lists
            for intent, keywords in self.commands.items():
                if any(kw in query for kw in keywords):
                    response = dispatch_command(intent, query, self.settings)
                    if response:
                        self.speak(response)
                    break

            # small pause to avoid CPU overuse
            time.sleep(0.2)

if __name__ == "__main__":
    assistant = Voicey()
    assistant.run()

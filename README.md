````markdown
# Voicey — A Beginner‑Friendly Python Voice Assistant

Voicey is a lightweight, modular voice assistant built with Python.  
It supports speech recognition, text‑to‑speech, task management, music playback, weather reports, and Wikipedia summaries.

---

## Features

- **Wake Word & Continuous Listen**: Say “hey voicey” to trigger.  
- **Commands**:  
  - Greeting  
  - Add / List To‑Do Tasks  
  - Play Random MP3 from `music/`  
  - Report Current Time & Date  
  - Fetch Weather via OpenWeatherMap API  
  - Wikipedia Topic Summaries  
- **Offline TTS** with `pyttsx3`  
- **Configurable** via `config/commands.json` and `config/settings.yaml`

---

## Installation

1. Clone this repo:

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. (Ubuntu only) If you see microphone errors:

   ```bash
   sudo apt-get install portaudio19-dev python3-pyaudio
   ```

---

## Configuration

* **`config/commands.json`**: Map spoken phrases to intents.

* **`config/settings.yaml`**:

  ```yaml
  music_folder: music
  weather_api_key: YOUR_OPENWEATHERMAP_API_KEY
  default_city: Yerevan
  wiki_lang: en
  ```

* **Music**: Drop your `.mp3` files into the `music/` directory.

---

## Usage

```bash
python -m voicey.assistant
```

* Voicey will print and speak prompts.
* Speak one of your configured keywords, e.g., “add task buy milk” or “what time is it”.

---

## Extending

* Add new intents in `config/commands.json` and write handlers in `voicey/commands.py`.
* Hook up a GUI using Tkinter or PyQt.
* Deploy on Raspberry Pi for a standalone desktop assistant.

---

## License

This project is licensed under the MIT License.
Feel free to fork and customize!

```

Save that as `README.md`, commit, and push. You’ll then have a clear project repo ready for GitHub!
```

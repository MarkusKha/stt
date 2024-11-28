# Speech-to-Text Transcription App

A fast, local speech-to-text transcription app using OpenAI's Whisper model. Perfect for transcribing audio files for further processing with ChatGPT.

## Features

- Drag-and-drop interface for audio files
- Local processing (no API keys needed)
- Fast transcription using Whisper's base model
- Copy-to-clipboard functionality
- Support for various audio formats

## Setup

1. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Simply drag and drop your audio file into the interface (or click to select)
2. Wait for the transcription to complete
3. Use the "Copy" button to copy the transcribed text
4. Paste directly into ChatGPT for summarization

## Notes

- The app uses Whisper's "base" model for a good balance of speed and accuracy
- Processing time depends on your machine's capabilities and the audio file length
- Supports common audio formats (mp3, wav, m4a, etc.)
- All processing is done locally on your machine

## License
This project is licensed under the MIT License. See the LICENSE file for details.

Copyright © MarkusKha
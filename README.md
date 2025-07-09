# Voice-Based Conversational AI with Sarvam AI

This project implements a voice-based conversational AI system using Sarvam AI's APIs for speech-to-text (ASR), chat completion (LLM), and text-to-speech (TTS). The system records user audio, transcribes it, generates a response using a language model, converts the response to audio, and plays it back. It supports multilingual interactions, particularly for regional Indian languages.

## Features
- **Speech-to-Text**: Transcribes spoken audio using Sarvam AI's ASR API with automatic language detection.
- **Conversational AI**: Generates responses using Sarvam AI's chat completion API.
- **Text-to-Speech**: Synthesizes responses into audio in the detected language using Sarvam AI's TTS API.
- **Multilingual Support**: Handles multiple languages, leveraging Sarvam AI's capabilities for regional Indian languages.
- **Error Handling**: Robust checks for API responses and audio processing.

## Prerequisites
- Python 3.7+
- A valid Sarvam AI API key (sign up at [Sarvam AI](https://sarvam.ai/)).
- A working microphone and speakers for audio input/output.
- Internet connection to access Sarvam AI APIs.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies**:
   Install the required Python libraries using pip:
   ```bash
   pip install requests sounddevice soundfile
   ```

3. **Set Up API Key**:
   Replace `"YOUR_API_KEY"` in the `main.py` script with your actual Sarvam AI API key:
   ```python
   API_KEY = "your-actual-api-key"
   ```

## Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. Follow the prompts:
   - The program will record audio for 5 seconds when prompted ("🎙️ Recording... Speak now!").
   - Speak clearly into your microphone (e.g., "Hello, how are you?" in any supported language).
   - The system will transcribe your speech, generate a response, and play it back as audio.

## How It Works
1. **Audio Recording**: Records 5 seconds of audio using `sounddevice` and saves it as `input.wav`.
2. **Speech-to-Text**: Sends the audio to Sarvam AI's ASR API, which returns the transcribed text and detected language.
3. **Chat Response**: Sends the transcribed text to Sarvam AI's chat API to generate a conversational response.
4. **Text-to-Speech**: Converts the response to audio using Sarvam AI's TTS API in the detected language.
5. **Playback**: Plays the synthesized audio using `sounddevice`.

## Example
- **User Input**: "Hello, how are you?" (spoken in English or Hindi).
- **Transcription**: `transcript = "Hello, how are you?"`, `language = "en"`.
- **Bot Response**: "I'm doing great, thanks for asking!"
- **Output**: The response is played as audio in the same language.

## Configuration
- **Recording Duration**: Modify the `duration` parameter in `record_audio()` to change recording length (default: 5 seconds).
- **API Endpoints**:
  - ASR: `https://api.sarvam.ai/speech-to-text`
  - Chat: `https://api.sarvam.ai/v1/chat/completions`
  - TTS: `https://api.sarvam.ai/text-to-speech`
- **TTS Parameters**: Adjust `speaker`, `pitch`, `pace`, or `loudness` in `synthesize_speech()` for different voice styles.

## Troubleshooting
- **API Errors**: Ensure your Sarvam AI API key is valid and the API endpoints are accessible.
- **Audio Issues**: Verify your microphone and speakers are working and properly configured.
- **Dependencies**: Ensure all required libraries (`requests`, `sounddevice`, `soundfile`) are installed.
- **Language Detection**: If language detection fails, check the audio quality or specify a language code in `transcribe()`.

## Contributing
Contributions are welcome! Please:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Powered by [Sarvam AI](https://sarvam.ai/) APIs for ASR, LLM, and TTS.
- Built with Python libraries: `requests`, `sounddevice`, and `soundfile`.

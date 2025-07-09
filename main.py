import requests
import sounddevice as sd
import soundfile as sf
import time
import base64

#---------- API Key & EndPoints ---------
API_KEY = "YOUR_API_KEY"
ASR_URL = "https://api.sarvam.ai/speech-to-text"
CHAT_URL = "https://api.sarvam.ai/v1/chat/completions"
TTS_URL = "https://api.sarvam.ai/text-to-speech"

# recording the audio of 10 sec
def record_audio(duration=, filename="input.wav"):
    print("Recording... Speak now!")
    data = sd.rec(int(duration * 16000), samplerate=16000, channels=1)
    sd.wait()
    sf.write(filename, data, 16000)
    print("-- Recording complete. --")
    return filename

# sending it to sarvam's ASR to detect the language and convert speech to text using it's APIs
def transcribe(file):
    print("Transcribing with Sarvam ASR...")
    with open(file, "rb") as f:
        files = {
            "file": (file, f, "audio/wav")
        }
        data = {
            "model": "saarika:v2.5",
            "language_code": "unknown"
        }
        headers = {
            "api-subscription-key": API_KEY
        }
        response = requests.post(ASR_URL, headers=headers, files=files, data=data)

    if response.status_code != 200:
        raise RuntimeError(f"ASR failed [{response.status_code}]: {response.text}")

    result = response.json()
    transcript = result.get("transcript")
    lang_code = result.get("language_code")
    if not transcript or not lang_code:
        raise ValueError(f"Invalid ASR response: {result}")
    return transcript, lang_code

# using Sarvam's LLM model to generate response again using it's API only
def chat_with_bot(user_text):
    print("Generating response with Sarvam LLM...")
    payload = {
        "model": "sarvam-m",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant in regional Indian languages."},
            {"role": "user", "content": user_text}
        ],
        "temperature": 0.7
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    resp = requests.post(CHAT_URL, headers=headers, json=payload)
    if resp.status_code != 200:
        raise RuntimeError(f"Chat API failed [{resp.status_code}]: {resp.text}")
    return resp.json()["choices"][0]["message"]["content"]

# converting the generated reponse to audio file with the help of sarvam's TTS model
def synthesize_speech(text, lang_code):
    print("Converting to speech with Sarvam TTS...")
    payload = {
        "inputs": [text],
        "target_language_code": lang_code,
        "speaker": "vidya",
        "pitch": 0.0,
        "pace": 1.0,
        "loudness": 1.0,
        "speech_sample_rate": 16000,
        "enable_preprocessing": False,
        "model": "bulbul:v2"
    }
    headers = {
        "api-subscription-key": API_KEY,
        "Content-Type": "application/json"
    }
    resp = requests.post(TTS_URL, headers=headers, json=payload)
    if resp.status_code != 200:
        raise RuntimeError(f"TTS failed [{resp.status_code}]: {resp.text}")

    result = resp.json()
    if not result.get("audios"):
        raise ValueError("TTS response missing audio data")

    audio_data = base64.b64decode(result["audios"][0])
    with open("response.wav", "wb") as f:
        f.write(audio_data)
    return "response.wav"

# playing the audio file of response generated
def play_audio(file):
    print("Playing response...")
    data, fs = sf.read(file)
    sd.play(data, fs)
    sd.wait()

# integration of all the tasks
def main():
    try:
        wav = record_audio()
        transcript, lang = transcribe(wav)
        print(f"You said [{lang}]: {transcript}")

        reply = chat_with_bot(transcript)
        print(f"Bot reply: {reply}")

        response_audio = synthesize_speech(reply, lang)
        play_audio(response_audio)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

from textwrap import dedent
from faster_whisper import WhisperModel


def transcribe(audio_path: str) -> str:
    model = WhisperModel("tiny")
    segments, info = model.transcribe(audio_path)
    text = "".join([s.text for s in segments]).lstrip()
    return text

if __name__ == "__main__":
    text = transcribe("/Users/nico/Downloads/audio-test-10seconds.m4a")
    print(text)
    assert text[:22] == "This is a longer audio"

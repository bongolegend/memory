from faster_whisper import WhisperModel


def transcribe(audio_path: str) -> str:
    model = WhisperModel("tiny")
    segments, info = model.transcribe(audio_path)
    text = "".join([s.text for s in segments]).lstrip()
    return text


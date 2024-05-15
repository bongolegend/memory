from memory.speech_to_text import transcribe


def test_transcribe_happy_path():
    text = transcribe("tests/audio-test-10seconds.m4a")
    print(text)
    assert text[:22] == "This is a longer audio"
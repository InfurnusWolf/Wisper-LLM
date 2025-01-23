import unittest

class TestWhisperModel(unittest.TestCase):
    def test_model_loading(self):
        from transformers import pipeline
        whisper_model = pipeline("automatic-speech-recognition", model="openai/whisper-small")
        self.assertIsNotNone(whisper_model)

if __name__ == '__main__':
    unittest.main()
import unittest

from assistant import Assistant
from constants import MODEL_NAME, CPU

COMMAND_PATH = "./audios/ligar_lampada.wav"


class TestAssistant(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.assistant = Assistant(MODEL_NAME, CPU)

    def test_model_wrapper_initialized(self):
        self.assertIsNotNone(self.assistant.model_wrapper)
        self.assertTrue(self.assistant.model_wrapper.initialized)

    def test_assistant_initialized(self):
        self.assertTrue(self.assistant.initialized)

    def test_command_execution(self):
        response = self.assistant.receive_command(COMMAND_PATH)

        self.assertIsNotNone(response)
        self.assertEqual(response, ("ligar", "lâmpada"))


if __name__ == '__main__':
    unittest.main()

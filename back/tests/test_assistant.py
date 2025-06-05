import unittest

from assistant import Assistant
from constants import MODEL_NAME, CPU

expected = [
    {
        "path": "./audios/ligar_lampada.wav",
        "command": ("ligar", "lâmpada")
    },
    {
        "path": "./audios/desligar_lampada.wav",
        "command": ("desligar", "lâmpada")
    },
    {
        "path": "./audios/ligar_ar_condicionado.wav",
        "command": ("ligar", "ar condicionado")
    },
    {
        "path": "./audios/desligar_ar_condicionado.wav",
        "command": ("desligar", "ar condicionado")
    },
    {
        "path": "./audios/ligar_projetor.wav",
        "command": ("ligar", "projetor")
    },
    {
        "path": "./audios/desligar_projetor.wav",
        "command": ("desligar", "projetor")
    },
    {
        "path": "./audios/abrir_cortina.wav",
        "command": ("abrir", "cortina")
    },
    {
        "path": "./audios/fechar_cortina.wav",
        "command": ("fechar", "cortina")
    },
    {
        "path": "./audios/iniciar_gravacao.wav",
        "command": ("iniciar", "gravação")
    },
    {
        "path": "./audios/finalizar_gravacao.wav",
        "command": ("finalizar", "gravação")
    }
]



class TestAssistant(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.assistant = Assistant(MODEL_NAME, CPU)

    def test_model_wrapper_initialized(self):
        self.assertIsNotNone(self.assistant.model_wrapper)
        self.assertTrue(self.assistant.model_wrapper.initialized)

    def test_assistant_initialized(self):
        self.assertTrue(self.assistant.initialized)

    def test_commands(self):
        for item in expected:
            response = self.assistant.receive_command(item["path"])

            self.assertIsNotNone(response)
            self.assertEqual(response, item["command"])


if __name__ == '__main__':
    unittest.main()

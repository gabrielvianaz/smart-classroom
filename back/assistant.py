import json

from constants import CONFIG
from model_wrapper import ModelWrapper
from speech_helper import SpeechHelper


class Assistant:
    def __init__(self, model_name: object, device: object) -> None:
        try:
            self.model_wrapper = ModelWrapper(model_name, device)

            if self.model_wrapper.initialized:
                self.speech_helper = SpeechHelper(self.model_wrapper, device)
                self.config = self.__load_config()
                self.initialized = True
            else:
                raise Exception("Model wrapper not initialized")
        except Exception as e:
            print(f"There was an error while initializing the assistant: {e}")
            self.initialized = False

    def receive_command(self, speech_path):
        squeezed_speech = self.speech_helper.squeeze_speech(speech_path)
        transcription = self.speech_helper.transcript_speech(squeezed_speech)
        command = self.speech_helper.remove_stop_words(transcription)
        valid, command_action, command_object = self.__validate_command(command, self.config["actions"])

        if valid:
            return command_action, command_object
        else:
            raise Exception("Invalid command")

    @staticmethod
    def __load_config():
        with open(CONFIG, "r", encoding="utf-8") as config_file:
            config = json.load(config_file)
            config_file.close()

            return config

    @staticmethod
    def __validate_command(command, actions):
        success, command_action, command_object = False, None, None

        if len(command) >= 2:
            command_action = command[0]
            command_object = " ".join([word for word in command[1:]])

            for expected_action in actions:
                if command_action == expected_action["name"]:
                    if command_object in expected_action["objects"]:
                        success = True

                        break

        return success, command_action, command_object

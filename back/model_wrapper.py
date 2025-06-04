from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC


class ModelWrapper:
    def __init__(self, model_name, device):
        try:
            self.processor = Wav2Vec2Processor.from_pretrained(model_name)
            self.model = Wav2Vec2ForCTC.from_pretrained(model_name).to(device)
            self.initialized = True
        except Exception as e:
            print(f"There was an error while initializing the model {model_name}: {e}")
            self.initialized = False

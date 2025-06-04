import pyaudio
import torch
from nltk import corpus, word_tokenize
from torchaudio import load, transforms

from constants import SAMPLE_RATE, CORPUS_LANG


class SpeechHelper:
    def __init__(self, model_wrapper, device):
        self.model = model_wrapper.model
        self.processor = model_wrapper.processor
        self.device = device
        self.recorder = pyaudio.PyAudio()
        self.stop_words = set(corpus.stopwords.words(CORPUS_LANG))

    @staticmethod
    def squeeze_speech(path):
        audio, sampling = load(path)

        if audio.shape[0] > 1:
            audio = torch.mean(audio, dim=0, keepdim=True)

        resample = transforms.Resample(sampling, SAMPLE_RATE)
        audio = resample(audio)

        return audio.squeeze()

    def transcript_speech(self, speech):
        result = self.processor(speech, return_tensors="pt", sampling_rate=SAMPLE_RATE).input_values.to(self.device)
        result = self.model(result).logits

        prediction = torch.argmax(result, dim=-1)
        transcription = self.processor.batch_decode(prediction)[0]

        return transcription.lower()

    def remove_stop_words(self, transcription):
        command = []
        tokens = word_tokenize(transcription)

        for token in tokens:
            if token not in self.stop_words:
                command.append(token)

        return command

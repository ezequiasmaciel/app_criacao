from TTS.api import TTS
import os

# Baixa e prepara o modelo (uma vez)
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=False)

def gerar_audio_coqui(texto, caminho_saida, idioma="pt"):
    tts.tts_to_file(text=texto, file_path=caminho_saida, speaker_wav=None, language=idioma)

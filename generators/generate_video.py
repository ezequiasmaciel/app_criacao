from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip

def gerar_video(caminho_imagem, caminho_audio, caminho_saida, duracao=8):
    imagem = ImageClip(caminho_imagem).set_duration(duracao).resize(height=720)
    audio = AudioFileClip(caminho_audio).set_duration(duracao)
    
    video = CompositeVideoClip([imagem.set_audio(audio)])
    video.write_videofile(caminho_saida, fps=24)

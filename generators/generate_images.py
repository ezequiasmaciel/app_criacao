from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float32)
pipe = pipe.to("cpu")

def gerar_imagem(prompt, caminho_saida):
    imagem = pipe(prompt).images[0]
    imagem.save(caminho_saida)

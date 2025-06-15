import requests
import os

PEXELS_API_KEY = os.getenv("f1C4lI4Ne0UP9tTzsWOPcXHqqbPwYgZodVXUc1EiTNyC5vMhPUlIlVlu")

def buscar_video_pexels(termo_busca):
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": termo_busca, "per_page": 1}
    url = "https://api.pexels.com/videos/search"

    resposta = requests.get(url, headers=headers, params=params)
    if resposta.status_code == 200:
        dados = resposta.json()
        if dados["videos"]:
            return dados["videos"][0]["video_files"][0]["link"]
    return None

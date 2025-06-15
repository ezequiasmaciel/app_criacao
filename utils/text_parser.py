def dividir_em_cenas(texto):
    # Divide o roteiro por parágrafos/cenas
    cenas = [par.strip() for par in texto.split("\n") if par.strip()]
    return cenas

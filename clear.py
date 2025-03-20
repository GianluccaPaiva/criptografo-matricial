def limpar(arquivo):
    with open(arquivo, "w") as f:
        f.truncate()
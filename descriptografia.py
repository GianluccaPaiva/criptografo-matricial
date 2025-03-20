def pegar_elemento_0x0_arquivo(arquivo="base/texto_matrizes.txt"):
    with open(arquivo, "r") as f:
        linhas = f.readlines()
        matrizes = [linhas[i:i+3] for i in range(0, len(linhas), 3)]
        elementos_0x0 = [chr(int(matriz[0].strip().split()[0])) for matriz in matrizes]
        return elementos_0x0

def mostrar_traducao(elementos_0x0):
    for elemento in elementos_0x0:
        print(elemento, end="")
    print(end=" ")

def salvar(elementos_0x0, arquivo="texto/texto_descriptografado.txt"):
    with open(arquivo, "w", encoding="utf-8") as f:
        for elemento in elementos_0x0:
            f.write(elemento)
        f.write("\n")
        
def descriptografar():
    palavras = pegar_elemento_0x0_arquivo()        
    mostrar_traducao(palavras)
    salvar(palavras)
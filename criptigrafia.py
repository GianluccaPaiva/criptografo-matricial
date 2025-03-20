import random
def fragmentar_texto(input_user):
    texto = input_user
    texto = list(texto)
    return texto

def cria_matriz(letra):
    i = 1
    matriz = [None]*9
    matriz[0] = ord(letra)
    while i<9:
        numero = random.randint(0, 200)
        matriz[i] = numero
        i+=1
    return matriz
def salvar_matrizes(matrizes, arquivo="base/texto_matrizes.txt"):
    with open(arquivo, "a") as f:
        for matriz in matrizes:
            elementos = [str(elemento) for elemento in matriz]
            for i in range(0, len(elementos), 3):
                linha = " ".join(elementos[i:i+3])
                f.write(linha + "\n")
                
def salvar_texto_criptografado(texto_criptografado, arquivo="texto/texto_criptografado.txt"):
    with open(arquivo, "ab") as f:
        f.write(texto_criptografado + b" ")
            
def determinante(matriz):
        determinante = matriz[0]*((matriz[4]*matriz[8])-(matriz[5]*matriz[7]))-matriz[1]*((matriz[3]*matriz[8])-(matriz[5]*matriz[6]))+matriz[2]*((matriz[3]*matriz[7])-(matriz[4]*matriz[6]))
        return determinante
    
def criptografar(input_user):
    texto = fragmentar_texto(input_user)
    letras_novas = []
    matrizes = []
    for caractere in texto:
        matriz = cria_matriz(caractere)
        matrizes.append(matriz)
        determinante_valor = determinante(matriz)
        determinante_valor = determinante_valor % 0x10FFFF
        caractere_criptografado = chr(determinante_valor)
        letras_novas.append(caractere_criptografado)
    texto_criptografado = ''.join(letras_novas).encode('utf-8')
    salvar_matrizes(matrizes)
    salvar_texto_criptografado(texto_criptografado)
    print(''.join(letras_novas))

def principal():    
    input_user = input("Digite o texto a ser criptografada: ")
    if len(input_user) > 220:
        print("O texto deve ter no máximo 220 caracteres.")

    else: 
        criptografar(input_user) 


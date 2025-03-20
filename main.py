import criptigrafia
import clear
import descriptografia
def main():
    print("Bem vindo ao programa de criptografia")
    print("Selecione o comando que deseja executar: ")
    print("1 - Criptografar")
    print("2 - Descriptografar")
    print("3 - Limpar arquivos")
    print("4 - Sair")
    input_user = input(">>>>>>: ")
    selecao(input_user)
    
def selecao(input_user):
    if input_user == "1":
        criptigrafia.principal()
    elif input_user == "2":
        descriptografia.descriptografar()
    elif input_user == "3":
        decisao = input("Tem certeza que deseja limpar os arquivos criptografados e descriptografados? (S/N): ")
        if decisao == "S" or "s":
            clear.limpar("base/texto_matrizes.txt")
            clear.limpar("texto/texto_criptografado.txt")
            clear.limpar("texto/texto_descriptografado.txt")
        else:
            print("Operação cancelada.")
            
    elif input_user == "4":
        print("Saindo...")
    else:
        print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
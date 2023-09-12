import random

def obter_opcoes():
    comprimento = int(input("Digite o comprimento desejado para a senha: "))
    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
    incluir_especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

    return comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_especiais

def gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_especiais):
    caracteres = ''

    if incluir_maiusculas:
        caracteres += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if incluir_minusculas:
        caracteres += 'abcdefghijklmnopqrstuvwxyz'
    if incluir_numeros:
        caracteres += '0123456789'
    if incluir_especiais:
        caracteres += '!@#$%^&*()_+=-[]{}|\\:;,.<>?/'

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    print("Bem-vindo ao Gerador de Senhas!")

    comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_especiais = obter_opcoes()

    senha_gerada = gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_especiais)

    print(f"\nSenha gerada: {senha_gerada}")

    input("Pressione <enter> para encerrar!")

if __name__ == "__main__":
    main()




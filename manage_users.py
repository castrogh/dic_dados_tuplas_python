from funcoes import *

usuarios = {}
opcao = menu()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        chave = input("Digite o login: ").upper()
        nome = input("Digite o nome: ").upper()
        data = input("Digite a última data de acesso: ")
        estacao = input("Qual a última estação acessada: ").upper()
        usuarios[chave] = [nome, data, estacao]

    opcao = menu()
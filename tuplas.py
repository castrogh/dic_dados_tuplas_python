usuarios = {}
emails = ["ghscastro@hotmail.com", "ghscastro@gmail.com"]

tupla = list(enumerate(emails))

for chave in range(0, len(tupla)):
    print("E-mail: ", tupla[chave][1]) #usar o [chave][1] faz com que o resultado impresso seja somente o e-mail em si, pois a tupla como um todo é composta por (0, 'ghscastro@hotmail.com'), então, ao usar a variável "chave" eu posiciono o códido no primeiro elemento da lista emails e ao usar o [1], eu posiciono o código no segundo elemento da tupla, que é o email em si
    usuarios[tupla[chave]] = [input("Digite o nome: "), input("Digite o nível: ")]

for chave, dado in usuarios.items():
    print("Usuário: ", chave[0])
    print("E-mail: ", chave[1])
    print("Nome: ", dado[0])
    print("Nível: ", dado[1])
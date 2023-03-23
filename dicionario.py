usuarios = {}

usuarios={ #os objetos (elementos) do dicionário tem sua chave seguida pelos dados, como mostrado abaixo, os dados ficam armazenados numa lista 
    "castrogh": ["Gabriel Castro", "23/03/2023", "Office_X01"],
    "danicastro": ["Danielle Castro", "22/03/2023", "Office_X02"]
}

usuarios["maicao"] = ["Maicão Castro", "20/03/2023", "Office_X03"] #ao adicionar desta forma mais um objeto no dicionário, o Python vai interpretá-lo como um novo registro a ser mostrado e não um novo dicionário

print (usuarios)

print ("####----####")
print (usuarios.get(input("Digite o login que deseja consultar: "))) #o método get traz a informação solicitada pelo usuário, caso ela esteja registrada no dicionário
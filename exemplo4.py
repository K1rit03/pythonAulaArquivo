with open("clientes.txt","a",encoding='utf-8') as arquivo:

    while True:
        try:
            nome = input("Nome: ")
            if nome == '':
                break
            idade = int(input("Idade: "))

            arquivo.write(f'{nome} - {idade }\n')
        except ValueError:
            print("ERRO!! a idade deve ser um numero inteiro")

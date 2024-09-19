with open("exercicio1.txt","a",encoding='utf-8') as arquivo:

    for n in range(10):
        numero = int(input("Insira um numero inteiros"))
        arquivo.write(f'{numero}\n')
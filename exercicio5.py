numeros = []


with open('pares.txt','r',encoding='utf-8') as arquivo1:
    for linha in arquivo1:
        numeros.append(int(linha.strip()))

with open('impares.txt','r',encoding='utf-8') as arquivo2:
    for linha in arquivo2:
        numeros.append(int(linha.strip()))



numeros.sort()

print(f"Numeros em ordem crescente: {numeros}")

with open("todos_numeros.txt","w",encoding='utf-8') as arquivo_juncao:
    for numero in numeros:
        arquivo_juncao.write(f'{numero}\n')

    

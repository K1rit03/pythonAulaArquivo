with open("arquivo.txt","a",encoding='utf-8') as arquivo:
    while True:
        char = str(input('Insira aqui os caracteres desejaveis'))
        if char == "":
            break
        arquivo.write(f'{char}\n')
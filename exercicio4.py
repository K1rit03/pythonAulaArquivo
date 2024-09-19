with open("pares.txt","a",encoding='utf-8') as arquivo:
    with open("impares.txt","a",encoding='utf-8') as arquivoi:
        while True:
            n = int(input("Insira aqui um numero inteiro:"))
            if n == 0:
                break
            if n % 2 == 0:
                arquivo.write(f'{n}\n')
            else:
                arquivoi.write(f'{n}\n')

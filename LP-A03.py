# LPA03
Soma = int()
Quant = int()
while True:
    n = int(input("Digite um número inteiro: "))
    if n == 0:
        break
    Soma = Soma + n
    Quant = Quant + 1
    Media = Soma/Quant

print("Quantidade de números digitados:", Quant)
print("Soma: ", Soma)
print("Média: ", Media)
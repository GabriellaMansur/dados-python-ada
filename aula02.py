# Operadores lógicos, estruturas condicionais e loop while
# Problema gerador: como exibir sequencialmente os números de 1 a 10, um por linha?

numero = 20
numero < 20

"""
Operadores lógicos de comparação

Maior que: >
Maior ou igual: >=
Menor que: <
Menor ou igual: <=
Igual: ==
Diferente: !=

"""

# Operadores lógicos de conjunção
print("Operador and:")
print(True and False)
print(False and False)
print(True and True)

print("Operador or:")
print(False or True)
print(True or True)
print(False or False)

# Estruturas condicionais

# Exemplo 01
media = 3
if media >= 5:
    print("Aprovado")
else:
    print("Reprovado")


# Exemplo 02:
media = 4
frequencia = 50

if media >= 9:
  print("Aprovado")
elif media >= 6 and frequencia >= 75:
  print("Aprovado")
elif media >= 6 and frequencia < 75:
  print("Recuperação")
elif media < 6 and frequencia >= 75:
  print("Recuperação")
else:
  print("Reprovado")


# Laços de repetição
cont = 1

while cont <= 5:
  print("Olá mundo!")
  # cont = cont + 1
  cont += 1


num = float(input("Usuário, digite um número maior do que 10: "))
while num <= 10:
  num = float(input("Número digitado foi menor ou igual a 10! Digite um número maior que 10: "))

print("Legal, o número digitado foi", num)

# Problema gerador
cont = 1
while cont <= 10:
    print(cont)
    cont += 1
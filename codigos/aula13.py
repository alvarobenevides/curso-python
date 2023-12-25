nome = 'Álvaro Benevides'
altura = 1.54
peso = 36.7
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Álvaro Benevides tem 1.54 de altura,
# pesa 36.7 quilos e seu IMC é
# 15.47478495530444
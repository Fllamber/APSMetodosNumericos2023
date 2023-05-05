# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Questão 1
# Dado o número FFFAEDA10 na base hexadecimal.
# faça a conversão para as bases:

number = "0xFFFAEDA10"

print()

# - binária
print("A conversão de FFFAEDA10 para Binário é: ")
print(f'{0xFFFAEDA10:0>36b}')

print()
# - octal
print("A conversão de FFFAEDA10 para Octal é: ")
print(f'{0xFFFAEDA10:0>12o}')

print()
# - heptadecimal (base 7)
def base10_to(num, base):
    numb = []
    r = num
    while r > 0:
        r, q = divmod(r, base)
        numb.append(q)
        #print("R: ", r, "Q: ", q)
    #print(q)
    numb.reverse()
    return int(''.join(map(str, numb)))

print("A conversão de FFFAEDA10 para Heptadecimal  é: ")
print(base10_to(int(number, 16), 7))

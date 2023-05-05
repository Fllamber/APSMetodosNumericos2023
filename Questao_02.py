# -*- coding: utf-8 -*-
#!/usr/bin/env python


# Considere uma variável x com valor inicial igual a 10.
# Em seguida, realize a operação
# x dividido por 2 e atualize x com o resultado.
# Continue nesse processo até que x atinja uma precisão
# de 1E-06. Responda:

from decimal import Decimal
from matplotlib import pyplot as plt


def fexp(number):
    (sign, digits, exponent) = Decimal(number).as_tuple()
    return len(digits) + exponent - 1


def fman(number):
    return Decimal(number).scaleb(-fexp(number)).normalize()


def divide_until(x, div, exponent):
    ''' Função realiza divisões sucessivas
    até chegar no expoente deseado '''
    stop = True
    count = 0
    list_values_x = []
    list_values_y = []
    while stop:
        list_values_y.append(count)
        count += 1
        list_values_x.append(x)
        x = x/div
        # Verifica se o expoente é elevado a -6
        if fexp(x) == exponent:
            aux_fman = fman(x)
            # Se for Elevado a exponent, então verifica se é entre 0 e 2 (1.algo)
            if (aux_fman < 2) and (aux_fman > 0):
                list_values_x.append(x)
                list_values_y.append(count)
                stop = False
    return list_values_x, list_values_y, count


valores, tempo, vezes = divide_until(10, 2, -6)

plt.plot(tempo, valores)
plt.xlabel("Tempo")
plt.ylabel("Valores")

plt.xticks(tempo)

# arrumar os primeiros 5 valores e o ultimo valor
y_val = valores[0:5]
y_val.append(valores[vezes])
plt.yticks(y_val)

# pegar os valores em float e converter para notacao científica
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['%.1E' % Decimal(x) for x in current_values])


# B Qual o ultimo valor de x
print()
print("O último valor de X é: ", valores[vezes])
print()
print("O Método teve iterações: ", vezes)
print()

# Colocar o título da janela
plt.title('Divisão Sucessiva do número ' + str(10))

# mostrar gráfico
plt.show()

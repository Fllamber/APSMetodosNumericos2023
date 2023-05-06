# -*- coding: utf-8 -*-
#!/usr/bin/env python

import numpy as np
#import scipy


def f(xis):
    """
    Essa funcao apresenta múltiplas raízes
    :param xis:
    :return:
    """
    return (xis**4) - (7*(xis**2)) + xis - 8


def f_parada(a, b, precisao):
    if np.abs(a-b) < precisao:
        return True
    else:
        return False

def funcao_bissecao(a, b, itera, precisao):
    """
    Funcao de bissecao
    :param a: O Primeiro ponto de onde a busca vai partir
    :param b: O Segundo ponto de busca
    :param itera: O Número de iterações
    :param precisao: A precisão desejada
    :return: retorna o ponto de raiz no eixo X e a quantidade de iterações
    """
    fa = f(a)
    fb = f(b)
    if f(a)*f(b) >= 0:
        print("Nenhuma raiz ou múltiplas raizes presentes, o método da bissecao não funcionará!")
        return None
    c = (a + b)/2
    i = 0
    criterio_de_precisao = False
    while((i < itera) or (criterio_de_precisao)):
        if criterio_de_precisao:
            break
        i = i + 1
        c = (a + b) / 2
        fx = f(c)
        #print(f'iter={i}, a={a}, b={b}, x={c}, f(a)={fa}, f(b)={fb}, f(x)={fx}')
        if fa * fx < 0:
            b = c
            fb = fx
        elif fb * fx < 0:
            a = c
            fa = fx
        elif fx == 0:
            print("Solução exata encontrada.")
            return c
        else:
            print("Método da Bisseção falhou!")
            return None
        criterio_de_precisao = f_parada(a, b, precisao)
    return c, i

ponto1 = -5
ponto2 = 0

ponto3 = 0
ponto4 = 5

itera1 = 1000
precisao1 = 1e-06
aux, vezes = funcao_bissecao(ponto1, ponto2, itera1, precisao1)
aux2, vezes2 = funcao_bissecao(ponto3, ponto4, itera1, precisao1)

print()
print('O resultado do método da Bisseção entre {} e {} é X = {:E}'.format(ponto1, ponto2, aux))
print('O resultado do método da Bisseção entre {} e {} é X = {:E}'.format(ponto3, ponto4, aux2))
print("Sem essa separação, o método da bissecao falharia pois existem duas raízes.")
print()
print("Medindo-se de 0, A primeira checagem teve", vezes, "iterações")
#print("Medindo-se de 1, A primeira checagem teve", vezes+1, "iterações")
print()
print("Medindo-se de 0, A segunda checagem teve", vezes2, "iterações")
#print("Medindo-se de 1, A segunda checagem teve", vezes2+1, "iterações")

print("Total de iteracoes Bissecao: ", vezes+vezes2, "Iterações")

#print(scipy.optimize.minimize(f, 5, method='L-BFGS-B'))

# Não foi especificado qual método quase-newton era requerido.
# Não consegui implementar mesmo após 25 tentativas
# Nem chatgpt ajuda essa

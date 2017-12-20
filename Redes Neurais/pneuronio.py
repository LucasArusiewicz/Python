import numpy as np
import random

def derivada(n):
	return n * (1 - n)

#Entrada
x = 0.3

#Saida
y = 0.006

#Peso
w = random.random()

#épocas
for i in range(600):

	#funcao de ativacao
	a = np.tanh(x * w)

	#erro (alvo - ativacao)
	e = y - a

	#ajusta peso
	w += x * derivada(e)

	#Exibe aprendizado
	print(a)

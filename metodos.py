from sympy import *
from math import *
from numpy import *
from decimal import Decimal
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

t = Symbol('t')
y = Symbol('y')
f = Function('f')(t, y)

qtlinhas = 0

entrada = open('entrada.txt', 'r')
saida = open('saida.txt', 'w');

#FUNCOES

def euler(yn, tn, h, funcao):
	def f(t,y):
		return eval(funcao)
		#eval retorna o resultado da expressao com as entradas dadas
	yn1 = yn + f(tn, yn)*h
	return yn1

def euler_inverso(yn, tn, h, funcao):
	def f(t,y):
		return eval(funcao)
	yn1 = euler(yn, tn, h, funcao)
	tn1 = tn + h
	yn1 = yn + f(tn1, yn1)*h
	return yn1

def euler_aprimorado(yn, tn, h, funcao):
	def f(t,y):
		return eval(funcao)
	yn1 = euler(yn, tn, h, funcao)
	tn1 = tn + h
	yn1 = yn + (h/2)*(f(tn,yn) + f(tn1,yn1))
	return yn1

def runge_kutta(yn, tn, h, funcao):
	def f(t,y):
		return eval(funcao)
	kn1 = f(tn, yn)
	kn2 = f((tn + (h/2)), (yn + (h/2)*kn1))
	kn3 = f((tn + (h/2)), (yn + (h/2)*kn2))
	kn4 = f((tn + h), (yn + h*kn3))
	yn1 = yn + h*((kn1 + 2*kn2 + 2*kn3 + kn4)/6)
	return yn1

def adam_bashforth2(yn, yn1, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn = f(tn, yn)
	fn1 = f((tn+h), yn1)
	yn2 = (yn1 + (Decimal(3.0/2))*h*fn1 - (Decimal(1.0/2))*h*fn)
	return yn2

def adam_bashforth3(yn, yn1, yn2, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn = f(tn, yn)
	fn1 = f(tn+h, yn1)
	fn2 = f(tn+2*h, yn2)
	yn3 = yn2 + (Decimal(23.0/12))*h*fn2 - (Decimal(4.0/3))*h*fn1 + (Decimal(5.0/12))*h*fn
	return yn3

def adam_bashforth4(yn, yn1, yn2, yn3, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn = f(tn, yn)
	fn1 = f((tn+h), yn1)
	fn2 = f((tn+2*h), yn2)
	fn3 = f((tn+3*h), yn3)
	yn4 = yn3 + (Decimal(55.0/24))*h*fn3 - (Decimal(59.0/24))*h*fn2 + (Decimal(37.0/24))*h*fn1 - (Decimal(3.0/8))*h*fn
	return yn4

def adam_bashforth5(yn, yn1, yn2, yn3, yn4, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn = f(tn, yn)
	fn1 = f(tn+h, yn1)
	fn2 = f(tn+2*h, yn2)
	fn3 = f(tn+3*h, yn3)
	fn4 = f(tn+4*h, yn4)
	yn5 = yn4 + (Decimal(1901.0/720))*h*fn4 - (Decimal(1387.0/360))*h*fn3 + (Decimal(109.0/30))*h*fn2 - (Decimal(637.0/360))*h*fn1 + (Decimal(251.0/720))*h*fn
	return yn5

def adam_bashforth6(yn, yn1, yn2, yn3, yn4, yn5, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn = f(tn, yn)
	fn1 = f(tn+h, yn1)
	fn2 = f(tn+2*h, yn2)
	fn3 = f(tn+3*h, yn3)
	fn4 = f(tn+4*h, yn4)
	fn5 = f(tn+5*h, yn5)
	yn6 = yn5 + (Decimal(4277.0/1440))*h*fn5 - (Decimal(2641.0/480))*h*fn4 + (Decimal(4991.0/720))*h*fn3 - (Decimal(3649.0/720))*h*fn2 + (Decimal(959.0/480))*h*fn1 - (Decimal(95.0/288))*h*fn
	return yn6

def adam_bashforth7(yn, yn1, yn2, yn3, yn4, yn5, yn6, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn = f(tn, yn)
	fn1 = f(tn+h, yn1)
	fn2 = f(tn+2*h, yn2)
	fn3 = f(tn+3*h, yn3)
	fn4 = f(tn+4*h, yn4)
	fn5 = f(tn+5*h, yn5)
	fn6 = f(tn+6*h, yn6)
	yn7 = yn6 + (Decimal(198721.0/60480))*h*fn6 - (Decimal(18637.0/2520))*h*fn5 + (Decimal(235183.0/20160))*h*fn4 - (Decimal(10754.0/945))*h*fn3 + (Decimal(135713.0/20160))*h*fn2 - (Decimal(5603.0/2520))*h*fn1 + (Decimal(19087.0/60480))*h*fn
	return yn7

def adam_bashforth8(yn, yn1, yn2, yn3, yn4, yn5, yn6, yn7, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn = f(tn, yn)
	fn1 = f(tn+h, yn1)
	fn2 = f(tn+2*h, yn2)
	fn3 = f(tn+3*h, yn3)
	fn4 = f(tn+4*h, yn4)
	fn5 = f(tn+5*h, yn5)
	fn6 = f(tn+6*h, yn6)
	fn7 = f(tn+7*h, yn7)
	yn8 = yn7 + (Decimal(16083.0/4480))*h*fn7 - (Decimal(1152169.0/120960))*h*fn6 + (Decimal(242653.0/13440))*h*fn5 - (Decimal(296053.0/13440))*h*fn4 + (Decimal(2102243.0/120960))*h*fn3 - (Decimal(115747.0/13440))*h*fn2 + (Decimal(32863.0/13440))*h*fn1 - (Decimal(5257.0/17280))*h*fn
	return yn8

def adam_moulton2(yn, yn1, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn = f(tn, yn)
	fn1 = f(tn+h, yn1)
	yn1 = yn + (Decimal(1.0/2))*h*fn + (Decimal(1.0/2))*h*fn1
	return yn1

def adam_moulton3(yn, yn1, yn2, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn = f(tn, yn)
	fn1 = f(tn+h, yn1)
	fn2 = f(tn+2*h, yn2)
	yn2 = yn1 + (Decimal(5.0/12))*h*fn2 + (Decimal(2.0/3))*h*fn1 - (Decimal(1.0/12))*h*fn 
	return yn2

def adam_moulton4(yn, yn1, yn2, yn3, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn = f(tn, yn)
	fn1 = f(tn+h, yn1)
	fn2 = f(tn+2*h, yn2)
	fn3 = f(tn+3*h, yn3)
	yn3 = yn2 + (Decimal(9.0/24))*h*fn3 + (Decimal(19.0/24))*h*fn2 - (Decimal(5.0/24))*h*fn1 + (Decimal(1.0/24))*h*fn 
	return yn3

def adam_moulton5(yn, yn1, yn2, yn3, yn4, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn = f(tn, yn)
	fn1 = f(tn+h, yn1)
	fn2 = f(tn+2*h, yn2)
	fn3 = f(tn+3*h, yn3)
	fn4 = f(tn+4*h, yn4)
	yn4 = yn3 + (Decimal(251.0/720))*h*fn4 + (Decimal(646.0/720))*h*fn3 - (Decimal(264.0/720))*h*fn2 + (Decimal(106.0/720))*h*fn1 - (Decimal(19.0/720))*h*fn 
	return yn4

def adam_moulton6(yn, yn1, yn2, yn3, yn4, yn5, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn = f(tn, yn)
	fn1 = f(tn+h, yn1)
	fn2 = f(tn+2*h, yn2)
	fn3 = f(tn+3*h, yn3)
	fn4 = f(tn+4*h, yn4)
	fn5 = f(tn+5*h, yn5)
	yn5 = yn4 + (Decimal(95.0/288))*h*fn5 + (Decimal(1427.0/1440))*h*fn4 - (Decimal(133.0/240))*h*fn3 + (Decimal(241.0/720))*h*fn2 - (Decimal(173.0/1440))*h*fn1 + (Decimal(3.0/160))*h*fn
	return yn5

def adam_moulton7(yn, yn1, yn2, yn3, yn4, yn5, yn6, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn = f(tn, yn)
	fn1 = f(tn+h, yn1)
	fn2 = f(tn+2*h, yn2)
	fn3 = f(tn+3*h, yn3)
	fn4 = f(tn+4*h, yn4)
	fn5 = f(tn+5*h, yn5)
	fn6 = f(tn+6*h, yn6)
	yn6 = yn5 + (Decimal(19087.0/60480))*h*fn6 + (Decimal(2713.0/2520))*h*fn5 - (Decimal(15487.0/20160))*h*fn4 + (Decimal(586.0/945))*h*fn3 - (Decimal(6737.0/20160))*h*fn2 + (Decimal(263.0/2520))*h*fn1 - (Decimal(863.0/60480))*h*fn
	return yn6

def adam_moulton8(yn, yn1, yn2, yn3, yn4, yn5, yn6, yn7, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn = f(tn, yn)
	fn1 = f(tn+h, yn1)
	fn2 = f(tn+2*h, yn2)
	fn3 = f(tn+3*h, yn3)
	fn4 = f(tn+4*h, yn4)
	fn5 = f(tn+5*h, yn5)
	fn6 = f(tn+6*h, yn6)
	fn7 = f(tn+7*h, yn7)
	yn7 = yn6 + (Decimal(5257.0/17280))*h*fn7 + (Decimal(139849.0/120960))*h*fn6 - (Decimal(4511.0/4480))*h*fn5 + (Decimal(123133.0/120960))*h*fn4 - (Decimal(88547.0/120960))*h*fn3 + (Decimal(1537.0/4480))*h*fn2 - (Decimal(11351.0/120960))*h*fn1 + (Decimal(275.0/24192))*h*fn
	return yn7

def inversa2(yn, yn1, yn2, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn2 = f(tn+2*h, yn2)
	yn2 = (Decimal(4.0/3))*yn1 - (Decimal(1.0/3))*yn + (Decimal(2.0/3))*h*fn2 
	return yn2

def inversa3(yn, yn1, yn2, yn3, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn3 = f(tn+3*h, yn3)
	yn3 = (Decimal(18.0/11))*yn2 - (Decimal(9.0/11))*yn1 + (Decimal(2.0/11))*yn + (Decimal(6.0/11))*h*fn3 
	return yn3

def inversa4(yn, yn1, yn2, yn3, yn4, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn4 = f(tn+4*h, yn4)
	yn4 = (Decimal(48.0/25))*yn3 - (Decimal(36.0/25))*yn2 + (Decimal(16.0/25))*yn1 - (Decimal(3.0/25))*yn + (Decimal(12.0/25))*h*fn4 
	return yn4

def inversa5(yn, yn1, yn2, yn3, yn4, yn5, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn5 = f(tn+5*h, yn5)
	yn5 = (Decimal(300.0/137))*yn4 - (Decimal(300.0/137))*yn3 + (Decimal(200.0/137))*yn2 - (Decimal(75.0/137))*yn1 + (Decimal(12.0/137))*yn + (Decimal(60.0/137))*h*fn5 
	return yn5

def inversa6(yn, yn1, yn2, yn3, yn4, yn5, yn6, tn, h, funcao):
	def f(t,y):
		return eval(str(funcao))
	fn6 = f(tn+6*h, yn6)
	yn6 = (Decimal(360.0/147))*yn5 - (Decimal(450.0/147))*yn4 + (Decimal(400.0/147))*yn3 - (Decimal(225.0/147))*yn2 + (Decimal(72.0/147))*yn1 - (Decimal(10.0/147))*yn + (Decimal(60.0/147))*h*fn6 
	return yn6

for linha in entrada:
	qtlinhas = qtlinhas + 1
	vetor = linha.split(' ')

	if str(vetor[0]) == 'euler':
		saida.write('Metodo de Euler\n')
		y0 = Decimal(vetor[1])
		t0 = Decimal(vetor[2])
		h = Decimal(vetor[3])
		passos = int(vetor[4])
		funcao = vetor[5]

		saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
		saida.write('h = %s\n' % str(h))
		saida.write('0 %s\n' % str(y0))

		eulert = []
		eulery = []

		yn = y0
		tn = t0
		for i in range(1, passos+1):
			yn1 = euler(yn, tn, h, funcao)
			saida.write('%d %s\n' % (i, str(yn1)))
			yn = yn1
			tn = tn + h
			eulert.append(tn)
			eulery.append(yn1)
		saida.write('\n')

	if str(vetor[0]) == 'euler_inverso':
		saida.write('Metodo de Euler Inverso\n')
		y0 = Decimal(vetor[1])
		t0 = Decimal(vetor[2])
		h = Decimal(vetor[3])
		passos = int(vetor[4])
		funcao = vetor[5]

		saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
		saida.write('h = %s\n' % str(h))
		saida.write('0 %s\n' % str(y0))

		eulerit = []
		euleriy = []

		yn = y0
		tn = t0
		for i in range(1, passos+1):
			yn1 = euler_inverso(yn, tn, h, funcao)
			saida.write('%d %s\n' % (i, str(yn1)))
			yn = yn1
			tn = tn + h
			eulerit.append(tn)
			euleriy.append(yn1)
		saida.write('\n')

	if str(vetor[0]) == 'euler_aprimorado':
		saida.write('Metodo de Euler Aprimorado\n')
		y0 = Decimal(vetor[1])
		t0 = Decimal(vetor[2])
		h = Decimal(vetor[3])
		passos = int(vetor[4])
		funcao = vetor[5]

		saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
		saida.write('h = %s\n' % str(h))
		saida.write('0 %s\n' % str(y0))

		eulerat = []
		euleray = []

		yn = y0
		tn = t0
		for i in range(1, passos+1):
			yn1 = euler_aprimorado(yn, tn, h, funcao)
			saida.write('%d %s\n' % (i, str(yn1)))
			yn = yn1
			tn =  tn + h
			eulerat.append(tn)
			euleray.append(yn1)
		saida.write('\n')

	if str(vetor[0]) == 'runge_kutta':
		saida.write('Metodo de Runge-Kutta\n')
		y0 = Decimal(vetor[1])
		t0 = Decimal(vetor[2])
		h = Decimal(vetor[3])
		passos = int(vetor[4])
		funcao = vetor[5]

		saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
		saida.write('h = %s\n' % str(h))
		saida.write('0 %s\n' % str(y0))

		runget = []
		rungey = []

		yn = y0
		tn = t0
		for i in range(1, passos+1):
			yn1 = runge_kutta(yn, tn, h, funcao)
			saida.write('%d %s\n' % (i, str(yn1)))
			yn = yn1
			tn = tn + h
			runget.append(tn)
			rungey.append(yn1)
		saida.write('\n')

	if str(vetor[0]) == 'adam_bashforth' or str(vetor[0]) == 'adam_bashforth_by_euler' or str(vetor[0]) == 'adam_bashforth_by_euler_inverso' or str(vetor[0]) == 'adam_bashforth_by_euler_aprimorado' or str(vetor[0]) == 'adam_bashforth_by_runge_kutta':
		
		if str(vetor[0]) == 'adam_bashforth_by_euler':
			saida.write('Metodo de Adams-Bashforth por Euler\n')
			recebePontos = 0
		elif str(vetor[0]) == 'adam_bashforth_by_euler_inverso':
			saida.write('Metodo de Adams-Bashforth por Euler Inverso\n')
			recebePontos = 0
		elif str(vetor[0]) == 'adam_bashforth_by_euler_aprimorado':
			saida.write('Metodo de Adams-Bashforth por Euler Aprimorado\n')
			recebePontos = 0
		elif str(vetor[0]) == 'adam_bashforth_by_runge_kutta':
			saida.write('Metodo de Adams-Bashforth por Runge-Kutta\n')
			recebePontos = 0
		elif str(vetor[0]) == 'adam_bashforth':
			saida.write('Metodo de Adams-Bashforth\n')
			recebePontos = 1

		abt = []
		aby = []

		ordem = int(vetor[len(vetor) - 1])

		y0 = Decimal(vetor[1])

		if ordem == 2:
			if recebePontos == 1:
				y1 = Decimal(vetor[2])
				t0 = Decimal(vetor[3])
				h = Decimal(vetor[4])
				passos = int(vetor[5])
				funcao = str(vetor[6])

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('y(%s) = %s\n' % (str(t0+h), str(y1)))

			elif recebePontos == 0:
				t0 = Decimal(vetor[2])
				h = Decimal(vetor[3])
				passos = int(vetor[4])
				funcao = vetor[5]

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))

				if str(vetor[0]) == 'adam_bashforth_by_euler':
					y1 = euler(y0, t0, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_euler_inverso':
					y1 = euler_inverso(y0, t0, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_euler_aprimorado':
					y1 = euler_aprimorado(y0, t0, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_runge_kutta':
					y1 = runge_kutta(y0, t0, h, funcao) 

			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))
			saida.write('1 %s\n' % str(y1))

			abt.append(t0)
			aby.append(y0)
			abt.append(t0+h)
			aby.append(y1)

			yn = y0
			yn1 = y1
			tn = t0
			for i in range(2, passos+1):
				yn2 = adam_bashforth2(yn, yn1, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn2)))
				abt.append(tn+2*h)
				aby.append(yn2)
				yn = yn1
				yn1 = yn2
				tn = tn + h
			saida.write('\n')

		if ordem == 3:
			y0 = Decimal(vetor[1])
			if recebePontos == 1:
				y1 = Decimal(vetor[2])
				y2 = Decimal(vetor[3])
				t0 = Decimal(vetor[4])
				h = Decimal(vetor[5])
				passos = int(vetor[6])
				funcao = str(vetor[7])

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('y(%s) = %s\n' % (str(t0+h), str(y1)))
				saida.write('y(%s) = %s\n' % (str(t0+2*h), str(y2)))

			elif recebePontos == 0:
				t0 = Decimal(vetor[2])
				h = Decimal(vetor[3])
				passos = int(vetor[4])
				funcao = vetor[5]

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))

				if str(vetor[0]) == 'adam_bashforth_by_euler':
					y1 = euler(y0, t0, h, funcao)
					y2 = euler(y1, t0+h, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_euler_inverso':
					y1 = euler_inverso(y0, t0, h, funcao)
					y2 = euler_inverso(y1, t0+h, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_euler_aprimorado':
					y1 = euler_aprimorado(y0, t0, h, funcao)
					y2 = euler_aprimorado(y1, t0+h, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_runge_kutta':
					y1 = runge_kutta(y0, t0, h, funcao)
					y2 = runge_kutta(y1, t0+h, h, funcao)

			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))
			saida.write('1 %s\n' % str(y1))
			saida.write('2 %s\n' % str(y2))

			abt.append(t0)
			aby.append(y0)
			abt.append(t0+h)
			aby.append(y1)
			abt.append(t0+2*h)
			aby.append(y2)

			yn = y0
			yn1 = y1
			yn2 = y2
			tn = t0
			for i in range(3, passos+1):
				yn3 = adam_bashforth3(yn, yn1, yn2, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn3)))
				abt.append(tn+3*h)
				aby.append(yn3)
				yn = yn1
				yn1 = yn2
				yn2 = yn3
				tn = tn + h
			saida.write('\n')

		if ordem == 4:
			y0 = Decimal(vetor[1])
			if recebePontos == 1:
				y1 = Decimal(vetor[2])
				y2 = Decimal(vetor[3])
				y3 = Decimal(vetor[4])
				t0 = Decimal(vetor[5])
				h = Decimal(vetor[6])
				passos = int(vetor[7])
				funcao = str(vetor[8])

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('y(%s) = %s\n' % (str(t0+h), str(y1)))
				saida.write('y(%s) = %s\n' % (str(t0+2*h), str(y2)))
				saida.write('y(%s) = %s\n' % (str(t0+3*h), str(y3)))

			elif recebePontos == 0:
				t0 = Decimal(vetor[2])
				h = Decimal(vetor[3])
				passos = int(vetor[4])
				funcao = vetor[5]

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))

				if str(vetor[0]) == 'adam_bashforth_by_euler':
					y1 = euler(y0, t0, h, funcao)
					y2 = euler(y1, t0+h, h, funcao)
					y3 = euler(y2, t0+2*h, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_euler_inverso':
					y1 = euler_inverso(y0, t0, h, funcao)
					y2 = euler_inverso(y1, t0+h, h, funcao)
					y3 = euler_inverso(y2, t0+2*h, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_euler_aprimorado':
					y1 = euler_aprimorado(y0, t0, h, funcao)
					y2 = euler_aprimorado(y1, t0+h, h, funcao)
					y3 = euler_aprimorado(y2, t0+2*h, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_runge_kutta':
					y1 = runge_kutta(y0, t0, h, funcao)
					y2 = runge_kutta(y1, t0+h, h, funcao)
					y3 = runge_kutta(y2, t0+2*h, h, funcao)
				
			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))
			saida.write('1 %s\n' % str(y1))
			saida.write('2 %s\n' % str(y2))
			saida.write('3 %s\n' % str(y3))

			abt.append(t0)
			aby.append(y0)
			abt.append(t0+h)
			aby.append(y1)
			abt.append(t0+2*h)
			aby.append(y2)
			abt.append(t0+3*h)
			aby.append(y3)

			yn = y0
			yn1 = y1
			yn2 = y2
			yn3 = y3
			tn = t0
			for i in range(4, passos+1):
				yn4 = adam_bashforth4(yn, yn1, yn2, yn3, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn4)))
				abt.append(tn+4*h)
				aby.append(yn4)
				yn = yn1
				yn1 = yn2
				yn2 = yn3
				yn3 = yn4
				tn = tn + h
			saida.write('\n')

		if ordem == 5:
			y0 = Decimal(vetor[1])
			if recebePontos == 1:
				y1 = Decimal(vetor[2])
				y2 = Decimal(vetor[3])
				y3 = Decimal(vetor[4])
				y4 = Decimal((vetor[5]))
				t0 = Decimal(vetor[6])
				h = Decimal(vetor[7])
				passos = int(vetor[8])
				funcao = str(vetor[9])

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('y(%s) = %s\n' % (str(t0+h), str(y1)))
				saida.write('y(%s) = %s\n' % (str(t0+2*h), str(y2)))
				saida.write('y(%s) = %s\n' % (str(t0+3*h), str(y3)))
				saida.write('y(%s) = %s\n' % (str(t0+4*h), str(y4)))

			elif recebePontos == 0:
				t0 = Decimal(vetor[2])
				h = Decimal(vetor[3])
				passos = int(vetor[4])
				funcao = vetor[5]

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				
				if str(vetor[0]) == 'adam_bashforth_by_euler':
					y1 = euler(y0, t0, h, funcao)
					y2 = euler(y1, t0+h, h, funcao)
					y3 = euler(y2, t0+2*h, h, funcao)
					y4 = euler(y3, t0+3*h, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_euler_inverso':
					y1 = euler_inverso(y0, t0, h, funcao)
					y2 = euler_inverso(y1, t0+h, h, funcao)
					y3 = euler_inverso(y2, t0+2*h, h, funcao)
					y4 = euler_inverso(y3, t0+3*h, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_euler_aprimorado':
					y1 = euler_aprimorado(y0, t0, h, funcao)
					y2 = euler_aprimorado(y1, t0+h, h, funcao)
					y3 = euler_aprimorado(y2, t0+2*h, h, funcao)
					y4 = euler_aprimorado(y3, t0+3*h, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_runge_kutta':
					y1 = runge_kutta(y0, t0, h, funcao)
					y2 = runge_kutta(y1, t0+h, h, funcao)
					y3 = runge_kutta(y2, t0+2*h, h, funcao)
					y4 = runge_kutta(y3, t0+3*h, h, funcao)

			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))
			saida.write('1 %s\n' % str(y1))
			saida.write('2 %s\n' % str(y2))
			saida.write('3 %s\n' % str(y3))
			saida.write('4 %s\n' % str(y4))

			abt.append(t0)
			aby.append(y0)
			abt.append(t0+h)
			aby.append(y1)
			abt.append(t0+2*h)
			aby.append(y2)
			abt.append(t0+3*h)
			aby.append(y3)
			abt.append(t0+4*h)
			aby.append(y4)

			yn = y0
			yn1= y1
			yn2 = y2
			yn3 = y3
			yn4 = y4
			tn = t0
			for i in range(5, passos+1):
				yn5 = adam_bashforth5(yn, yn1, yn2, yn3, yn4, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn5)))
				abt.append(tn+5*h)
				aby.append(yn5)
				yn = yn1
				yn1 = yn2
				yn2 = yn3
				yn3 = yn4
				yn4 = yn5
				tn = tn + h
			saida.write('\n')

		if ordem == 6:
			y0 = Decimal(vetor[1])
			if recebePontos == 1:
				y1 = Decimal(vetor[2])
				y2 = Decimal(vetor[3])
				y3 = Decimal(vetor[4])
				y4 = Decimal(vetor[5])
				y5 = Decimal(vetor[6])
				t0 = Decimal(vetor[7])
				h = Decimal(vetor[8])
				passos = int(vetor[9])
				funcao = str(vetor[10])

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('y(%s) = %s\n' % (str(t0+h), str(y1)))
				saida.write('y(%s) = %s\n' % (str(t0+2*h), str(y2)))
				saida.write('y(%s) = %s\n' % (str(t0+3*h), str(y3)))
				saida.write('y(%s) = %s\n' % (str(t0+4*h), str(y4)))
				saida.write('y(%s) = %s\n' % (str(t0+5*h), str(y5)))

			elif recebePontos == 0:
				t0 = Decimal(vetor[2])
				h = Decimal(vetor[3])
				passos = int(vetor[4])
				funcao = vetor[5]

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))

				if str(vetor[0]) == 'adam_bashforth_by_euler':
					y1 = euler(y0, t0, h, funcao)
					y2 = euler(y1, t0+h, h, funcao)
					y3 = euler(y2, t0+2*h, h, funcao)
					y4 = euler(y3, t0+3*h, h, funcao)
					y5 = euler(y4, t0+4*h, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_euler_inverso':
					y1 = euler_inverso(y0, t0, h, funcao)
					y2 = euler_inverso(y1, t0+h, h, funcao)
					y3 = euler_inverso(y2, t0+2*h, h, funcao)
					y4 = euler_inverso(y3, t0+3*h, h, funcao)
					y5 = euler_inverso(y4, t0+4*h, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_euler_aprimorado':
					y1 = euler_aprimorado(y0, t0, h, funcao)
					y2 = euler_aprimorado(y1, t0+h, h, funcao)
					y3 = euler_aprimorado(y2, t0+2*h, h, funcao)
					y4 = euler_aprimorado(y3, t0+3*h, h, funcao)
					y5 = euler_aprimorado(y4, t0+4*h, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_runge_kutta':
					y1 = runge_kutta(y0, t0, h, funcao)
					y2 = runge_kutta(y1, t0+h, h, funcao)
					y3 = runge_kutta(y2, t0+2*h, h, funcao)
					y4 = runge_kutta(y3, t0+3*h, h, funcao)
					y5 = runge_kutta(y4, t0+4*h, h, funcao)

			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))
			saida.write('1 %s\n' % str(y1))
			saida.write('2 %s\n' % str(y2))
			saida.write('3 %s\n' % str(y3))
			saida.write('4 %s\n' % str(y4))
			saida.write('5 %s\n' % str(y5))

			abt.append(t0)
			aby.append(y0)
			abt.append(t0+h)
			aby.append(y1)
			abt.append(t0+2*h)
			aby.append(y2)
			abt.append(t0+3*h)
			aby.append(y3)
			abt.append(t0+4*h)
			aby.append(y4)
			abt.append(t0+5*h)
			aby.append(y5)

			yn = y0
			yn1= y1
			yn2 = y2
			yn3 = y3
			yn4 = y4
			yn5 = y5
			tn = t0
			for i in range(6, passos+1):
				yn6 = adam_bashforth6(yn, yn1, yn2, yn3, yn4, yn5, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn6)))
				abt.append(tn+6*h)
				aby.append(yn6)
				yn = yn1
				yn1 = yn2
				yn2 = yn3
				yn3 = yn4
				yn4 = yn5
				yn5 = yn6
				tn = tn + h
			saida.write('\n')

		if ordem == 7:
			y0 = Decimal(vetor[1])
			if recebePontos == 1:
				y1 = Decimal(vetor[2])
				y2 = Decimal(vetor[3])
				y3 = Decimal(vetor[4])
				y4 = Decimal(vetor[5])
				y5 = Decimal(vetor[6])
				y6 = Decimal(vetor[7])
				t0 = Decimal(vetor[8])
				h = Decimal(vetor[9])
				passos = int(vetor[10])
				funcao = str(vetor[11])

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('y(%s) = %s\n' % (str(t0+h), str(y1)))
				saida.write('y(%s) = %s\n' % (str(t0+2*h), str(y2)))
				saida.write('y(%s) = %s\n' % (str(t0+3*h), str(y3)))
				saida.write('y(%s) = %s\n' % (str(t0+4*h), str(y4)))
				saida.write('y(%s) = %s\n' % (str(t0+5*h), str(y5)))
				saida.write('y(%s) = %s\n' % (str(t0+6*h), str(y6)))

			elif recebePontos == 0:
				t0 = Decimal(vetor[2])
				h = Decimal(vetor[3])
				passos = int(vetor[4])
				funcao = vetor[5]

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))

				if str(vetor[0]) == 'adam_bashforth_by_euler':
					y1 = euler(y0, t0, h, funcao)
					y2 = euler(y1, t0+h, h, funcao)
					y3 = euler(y2, t0+2*h, h, funcao)
					y4 = euler(y3, t0+3*h, h, funcao)
					y5 = euler(y4, t0+4*h, h, funcao)
					y6 = euler(y5, t0+5*h, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_euler_inverso':
					y1 = euler_inverso(y0, t0, h, funcao)
					y2 = euler_inverso(y1, t0+h, h, funcao)
					y3 = euler_inverso(y2, t0+2*h, h, funcao)
					y4 = euler_inverso(y3, t0+3*h, h, funcao)
					y5 = euler_inverso(y4, t0+4*h, h, funcao)
					y6 = euler_inverso(y5, t0+5*h, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_euler_aprimorado':
					y1 = euler_aprimorado(y0, t0, h, funcao)
					y2 = euler_aprimorado(y1, t0+h, h, funcao)
					y3 = euler_aprimorado(y2, t0+2*h, h, funcao)
					y4 = euler_aprimorado(y3, t0+3*h, h, funcao)
					y5 = euler_aprimorado(y4, t0+4*h, h, funcao)
					y6 = euler_aprimorado(y5, t0+5*h, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_runge_kutta':
					y1 = runge_kutta(y0, t0, h, funcao)
					y2 = runge_kutta(y1, t0+h, h, funcao)
					y3 = runge_kutta(y2, t0+2*h, h, funcao)
					y4 = runge_kutta(y3, t0+3*h, h, funcao)
					y5 = runge_kutta(y4, t0+4*h, h, funcao)
					y6 = runge_kutta(y5, t0+5*h, h, funcao)

			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))
			saida.write('1 %s\n' % str(y1))
			saida.write('2 %s\n' % str(y2))
			saida.write('3 %s\n' % str(y3))
			saida.write('4 %s\n' % str(y4))
			saida.write('5 %s\n' % str(y5))
			saida.write('6 %s\n' % str(y6))

			abt.append(t0)
			aby.append(y0)
			abt.append(t0+h)
			aby.append(y1)
			abt.append(t0+2*h)
			aby.append(y2)
			abt.append(t0+3*h)
			aby.append(y3)
			abt.append(t0+4*h)
			aby.append(y4)
			abt.append(t0+5*h)
			aby.append(y5)
			abt.append(t0+6*h)
			aby.append(y6)

			yn = y0
			yn1= y1
			yn2 = y2
			yn3 = y3
			yn4 = y4
			yn5 = y5
			yn6 = y6
			tn = t0
			for i in range(7, passos+1):
				yn7 = adam_bashforth7(yn, yn1, yn2, yn3, yn4, yn5, yn6, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn7)))
				abt.append(tn+7*h)
				aby.append(yn7)
				yn = yn1
				yn1 = yn2
				yn2 = yn3
				yn3 = yn4
				yn4 = yn5
				yn5 = yn6
				yn6 = yn7
				tn = tn + h
			saida.write('\n')

		if ordem == 8:
			y0 = Decimal(vetor[1])
			if recebePontos == 1:
				y1 = Decimal(vetor[2])
				y2 = Decimal(vetor[3])
				y3 = Decimal(vetor[4])
				y4 = Decimal(vetor[5])
				y5 = Decimal(vetor[6])
				y6 = Decimal(vetor[7])
				y7 = Decimal(vetor[8])
				t0 = Decimal(vetor[9])
				h = Decimal(vetor[10])
				passos = int(vetor[11])
				funcao = str(vetor[12])

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('y(%s) = %s\n' % (str(t0+h), str(y1)))
				saida.write('y(%s) = %s\n' % (str(t0+2*h), str(y2)))
				saida.write('y(%s) = %s\n' % (str(t0+3*h), str(y3)))
				saida.write('y(%s) = %s\n' % (str(t0+4*h), str(y4)))
				saida.write('y(%s) = %s\n' % (str(t0+5*h), str(y5)))
				saida.write('y(%s) = %s\n' % (str(t0+6*h), str(y6)))
				saida.write('y(%s) = %s\n' % (str(t0+7*h), str(y7)))

			elif recebePontos == 0:
				t0 = Decimal(vetor[2])
				h = Decimal(vetor[3])
				passos = int(vetor[4])
				funcao = vetor[5]

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))

				if str(vetor[0]) == 'adam_bashforth_by_euler':
					y1 = euler(y0, t0, h, funcao)
					y2 = euler(y1, t0+h, h, funcao)
					y3 = euler(y2, t0+2*h, h, funcao)
					y4 = euler(y3, t0+3*h, h, funcao)
					y5 = euler(y4, t0+4*h, h, funcao)
					y6 = euler(y5, t0+5*h, h, funcao)
					y7 = euler(y6, t0+6*h, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_euler_inverso':
					y1 = euler_inverso(y0, t0, h, funcao)
					y2 = euler_inverso(y1, t0+h, h, funcao)
					y3 = euler_inverso(y2, t0+2*h, h, funcao)
					y4 = euler_inverso(y3, t0+3*h, h, funcao)
					y5 = euler_inverso(y4, t0+4*h, h, funcao)
					y6 = euler_inverso(y5, t0+5*h, h, funcao)
					y7 = euler_inverso(y6, t0+6*h, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_euler_aprimorado':
					y1 = euler_aprimorado(y0, t0, h, funcao)
					y2 = euler_aprimorado(y1, t0+h, h, funcao)
					y3 = euler_aprimorado(y2, t0+2*h, h, funcao)
					y4 = euler_aprimorado(y3, t0+3*h, h, funcao)
					y5 = euler_aprimorado(y4, t0+4*h, h, funcao)
					y6 = euler_aprimorado(y5, t0+5*h, h, funcao)
					y7 = euler_aprimorado(y6, t0+6*h, h, funcao)
				elif str(vetor[0]) == 'adam_bashforth_by_runge_kutta':
					y1 = runge_kutta(y0, t0, h, funcao)
					y2 = runge_kutta(y1, t0+h, h, funcao)
					y3 = runge_kutta(y2, t0+2*h, h, funcao)
					y4 = runge_kutta(y3, t0+3*h, h, funcao)
					y5 = runge_kutta(y4, t0+4*h, h, funcao)
					y6 = runge_kutta(y5, t0+5*h, h, funcao)
					y7 = runge_kutta(y6, t0+6*h, h, funcao)

			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))
			saida.write('1 %s\n' % str(y1))
			saida.write('2 %s\n' % str(y2))
			saida.write('3 %s\n' % str(y3))
			saida.write('4 %s\n' % str(y4))
			saida.write('5 %s\n' % str(y5))
			saida.write('6 %s\n' % str(y6))
			saida.write('7 %s\n' % str(y7))

			abt.append(t0)
			aby.append(y0)
			abt.append(t0+h)
			aby.append(y1)
			abt.append(t0+2*h)
			aby.append(y2)
			abt.append(t0+3*h)
			aby.append(y3)
			abt.append(t0+4*h)
			aby.append(y4)
			abt.append(t0+5*h)
			aby.append(y5)
			abt.append(t0+6*h)
			aby.append(y6)
			abt.append(t0+7*h)
			aby.append(y7)

			yn = y0
			yn1= y1
			yn2 = y2
			yn3 = y3
			yn4 = y4
			yn5 = y5
			yn6 = y6
			yn7 = y7
			tn = t0
			for i in range(8, passos+1):
				yn8 = adam_bashforth8(yn, yn1, yn2, yn3, yn4, yn5, yn6, yn7, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn8)))
				abt.append(tn+8*h)
				aby.append(yn8)
				yn = yn1
				yn1 = yn2
				yn2 = yn3
				yn3 = yn4
				yn4 = yn5
				yn5 = yn6
				yn6 = yn7
				yn7 = yn8
				tn = tn + h
			saida.write('\n')

	if str(vetor[0]) == 'adam_multon' or str(vetor[0]) == 'adam_multon_by_euler' or str(vetor[0]) == 'adam_multon_by_euler_inverso' or str(vetor[0]) == 'adam_multon_by_euler_aprimorado' or str(vetor[0]) == 'adam_multon_by_runge_kutta':
		

		if str(vetor[0]) == 'adam_multon_by_euler':
			saida.write('Metodo de Adam-Moulton por Euler\n')
			recebePontos = 0
		elif str(vetor[0]) == 'adam_multon_by_euler_inverso':
			saida.write('Metodo de Adam-Moulton por Euler Inverso\n')
			recebePontos = 0
		elif str(vetor[0]) == 'adam_multon_by_euler_aprimorado':
			saida.write('Metodo de Adam-Moulton por Euler Aprimorado\n')
			recebePontos = 0
		elif str(vetor[0]) == 'adam_multon_by_runge_kutta':
			saida.write('Metodo de Adam-Moulton por Runge-Kutta\n')
			recebePontos = 0
		elif str(vetor[0]) == 'adam_multon':
			saida.write('Metodo de Adam-Moulton\n')
			recebePontos = 1
		
		ordem = int(vetor[len(vetor) - 1])

		amt = []
		amy = []

		if ordem == 2:
			y0 = Decimal(vetor[1])
			t0 = Decimal(vetor[2])
			h = Decimal(vetor[3])
			passos = int(vetor[4])
			funcao = vetor[5]

			saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))

			if str(vetor[0]) == 'adam_multon_by_euler' or str(vetor[0]) == 'adam_multon':
				y1 = euler(y0, t0, h, funcao)
			elif str(vetor[0]) == 'adam_multon_by_euler_inverso':
				y1 = euler_inverso(y0, t0, h, funcao)
			elif str(vetor[0]) == 'adam_multon_by_euler_aprimorado':
				y1 = euler_aprimorado(y0, t0, h, funcao)
			elif str(vetor[0]) == 'adam_multon_by_runge_kutta':
				y1 = runge_kutta(y0, t0, h, funcao)

			amt.append(t0)
			amy.append(y0)

			yn = y0
			yn1 = y1
			tn = t0
			for i in range(1, passos+1):
				yn1 = adam_moulton2(yn, yn1, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn1)))
				yn2 = adam_bashforth2(yn, yn1, tn, h, funcao)
				amt.append(tn+h)
				amy.append(yn1)
				yn = yn1
				yn1 = yn2
				tn = tn + h
			saida.write('\n')

		if ordem == 3:
			y0 = Decimal(vetor[1])
			if recebePontos == 1:
				y1 = Decimal(vetor[2])
				t0 = Decimal(vetor[3])
				h = Decimal(vetor[4])
				passos = int(vetor[5])
				funcao = str(vetor[6])

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('y(%s) = %s\n' % (str(t0+h), str(y1)))

			elif recebePontos == 0:
				t0 = Decimal(vetor[2])
				h = Decimal(vetor[3])
				passos = int(vetor[4])
				funcao = vetor[5]

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('h = %s\n' % str(h))
				saida.write('0 %s\n' % str(y0))

				if str(vetor[0]) == 'adam_multon_by_euler':
					y1 = euler(y0, t0, h, funcao)
				elif str(vetor[0]) == 'adam_multon_by_euler_inverso':
					y1 = euler_inverso(y0, t0, h, funcao)
				elif str(vetor[0]) == 'adam_multon_by_euler_aprimorado':
					y1 = euler_aprimorado(y0, t0, h, funcao)
				elif str(vetor[0]) == 'adam_multon_by_runge_kutta':
					y1 = runge_kutta(y0, t0, h, funcao)	


			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))
			saida.write('1 %s\n' % str(y1))

			amt.append(t0)
			amy.append(y0)
			amt.append(t0+h)
			amy.append(y1)

			y2 = adam_bashforth2(y0, y1, t0, h, funcao)

			yn = y0
			yn1 = y1
			yn2 = y2
			tn = t0
			for i in range(2, passos+1):
				yn2 = adam_moulton3(yn, yn1, yn2, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn2)))
				yn3 = adam_bashforth3(yn, yn1, yn2, tn, h, funcao)
				amt.append(tn+2*h)
				amy.append(yn2)
				yn = yn1
				yn1 = yn2
				yn2 = yn3
				tn = tn + h
			saida.write('\n')

		if ordem == 4:
			y0 = Decimal(vetor[1])
			if recebePontos == 1:
				y1 = Decimal(vetor[2])
				y2 = Decimal(vetor[3])
				t0 = Decimal(vetor[4])
				h = Decimal(vetor[5])
				passos = int(vetor[6])
				funcao = str(vetor[7])

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('y(%s) = %s\n' % (str(t0+h), str(y1)))
				saida.write('y(%s) = %s\n' % (str(t0+2*h), str(y2)))

			elif recebePontos == 0:
				t0 = Decimal(vetor[2])
				h = Decimal(vetor[3])
				passos = int(vetor[4])
				funcao = vetor[5]

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))

				if str(vetor[0]) == 'adam_multon_by_euler':
					y1 = euler(y0, t0, h, funcao)
					y2 = euler(y1, t0+h, h, funcao)
				elif str(vetor[0]) == 'adam_multon_by_euler_inverso':
					y1 = euler_inverso(y0, t0, h, funcao)
					y2 = euler_inverso(y1, t0+h, h, funcao)
				elif str(vetor[0]) == 'adam_multon_by_euler_aprimorado':
					y1 = euler_aprimorado(y0, t0, h, funcao)
					y2 = euler_aprimorado(y1, t0+h, h, funcao)
				elif str(vetor[0]) == 'adam_multon_by_runge_kutta':
					y1 = runge_kutta(y0, t0, h, funcao)
					y2 = runge_kutta(y1, t0+h, h, funcao)

			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))
			saida.write('1 %s\n' % str(y1))
			saida.write('2 %s\n' % str(y2))

			amt.append(t0)
			amy.append(y0)
			amt.append(t0+h)
			amy.append(y1)
			amt.append(t0+2*h)
			amy.append(y2)

			y3 = adam_bashforth3(y0, y1, y2, t0, h, funcao)

			yn = y0
			yn1 = y1
			yn2 = y2
			yn3 = y3
			tn = t0
			for i in range(3, passos+1):
				yn3 = adam_moulton4(yn, yn1, yn2, yn3, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn3)))
				yn4 = adam_bashforth4(yn, yn1, yn2, yn3, tn, h, funcao)
				amt.append(tn+3*h)
				amy.append(yn3)
				yn = yn1
				yn1 = yn2
				yn2 = yn3
				yn3 = yn4
				tn = tn + h
			saida.write('\n')

		if ordem == 5:
			y0 = Decimal(vetor[1])
			if recebePontos == 1:
				y1 = Decimal(vetor[2])
				y2 = Decimal(vetor[3])
				y3 = Decimal(vetor[4])
				t0 = Decimal(vetor[5])
				h = Decimal(vetor[6])
				passos = int(vetor[7])
				funcao = str(vetor[8])

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('y(%s) = %s\n' % (str(t0+h), str(y1)))
				saida.write('y(%s) = %s\n' % (str(t0+2*h), str(y2)))
				saida.write('y(%s) = %s\n' % (str(t0+3*h), str(y3)))

			elif recebePontos == 0:
				t0 = Decimal(vetor[2])
				h = Decimal(vetor[3])
				passos = int(vetor[4])
				funcao = vetor[5]

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))

				if str(vetor[0]) == 'adam_multon_by_euler':
					y1 = euler(y0, t0, h, funcao)
					y2 = euler(y1, t0+h, h, funcao)
					y3 = euler(y2, t0+2*h, h, funcao)
				elif str(vetor[0]) == 'adam_multon_by_euler_inverso':
					y1 = euler_inverso(y0, t0, h, funcao)
					y2 = euler_inverso(y1, t0+h, h, funcao)
					y3 = euler_inverso(y2, t0+2*h, h, funcao)
				elif str(vetor[0]) == 'adam_multon_by_euler_aprimorado':
					y1 = euler_aprimorado(y0, t0, h, funcao)
					y2 = euler_aprimorado(y1, t0+h, h, funcao)
					y3 = euler_aprimorado(y2, t0+2*h, h, funcao)
				elif str(vetor[0]) == 'adam_multon_by_runge_kutta':
					y1 = runge_kutta(y0, t0, h, funcao)
					y2 = runge_kutta(y1, t0+h, h, funcao)
					y3 = runge_kutta(y2, t0+2*h, h, funcao)
				
			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))
			saida.write('1 %s\n' % str(y1))
			saida.write('2 %s\n' % str(y2))
			saida.write('3 %s\n' % str(y3))

			amt.append(t0)
			amy.append(y0)
			amt.append(t0+h)
			amy.append(y1)
			amt.append(t0+2*h)
			amy.append(y2)
			amt.append(t0+3*h)
			amy.append(y3)

			y4 = adam_bashforth4(y0, y1, y2, y3, t0, h, funcao)

			yn = y0
			yn1 = y1
			yn2 = y2
			yn3 = y3
			yn4 = y4
			tn = t0
			for i in range(4, passos+1):
				yn4 = adam_moulton5(yn, yn1, yn2, yn3, yn4, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn4)))
				yn5 = adam_bashforth5(yn, yn1, yn2, yn3, yn4, tn, h, funcao)
				amt.append(tn+4*h)
				amy.append(yn4)
				yn = yn1
				yn1 = yn2
				yn2 = yn3
				yn3 = yn4
				yn4 = yn5
				tn = tn + h
			saida.write('\n')

		if ordem == 6:
			y0 = Decimal(vetor[1])
			if recebePontos == 1:
				y1 = Decimal(vetor[2])
				y2 = Decimal(vetor[3])
				y3 = Decimal(vetor[4])
				y4 = Decimal((vetor[5]))
				t0 = Decimal(vetor[6])
				h = Decimal(vetor[7])
				passos = int(vetor[8])
				funcao = str(vetor[9])

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('y(%s) = %s\n' % (str(t0+h), str(y1)))
				saida.write('y(%s) = %s\n' % (str(t0+2*h), str(y2)))
				saida.write('y(%s) = %s\n' % (str(t0+3*h), str(y3)))
				saida.write('y(%s) = %s\n' % (str(t0+4*h), str(y4)))

			elif recebePontos == 0:
				t0 = Decimal(vetor[2])
				h = Decimal(vetor[3])
				passos = int(vetor[4])
				funcao = vetor[5]

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				
				if str(vetor[0]) == 'adam_multon_by_euler':
					y1 = euler(y0, t0, h, funcao)
					y2 = euler(y1, t0+h, h, funcao)
					y3 = euler(y2, t0+2*h, h, funcao)
					y4 = euler(y3, t0+3*h, h, funcao)
				elif str(vetor[0]) == 'adam_multon_by_euler_inverso':
					y1 = euler_inverso(y0, t0, h, funcao)
					y2 = euler_inverso(y1, t0+h, h, funcao)
					y3 = euler_inverso(y2, t0+2*h, h, funcao)
					y4 = euler_inverso(y3, t0+3*h, h, funcao)
				elif str(vetor[0]) == 'adam_multon_by_euler_aprimorado':
					y1 = euler_aprimorado(y0, t0, h, funcao)
					y2 = euler_aprimorado(y1, t0+h, h, funcao)
					y3 = euler_aprimorado(y2, t0+2*h, h, funcao)
					y4 = euler_aprimorado(y3, t0+3*h, h, funcao)
				elif str(vetor[0]) == 'adam_multon_by_runge_kutta':
					y1 = runge_kutta(y0, t0, h, funcao)
					y2 = runge_kutta(y1, t0+h, h, funcao)
					y3 = runge_kutta(y2, t0+2*h, h, funcao)
					y4 = runge_kutta(y3, t0+3*h, h, funcao)

			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))
			saida.write('1 %s\n' % str(y1))
			saida.write('2 %s\n' % str(y2))
			saida.write('3 %s\n' % str(y3))
			saida.write('4 %s\n' % str(y4))

			amt.append(t0)
			amy.append(y0)
			amt.append(t0+1*h)
			amy.append(y1)
			amt.append(t0+2*h)
			amy.append(y2)
			amt.append(t0+3*h)
			amy.append(y3)
			amt.append(t0+4*h)
			amy.append(y4)

			y5 = adam_bashforth5(y0, y1, y2, y3, y4, t0, h, funcao)

			yn = y0
			yn1 = y1
			yn2 = y2
			yn3 = y3
			yn4 = y4
			yn5 = y5
			tn = t0
			for i in range(5, passos+1):
				yn5 = adam_moulton6(yn, yn1, yn2, yn3, yn4, yn5, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn5)))
				yn6 = adam_bashforth6(yn, yn1, yn2, yn3, yn4, yn5, tn, h, funcao)
				amt.append(tn+5*h)
				amy.append(yn5)
				yn = yn1
				yn1 = yn2
				yn2 = yn3
				yn3 = yn4
				yn4 = yn5
				yn5 = yn6
				tn = tn + h
			saida.write('\n')

		if ordem == 7:
			y0 = Decimal(vetor[1])
			if recebePontos == 1:
				y1 = Decimal(vetor[2])
				y2 = Decimal(vetor[3])
				y3 = Decimal(vetor[4])
				y4 = Decimal(vetor[5])
				y5 = Decimal(vetor[6])
				t0 = Decimal(vetor[7])
				h = Decimal(vetor[8])
				passos = int(vetor[9])
				funcao = str(vetor[10])

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('y(%s) = %s\n' % (str(t0+h), str(y1)))
				saida.write('y(%s) = %s\n' % (str(t0+2*h), str(y2)))
				saida.write('y(%s) = %s\n' % (str(t0+3*h), str(y3)))
				saida.write('y(%s) = %s\n' % (str(t0+4*h), str(y4)))
				saida.write('y(%s) = %s\n' % (str(t0+5*h), str(y5)))

			elif recebePontos == 0:
				t0 = Decimal(vetor[2])
				h = Decimal(vetor[3])
				passos = int(vetor[4])
				funcao = vetor[5]

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))

				if str(vetor[0]) == 'adam_multon_by_euler':
					y1 = euler(y0, t0, h, funcao)
					y2 = euler(y1, t0+h, h, funcao)
					y3 = euler(y2, t0+2*h, h, funcao)
					y4 = euler(y3, t0+3*h, h, funcao)
					y5 = euler(y4, t0+4*h, h, funcao)
				elif str(vetor[0]) == 'adam_multon_by_euler_inverso':
					y1 = euler_inverso(y0, t0, h, funcao)
					y2 = euler_inverso(y1, t0+h, h, funcao)
					y3 = euler_inverso(y2, t0+2*h, h, funcao)
					y4 = euler_inverso(y3, t0+3*h, h, funcao)
					y5 = euler_inverso(y4, t0+4*h, h, funcao)
				elif str(vetor[0]) == 'adam_multon_by_euler_aprimorado':
					y1 = euler_aprimorado(y0, t0, h, funcao)
					y2 = euler_aprimorado(y1, t0+h, h, funcao)
					y3 = euler_aprimorado(y2, t0+2*h, h, funcao)
					y4 = euler_aprimorado(y3, t0+3*h, h, funcao)
					y5 = euler_aprimorado(y4, t0+4*h, h, funcao)
				elif str(vetor[0]) == 'adam_multon_by_runge_kutta':
					y1 = runge_kutta(y0, t0, h, funcao)
					y2 = runge_kutta(y1, t0+h, h, funcao)
					y3 = runge_kutta(y2, t0+2*h, h, funcao)
					y4 = runge_kutta(y3, t0+3*h, h, funcao)
					y5 = runge_kutta(y4, t0+4*h, h, funcao)

			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))
			saida.write('1 %s\n' % str(y1))
			saida.write('2 %s\n' % str(y2))
			saida.write('3 %s\n' % str(y3))
			saida.write('4 %s\n' % str(y4))
			saida.write('5 %s\n' % str(y5))

			amt.append(t0)
			amy.append(y0)
			amt.append(t0+1*h)
			amy.append(y1)
			amt.append(t0+2*h)
			amy.append(y2)
			amt.append(t0+3*h)
			amy.append(y3)
			amt.append(t0+4*h)
			amy.append(y4)
			amt.append(t0+5*h)
			amy.append(y5)

			y6 = adam_bashforth6(y0, y1, y2, y3, y4, y5, t0, h, funcao)

			yn = y0
			yn1 = y1
			yn2 = y2
			yn3 = y3
			yn4 = y4
			yn5 = y5
			yn6 = y6
			tn = t0
			for i in range(6, passos+1):
				yn6 = adam_moulton7(yn, yn1, yn2, yn3, yn4, yn5, yn6, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn6)))
				yn7 = adam_bashforth7(yn, yn1, yn2, yn3, yn4, yn5, yn6, tn, h, funcao)
				amt.append(tn+6*h)
				amy.append(yn6)
				yn = yn1
				yn1 = yn2
				yn2 = yn3
				yn3 = yn4
				yn4 = yn5
				yn5 = yn6
				yn6 = yn7
				tn = tn + h
			saida.write('\n')

		if ordem == 8:
			y0 = Decimal(vetor[1])
			if recebePontos == 1:
				y1 = Decimal(vetor[2])
				y2 = Decimal(vetor[3])
				y3 = Decimal(vetor[4])
				y4 = Decimal(vetor[5])
				y5 = Decimal(vetor[6])
				y6 = Decimal(vetor[7])
				t0 = Decimal(vetor[8])
				h = Decimal(vetor[9])
				passos = int(vetor[10])
				funcao = str(vetor[11])

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('y(%s) = %s\n' % (str(t0+h), str(y1)))
				saida.write('y(%s) = %s\n' % (str(t0+2*h), str(y2)))
				saida.write('y(%s) = %s\n' % (str(t0+3*h), str(y3)))
				saida.write('y(%s) = %s\n' % (str(t0+4*h), str(y4)))
				saida.write('y(%s) = %s\n' % (str(t0+5*h), str(y5)))
				saida.write('y(%s) = %s\n' % (str(t0+6*h), str(y6)))

			elif recebePontos == 0:
				t0 = Decimal(vetor[2])
				h = Decimal(vetor[3])
				passos = int(vetor[4])
				funcao = vetor[5]

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))

				if str(vetor[0]) == 'adam_multon_by_euler':
					y1 = euler(y0, t0, h, funcao)
					y2 = euler(y1, t0+h, h, funcao)
					y3 = euler(y2, t0+2*h, h, funcao)
					y4 = euler(y3, t0+3*h, h, funcao)
					y5 = euler(y4, t0+4*h, h, funcao)
					y6 = euler(y5, t0+5*h, h, funcao)
				elif str(vetor[0]) == 'adam_multon_by_euler_inverso':
					y1 = euler_inverso(y0, t0, h, funcao)
					y2 = euler_inverso(y1, t0+h, h, funcao)
					y3 = euler_inverso(y2, t0+2*h, h, funcao)
					y4 = euler_inverso(y3, t0+3*h, h, funcao)
					y5 = euler_inverso(y4, t0+4*h, h, funcao)
					y6 = euler_inverso(y5, t0+5*h, h, funcao)
				elif str(vetor[0]) == 'adam_multon_by_euler_aprimorado':
					y1 = euler_aprimorado(y0, t0, h, funcao)
					y2 = euler_aprimorado(y1, t0+h, h, funcao)
					y3 = euler_aprimorado(y2, t0+2*h, h, funcao)
					y4 = euler_aprimorado(y3, t0+3*h, h, funcao)
					y5 = euler_aprimorado(y4, t0+4*h, h, funcao)
					y6 = euler_aprimorado(y5, t0+5*h, h, funcao)
				elif str(vetor[0]) == 'adam_multon_by_runge_kutta':
					y1 = runge_kutta(y0, t0, h, funcao)
					y2 = runge_kutta(y1, t0+h, h, funcao)
					y3 = runge_kutta(y2, t0+2*h, h, funcao)
					y4 = runge_kutta(y3, t0+3*h, h, funcao)
					y5 = runge_kutta(y4, t0+4*h, h, funcao)
					y6 = runge_kutta(y5, t0+5*h, h, funcao)

			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))
			saida.write('1 %s\n' % str(y1))
			saida.write('2 %s\n' % str(y2))
			saida.write('3 %s\n' % str(y3))
			saida.write('4 %s\n' % str(y4))
			saida.write('5 %s\n' % str(y5))
			saida.write('6 %s\n' % str(y6))

			amt.append(t0)
			amy.append(y0)
			amt.append(t0+1*h)
			amy.append(y1)
			amt.append(t0+2*h)
			amy.append(y2)
			amt.append(t0+3*h)
			amy.append(y3)
			amt.append(t0+4*h)
			amy.append(y4)
			amt.append(t0+5*h)
			amy.append(y5)
			amt.append(t0+6*h)
			amy.append(y6)

			y7 = adam_bashforth7(y0, y1, y2, y3, y4, y5, y6, t0, h, funcao)

			yn = y0
			yn1 = y1
			yn2 = y2
			yn3 = y3
			yn4 = y4
			yn5 = y5
			yn6 = y6
			yn7 = y7
			tn = t0
			for i in range(7, passos+1):
				yn7 = adam_moulton8(yn, yn1, yn2, yn3, yn4, yn5, yn6, yn7, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn7)))
				yn8 = adam_bashforth7(yn, yn1, yn2, yn3, yn4, yn5, yn6, yn7, tn, h, funcao)
				amt.append(tn+7*h)
				amy.append(yn7)
				yn = yn1
				yn1 = yn2
				yn2 = yn3
				yn3 = yn4
				yn4 = yn5
				yn5 = yn6
				yn6 = yn7
				yn7 = yn8
				tn = tn + h
			saida.write('\n')

	if str(vetor[0]) == 'formula_inversa' or str(vetor[0]) == 'formula_inversa_by_euler' or str(vetor[0]) == 'formula_inversa_by_euler_inverso' or str(vetor[0]) == 'formula_inversa_by_euler_aprimorado' or str(vetor[0]) == 'formula_inversa_by_runge_kutta' :
		ordem = int(vetor[len(vetor) - 1])
		
		if str(vetor[0]) == 'formula_inversa':
			saida.write('Metodo Formula Inversa de Diferenciacao\n')
			recebePontos = 1
		elif str(vetor[0]) == 'formula_inversa_by_euler':
			saida.write('Metodo Formula Inversa de Diferenciacao por Euler\n')
			recebePontos = 0
		elif str(vetor[0]) == 'formula_inversa_by_euler_inverso':
			saida.write('Metodo Formula Inversa de Diferenciacao por Euler Inverso\n')
			recebePontos = 0
		elif str(vetor[0]) == 'formula_inversa_by_euler_aprimorado':
			saida.write('Metodo Formula Inversa de Diferenciacao por Euler Aprimorado\n')
			recebePontos = 0
		elif str(vetor[0]) == 'formula_inversa_by_runge_kutta':
			saida.write('Metodo Formula Inversa de Diferenciacao por Runge-Kutta\n')
			recebePontos = 0

		fit = []
		fiy = []
		
		if ordem == 2:
			y0 = Decimal(vetor[1])
			if recebePontos == 0:
				t0 = Decimal(vetor[2])
				h = Decimal(vetor[3])
				passos = int(vetor[4])
				funcao = vetor[5]

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				
				if str(vetor[0]) == 'formula_inversa_by_euler':
					y1 = euler(y0, t0, h, funcao)
				elif str(vetor[0]) == 'formula_inversa_by_euler_inverso':
					y1 = euler_inverso(y0, t0, h, funcao)
				elif str(vetor[0]) == 'formula_inversa_by_euler_aprimorado':
					y1 = euler_aprimorado(y0, t0, h, funcao)
				elif str(vetor[0]) == 'formula_inversa_by_runge_kutta':
					y1 = runge_kutta(y0, t0, h, funcao)	

			elif recebePontos == 1:
				y1 = Decimal(vetor[2])
				t0 = Decimal(vetor[3])
				h = Decimal(vetor[4])
				passos = int(vetor[5])
				funcao = str(vetor[6])
				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('y(%s) = %s\n' % (str(t0+h), str(y1)))

			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))
			saida.write('1 %s\n' % str(y1))


			fit.append(t0)
			fiy.append(y0)
			fit.append(t0+h)
			fiy.append(y1)

			yn = y0
			yn1 = y1
			yn2 = adam_bashforth2(yn, yn1, t0, h, funcao)
			tn = t0
			for i in range(2, passos+1):
				yn2 = inversa2(yn, yn1, yn2, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn2)))
				yn3 = adam_bashforth3(yn, yn1, yn2, tn, h, funcao)
				fit.append(tn+2*h)
				fiy.append(yn2)
				yn = yn1
				yn1 = yn2
				yn2 = yn3
				tn = tn + h
			saida.write('\n')

		if ordem == 3:
			y0 = Decimal(vetor[1])
			if recebePontos == 0:
				t0 = Decimal(vetor[2])
				h = Decimal(vetor[3])
				passos = int(vetor[4])
				funcao = vetor[5]

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))

				if str(vetor[0]) == 'formula_inversa_by_euler':
					y1 = euler(y0, t0, h, funcao)
					y2 = euler(y1, t0+h, h, funcao)
				elif str(vetor[0]) == 'formula_inversa_by_euler_inverso':
					y1 = euler_inverso(y0, t0, h, funcao)
					y2 = euler_inverso(y1, t0+h, h, funcao)
				elif str(vetor[0]) == 'formula_inversa_by_euler_aprimorado':
					y1 = euler_aprimorado(y0, t0, h, funcao)
					y2 = euler_aprimorado(y1, t0+h, h, funcao)
				elif str(vetor[0]) == 'formula_inversa_by_runge_kutta':
					y1 = runge_kutta(y0, t0, h, funcao)
					y2 = runge_kutta(y1, t0+h, h, funcao)
			elif recebePontos == 1:
				y1 = Decimal(vetor[2])
				y2 = Decimal(vetor[3])
				t0 = Decimal(vetor[4])
				h = Decimal(vetor[5])
				passos = int(vetor[6])
				funcao = str(vetor[7])
				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('y(%s) = %s\n' % (str(t0+h), str(y1)))				
				saida.write('y(%s) = %s\n' % (str(t0+2*h), str(y2)))

			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))
			saida.write('1 %s\n' % str(y1))
			saida.write('2 %s\n' % str(y2))

			fit.append(t0)
			fiy.append(y0)
			fit.append(t0+h)
			fiy.append(y1)
			fit.append(t0+2*h)
			fiy.append(y2)

			yn = y0
			yn1 = y1
			yn2 = y2
			yn3 = adam_bashforth3(yn, yn1, yn2, t0, h, funcao)
			tn = t0
			for i in range(3, passos+1):
				yn3 = inversa3(yn, yn1, yn2, yn3, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn3)))
				yn4 = adam_bashforth4(yn, yn1, yn2, yn3, tn, h, funcao)
				fit.append(tn+3*h)
				fiy.append(yn3)
				yn = yn1
				yn1 = yn2
				yn2 = yn3
				yn3 = yn4
				tn = tn + h
			saida.write('\n')

		if ordem == 4:
			y0 = Decimal(vetor[1])
			if recebePontos == 0:
				t0 = Decimal(vetor[2])
				h = Decimal(vetor[3])
				passos = int(vetor[4])
				funcao = vetor[5]

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))

				if str(vetor[0]) == 'formula_inversa_by_euler':
					y1 = euler(y0, t0, h, funcao)
					y2 = euler(y1, t0+h, h, funcao)
					y3 = euler(y2, t0+2*h, h, funcao)
				elif str(vetor[0]) == 'formula_inversa_by_euler_inverso':
					y1 = euler_inverso(y0, t0, h, funcao)
					y2 = euler_inverso(y1, t0+h, h, funcao)
					y3 = euler_inverso(y2, t0+2*h, h, funcao)
				elif str(vetor[0]) == 'formula_inversa_by_euler_aprimorado':
					y1 = euler_aprimorado(y0, t0, h, funcao)
					y2 = euler_aprimorado(y1, t0+h, h, funcao)
					y3 = euler_aprimorado(y2, t0+2*h, h, funcao)
				elif str(vetor[0]) == 'formula_inversa_by_runge_kutta':
					y1 = runge_kutta(y0, t0, h, funcao)
					y2 = runge_kutta(y1, t0+h, h, funcao)
					y3 = runge_kutta(y2, t0+2*h, h, funcao)

			elif recebePontos == 1:
				y1 = Decimal(vetor[2])
				y2 = Decimal(vetor[3])
				y3 = Decimal(vetor[4])
				t0 = Decimal(vetor[5])
				h = Decimal(vetor[6])
				passos = int(vetor[7])
				funcao = str(vetor[8])
				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('y(%s) = %s\n' % (str(t0+h), str(y1)))				
				saida.write('y(%s) = %s\n' % (str(t0+2*h), str(y2)))				
				saida.write('y(%s) = %s\n' % (str(t0+3*h), str(y3)))

			
			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))
			saida.write('1 %s\n' % str(y1))
			saida.write('2 %s\n' % str(y2))
			saida.write('3 %s\n' % str(y3))

			fit.append(t0)
			fiy.append(y0)
			fit.append(t0+h)
			fiy.append(y1)
			fit.append(t0+2*h)
			fiy.append(y2)
			fit.append(t0+3*h)
			fiy.append(y3)

			yn = y0
			yn1 = y1
			yn2 = y2
			yn3 = y3
			yn4 = adam_bashforth4(yn, yn1, yn2, yn3, t0, h, funcao)
			tn = t0
			for i in range(4, passos+1):
				yn4 = inversa4(yn, yn1, yn2, yn3, yn4, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn4)))
				yn5 = adam_bashforth5(yn, yn1, yn2, yn3, yn4, tn, h, funcao)
				fit.append(tn+4*h)
				fiy.append(yn4)
				yn = yn1
				yn1 = yn2
				yn2 = yn3
				yn3 = yn4
				yn4 = yn5
				tn = tn + h
			saida.write('\n')

		if ordem == 5:
			y0 = Decimal(vetor[1])
			if recebePontos == 0:
				t0 = Decimal(vetor[2])
				h = Decimal(vetor[3])
				passos = int(vetor[4])
				funcao = vetor[5]

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))

				if str(vetor[0]) == 'formula_inversa_by_euler':
					y1 = euler(y0, t0, h, funcao)
					y2 = euler(y1, t0+h, h, funcao)
					y3 = euler(y2, t0+2*h, h, funcao)
					y4 = euler(y3, t0+3*h, h, funcao)
				elif str(vetor[0]) == 'formula_inversa_by_euler_inverso':
					y1 = euler_inverso(y0, t0, h, funcao)
					y2 = euler_inverso(y1, t0+h, h, funcao)
					y3 = euler_inverso(y2, t0+2*h, h, funcao)
					y4 = euler_inverso(y3, t0+3*h, h, funcao)
				elif str(vetor[0]) == 'formula_inversa_by_euler_aprimorado':
					y1 = euler_aprimorado(y0, t0, h, funcao)
					y2 = euler_aprimorado(y1, t0+h, h, funcao)
					y3 = euler_aprimorado(y2, t0+2*h, h, funcao)
					y4 = euler_aprimorado(y3, t0+3*h, h, funcao)
				elif str(vetor[0]) == 'formula_inversa_by_runge_kutta':
					y1 = runge_kutta(y0, t0, h, funcao)
					y2 = runge_kutta(y1, t0+h, h, funcao)
					y3 = runge_kutta(y2, t0+2*h, h, funcao)
					y4 = runge_kutta(y3, t0+3*h, h, funcao)

			elif recebePontos == 1:
				y1 = Decimal(vetor[2])
				y2 = Decimal(vetor[3])
				y3 = Decimal(vetor[4])
				y4 = Decimal(vetor[5])
				t0 = Decimal(vetor[6])
				h = Decimal(vetor[7])
				passos = int(vetor[8])
				funcao = str(vetor[9])
				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('y(%s) = %s\n' % (str(t0+h), str(y1)))				
				saida.write('y(%s) = %s\n' % (str(t0+2*h), str(y2)))				
				saida.write('y(%s) = %s\n' % (str(t0+3*h), str(y3)))				
				saida.write('y(%s) = %s\n' % (str(t0+4*h), str(y4)))
			
			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))
			saida.write('1 %s\n' % str(y1))
			saida.write('2 %s\n' % str(y2))
			saida.write('3 %s\n' % str(y3))
			saida.write('4 %s\n' % str(y4))

			fit.append(t0)
			fiy.append(y0)
			fit.append(t0+h)
			fiy.append(y1)
			fit.append(t0+2*h)
			fiy.append(y2)
			fit.append(t0+3*h)
			fiy.append(y3)
			fit.append(t0+4*h)
			fiy.append(y4)

			yn = y0
			yn1 = y1
			yn2 = y2
			yn3 = y3
			yn4 = y4
			yn5 = adam_bashforth5(yn, yn1, yn2, yn3, yn4, t0, h, funcao)
			tn = t0
			for i in range(5, passos+1):
				yn5 = inversa5(yn, yn1, yn2, yn3, yn4, yn5, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn5)))
				yn6 = adam_bashforth6(yn, yn1, yn2, yn3, yn4, yn5, tn, h, funcao)
				fit.append(tn+5*h)
				fiy.append(yn5)
				yn = yn1
				yn1 = yn2
				yn2 = yn3
				yn3 = yn4
				yn4 = yn5
				yn5 = yn6
				tn = tn + h
			saida.write('\n')

		if ordem == 6:
			y0 = Decimal(vetor[1])
			if recebePontos == 0:
				t0 = Decimal(vetor[2])
				h = Decimal(vetor[3])
				passos = int(vetor[4])
				funcao = vetor[5]

				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))

				if str(vetor[0]) == 'formula_inversa_by_euler':
					y1 = euler(y0, t0, h, funcao)
					y2 = euler(y1, t0+h, h, funcao)
					y3 = euler(y2, t0+2*h, h, funcao)
					y4 = euler(y3, t0+3*h, h, funcao)
					y5 = euler(y4, t0+4*h, h, funcao)
				elif str(vetor[0]) == 'formula_inversa_by_euler_inverso':
					y1 = euler_inverso(y0, t0, h, funcao)
					y2 = euler_inverso(y1, t0+h, h, funcao)
					y3 = euler_inverso(y2, t0+2*h, h, funcao)
					y4 = euler_inverso(y3, t0+3*h, h, funcao)
					y5 = euler_inverso(y4, t0+4*h, h, funcao)
				elif str(vetor[0]) == 'formula_inversa_by_euler_aprimorado':
					y1 = euler_aprimorado(y0, t0, h, funcao)
					y2 = euler_aprimorado(y1, t0+h, h, funcao)
					y3 = euler_aprimorado(y2, t0+2*h, h, funcao)
					y4 = euler_aprimorado(y3, t0+3*h, h, funcao)
					y5 = euler_aprimorado(y4, t0+4*h, h, funcao)
				elif str(vetor[0]) == 'formula_inversa_by_runge_kutta':
					y1 = runge_kutta(y0, t0, h, funcao)
					y2 = runge_kutta(y1, t0+h, h, funcao)
					y3 = runge_kutta(y2, t0+2*h, h, funcao)
					y4 = runge_kutta(y3, t0+3*h, h, funcao)
					y5 = runge_kutta(y4, t0+4*h, h, funcao)

			elif recebePontos == 1:
				y1 = Decimal(vetor[2])
				y2 = Decimal(vetor[3])
				y3 = Decimal(vetor[4])
				y4 = Decimal(vetor[5])
				y5 = Decimal(vetor[6])
				t0 = Decimal(vetor[7])
				h = Decimal(vetor[8])
				passos = int(vetor[9])
				funcao = str(vetor[10])
				saida.write('y(%s) = %s\n' % (str(t0), str(y0)))
				saida.write('y(%s) = %s\n' % (str(t0+h), str(y1)))				
				saida.write('y(%s) = %s\n' % (str(t0+2*h), str(y2)))				
				saida.write('y(%s) = %s\n' % (str(t0+3*h), str(y3)))				
				saida.write('y(%s) = %s\n' % (str(t0+4*h), str(y4)))
				saida.write('y(%s) = %s\n' % (str(t0+5*h), str(y5)))

			
			saida.write('h = %s\n' % str(h))
			saida.write('0 %s\n' % str(y0))
			saida.write('1 %s\n' % str(y1))
			saida.write('2 %s\n' % str(y2))
			saida.write('3 %s\n' % str(y3))
			saida.write('4 %s\n' % str(y4))
			saida.write('5 %s\n' % str(y5))

			fit.append(t0)
			fiy.append(y0)
			fit.append(t0+h)
			fiy.append(y1)
			fit.append(t0+2*h)
			fiy.append(y2)
			fit.append(t0+3*h)
			fiy.append(y3)
			fit.append(t0+4*h)
			fiy.append(y4)
			fit.append(t0+5*h)
			fiy.append(y5)

			yn = y0
			yn1 = y1
			yn2 = y2
			yn3 = y3
			yn4 = y4
			yn5 = y5
			yn6 = adam_bashforth6(yn, yn1, yn2, yn3, yn4, yn5, t0, h, funcao)
			tn = t0
			for i in range(6, passos+1):
				yn6 = inversa6(yn, yn1, yn2, yn3, yn4, yn5, yn6, tn, h, funcao)
				saida.write('%d %s\n' % (i, str(yn6)))
				yn7 = adam_bashforth7(yn, yn1, yn2, yn3, yn4, yn5, yn6, tn, h, funcao)
				fit.append(tn+6*h)
				fiy.append(yn6)
				yn = yn1
				yn1 = yn2
				yn2 = yn3
				yn3 = yn4
				yn4 = yn5
				yn5 = yn6
				yn6 = yn7
				tn = tn + h
			saida.write('\n')

plt.figure(1)
plt.subplot(2,2,1)
plt.plot(eulert, eulery, 'm')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Euler')

plt.subplot(2,2,2)
plt.plot(eulerit, euleriy, 'y')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Euler Inverso')

plt.subplot(2,2,3)
plt.plot(eulerat, euleray, 'g')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Euler Aprimorado')

plt.subplot(2,2,4)
plt.plot(runget, rungey, 'r')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Runge-Kutta')

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.4, wspace=0.35)

plt.figure(2)
plt.subplot(2,2,1)
plt.plot(abt, aby, 'y')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Adams-Bashforth')

plt.subplot(2,2,2)
plt.plot(amt, amy, 'r')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Adam-Moulton')

plt.subplot(2,2,3)
plt.plot(fit, fiy, 'm')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Inversa')

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.4, wspace=0.35)

plt.figure(3)
plt.plot(fit, fiy, 'r', amt, amy, 'g', abt, aby, 'b', runget, rungey, 'y', eulerat, euleray, 'k', eulerit, euleriy, 'm', eulert, eulery, 'c')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Todos os metodos')

red_patch = mpatches.Patch(color='red', label='Formula Inversa')
green_patch = mpatches.Patch(color='green', label='Adam-Moulton')
blue_patch = mpatches.Patch(color='blue', label='Adams-Bashforth')
yellow_patch = mpatches.Patch(color='yellow', label='Runge-Kutta')
black_patch = mpatches.Patch(color='black', label='Euler Aprimorado')
rosa_patch = mpatches.Patch(color='magenta', label='Euler Inverso')
laranja_patch = mpatches.Patch(color = 'cyan', label = 'Euler')
plt.legend(handles=[red_patch, green_patch, blue_patch, yellow_patch, black_patch, rosa_patch,laranja_patch])

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.4, wspace=0.35)

plt.show()
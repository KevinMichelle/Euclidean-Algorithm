import sys

def gcd(a, b):
	auxiliar = (a, b)
	a = max(auxiliar)
	b = min(auxiliar)
	while a % b != 0:
		c = a % b
		a = b
		b = c
	resultado = b
	return resultado

if len(sys.argv) != 3:
	print 'El numero de argumentos es invalido'
else:
	if sys.argv[1].isdigit() and sys.argv[2].isdigit():
		if sys.argv[1] > 1 and sys.argv[2] > 1:
			a = int(sys.argv[1])
			b = int(sys.argv[2])
			resultado = gcd(a, b)
			print resultado
	else:
		print 'Todos los argumentos deben ser numeros'

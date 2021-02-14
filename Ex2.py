def primomayor(num):
	c = int()
	primo = False
	for i in range(1,num+1):
		if (num%i==0):
			c = c+1
	if (c==2):
		primo = True
	return primo

if __name__ == '__main__':
	p = int()
	r = int()
	ma = int()
	m = int()
	r = 0
	m = [[int() for ind0 in range(4)] for ind1 in range(3)]
	print("Diguite los numeros de la matriz")
	for i in range(3):
		for j in range(4):
			print("Ingresar el elemento de la posicion [",i,"][",j,"]")
			m[i][j] = int(input())
	for i in range(3):
		for j in range(4):
			print(m[i][j]," ", end="")
		print("")
	for i in range(3):
		for j in range(4):
			if primomayor(m[i][j]):
				ma = m[i][j]
				ac = m[i][j]
				if (primomayor(ac)):
					if (ac>ma):
						ma = ac
				p = ma
	for i in range(3):
		for j in range(4):
			if (p==m[i][j]):
				r = r+1
	print("El mayor numero primo es ",p," y se repite ",r," veces en la matriz")


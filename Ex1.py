if __name__ == '__main__':
	c = int()
	num1 = int()
	num2 = int()
	num3 = int()
	m = int()
	m = [[int() for ind0 in range(6)] for ind1 in range(4)]
	print("Digite los numeros de la matriz")
	for i in range(4):
		for j in range(6):
			print("Matriz[",i,"][",j,"]")
			m[i][j] = int(input())
			num1 = 0
			num2 = 1
			while (num2+num1<=100):
				num3 = num1
				num1 = num2
				num2 = num3+num1
				if (m[i][j]==num2):
					c = c+1
	for i in range(4):
		for j in range(6):
			print(m[i][j], end="\t")
		print("")
	print("Los números que coincidieron con la secuencia fibonacci fueron: ",c)


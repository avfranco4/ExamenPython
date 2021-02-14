if __name__ == '__main__':
	n = int()
	nr = int()
	col = int()
	fil = int()
	m = int()
	nr = 0
	col = 0
	fil = 0
	print("Digite el limite de la matriz")
	n = int(input())
	m = [[int() for ind0 in range(n)] for ind1 in range(n)]
	for i in range(n):
		for j in range(n):
			print("Matriz [",i,"][",j,"]: ")
			m[i][j] = int(input())
	for i in range(n):
		for j in range(n):
			print(m[i][j]," ", end="")
		print("")
	print("Los numeros que no se repiten son: ", end="")
	while (fil<n and col<n):
		for i in range(n):
			for j in range(n):
				if (m[fil][col]==m[i][j]):
					nr = nr+1
		if (nr==1):
			print(m[fil][col]," ", end="")
		if (fil<n and col==n-1):
			fil = fil+1
		if (col<n-1):
			col = col+1
		else:
			col = 0
		nr = 0
	print("")


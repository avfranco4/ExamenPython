if __name__ == '__main__':
	n = int()
	num = int()
	a = int()
	c = int()
	num = 2
	c = 0
	print("Digite el limite del vector")
	n = int(input())
	print("Digite los elementos del vector")
	a = [int() for ind0 in range(n)]
	for i in range(n):
		print("Digite los elementos de la matriz A [",i,"]")
		a[i] = int(input())
	for i in range(n):
		print(a[i]," ", end="")
	for i in range(n):
		if (a[i]==num):
			c = c+1
	print("")
	print("El numero ",num," se ha encontrado ",c," veces en el vector")


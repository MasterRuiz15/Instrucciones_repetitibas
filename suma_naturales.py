## Programa que sume los 10 primeros numeros naturales

# input
n = int(input("Digite el valor de n: "))

# Processing
suma = 0
i = 1

while (i<=n):
    suma = suma + i
    i = i + 1

# output
print("La suma es: "+ str(suma))
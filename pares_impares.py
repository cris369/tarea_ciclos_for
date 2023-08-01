num = 0
par = 0
impar = 0


for i in range(1,11): 
    num = float(input(f"Ingrese numero: "))
    if num != 0:
       if num % 2 == 0:
        par += 1
       else:
        impar += 1
        
print(f"Hay {par} numeros pares")
print(f"Hay {impar} numeros impares")



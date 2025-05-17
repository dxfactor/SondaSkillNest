# 1 Básico
for i in range(0,101):
   print(i)
   
# 2 Múltiples de 2
for i in range(2, 500, 2):
   print(i)
   
# 3 Contando Vanilla Ice
for i in range(1, 101):
    if i % 5 == 0:
        print("ice ice")
    elif i % 10 == 0:
        print("baby")
    else:
        print(i)

# 4 Wow. Número gigante a la vista
pares = 0        
for i in range(0, 500000001, 2):
    if i % 2 == 0:
        pares += i
print(pares)

# 5 Regrésame al 3
for i in range(2024, 0, -3):
   print(i)

# 6 Contador dinámico
numInicial = 3
numFinal = 10
multiplo = 2

for numero in range(numInicial, numFinal + 1):
    if numero % multiplo == 0:
        print(numero)
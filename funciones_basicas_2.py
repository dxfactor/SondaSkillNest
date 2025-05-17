# 1 Multiplica por 2
def multiplica_por_dos(num):
    lista = []
    for i in range(num + 1):
         lista.append(i * 2)
    return lista
print(multiplica_por_dos(5))

# 2 Suma y resta
def suma_y_resta(num_list):
    print (num_list[0] + num_list[1])
    return num_list[0] - num_list[1]
print(suma_y_resta([5, 4]))

# 3 Sumatoria menos longitud
def sumatoria_menos_longitud(num_list):
    suma = 0
    for i in num_list:
        suma += i
    return suma - len(num_list)
 
print(sumatoria_menos_longitud([1, 2, 3, 4]))

# 4 Valoreds multiplicados por el segundo
def valores_multiplicados_segundo(num_list):
   if len(num_list) < 2:
      return []
   else:
      lista = []
      for i in num_list:
         lista.append(i * num_list[1])      
         print(len(lista))
      return lista
      
print(valores_multiplicados_segundo([1, 3, 5, 7]))
print(valores_multiplicados_segundo([1]))

# 5 Valor multiplicado y longitud
def valor_multiplicado_longitud(valor, longitud):
   Lista = []
   for i in range(longitud):
      Lista.append(valor * longitud)
   return Lista
print(valor_multiplicado_longitud(5,2))
print(valor_multiplicado_longitud(7,5))


   
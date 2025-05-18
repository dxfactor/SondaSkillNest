# 1 Carga de datos
list_ventas = [
    {
        "fecha": "2024-01-01",
        "producto": "Citroen C3",
        "cantidad": 1,
        "precio": 6990000
    },
    {
        "fecha": "2024-01-02",
        "producto": "Citroen C4",
        "cantidad": 1,
        "precio": 6990000
    },
    {
        "fecha": "2024-01-03",
        "producto": "Honda Civic",
        "cantidad": 1,
        "precio": 10990000
    },
    {
        "fecha": "2024-01-04",
        "producto": "Volvo XC40",
        "cantidad": 1,
        "precio": 18990000
    },
    {
        "fecha": "2024-01-05",
        "producto": "Volvo XC40",
        "cantidad": 1,
        "precio": 18990000
    },
    {
        "fecha": "2024-01-06",
        "producto": "Honda Civic",
        "cantidad": 1,
        "precio": 10990000
    }
]

# 2 Calcular el total de ventas   
total_ventas = 0
for venta in list_ventas:
    total_ventas += venta["cantidad"] * venta["precio"]
print(f"Ingresos totales: {total_ventas}")

# 3 Análisis del producto Más Vendido

ventas_por_producto = {}
for venta in list_ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad
print("Ventas por producto:")
for producto, cantidad in ventas_por_producto.items():
    print(f"{producto}: {cantidad} unidades")
    
# 4 Promedio de precio por producto
precios_por_producto = {}
for venta in list_ventas:
    producto = venta["producto"]
    precio = venta["precio"]
    cantidad = venta["cantidad"]
    
    if producto in precios_por_producto:
        suma_precios, total_unidades = precios_por_producto[producto]
        precios_por_producto[producto] = (suma_precios + (precio * cantidad), total_unidades + cantidad)
    else:
        precios_por_producto[producto] = (precio * cantidad, cantidad)
        
precios_promedio = {}
for producto, (suma_precios, total_unidades) in precios_por_producto.items():
    precios_promedio[producto] = suma_precios / total_unidades
    if total_unidades > 0:
        precios_promedio[producto] = suma_precios / total_unidades
    else:
        precios_promedio[producto] = 0
print("Precios promedio por producto:")
for producto, precio_promedio in precios_promedio.items():
    print(f"{producto}: {precio_promedio} por unidad")

# 5 Ventas por día
ingresos_por_dia = {}
for venta in list_ventas:
    fecha = venta["fecha"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += cantidad * precio
    else:
        ingresos_por_dia[fecha] = cantidad * precio
        
print("Ingresos por día:")
for fecha, ingresos_total in ingresos_por_dia.items():
    print(f"{fecha}: {ingresos_total}")

# 6 Representación de Datos

resumen_ventas = {}
for venta in list_ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    
    if producto not in resumen_ventas:
        resumen_ventas[producto] = {
            "cantidad_total": 0,
            "ingresos_totales": 0,
            "precio_promedio": 0
        }
    
    resumen_ventas[producto]["cantidad_total"] += cantidad
    resumen_ventas[producto]["ingresos_totales"] += cantidad * precio
    resumen_ventas[producto]["precio_promedio"] = resumen_ventas[producto]["ingresos_totales"] / resumen_ventas[producto]["cantidad_total"]
print("Resumen de ventas por producto:")
for producto, datos in resumen_ventas.items():
    print(f"{producto}:")
    print(f"  Cantidad total: {datos['cantidad_total']}")
    print(f"  Ingresos totales: {datos['ingresos_totales']}")
    print(f"  Precio promedio: {datos['precio_promedio']}")
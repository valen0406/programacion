#ventas_totales = 0
nombre = input("Digite su nombre:")
ingresos = float(input("Digite los ingresos obtenidos este mes:"))
total = round(ingresos * 0.13)
totall = round(ingresos + total)
redondeo = round(total, 2)

print(f"Estimado {nombre} el monto que le corresponde por las comisiones es: {total} y el valor total es: {totall}")
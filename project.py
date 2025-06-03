#                       MARGEN DE GANANCIAS PARA TU EMPRENDIMIENTO 

#Este pequeño script , personalmente me sirvio para calcular las 
#ganancias mensuales aproximadas que me daba por mes , en un local
#de comidas familiar, es sencillo , ya que teniamos muy poca variedad
#de bebidas y no necesitabamos tantas opciones , con scripts muy basicos.
# -Precio de compra de los packs
# -precio de venta por unidad 
# -Algunos costos fijos (luz , alquiler , etc)
#Brinda cierta recomendacion segun el nivel de ganancias , como si conviene invertir o cubrir gastos.


print("Calculadora de margen de ganancias para tu emprendimiento")
print("Maximiza tus ingresos sin perder de vista los costos")
print("por favor , ingresa los valores enteros , sin puntos")

precio_pack = int(input("cual es el precio del pack que vamos a sacar : "))
cantidad_por_pack = int(input("cuantas cantidades trae el pack : "))
cuanto_vendes = int(input("a cuanto vendes cada unidad?: "))
cuantos_compras = int(input("cuantos pack compras por semana: "))

#algunos costos fijos
luz = int(input("cuanto pagas de luz : "))
alquiler = int(input("cuanto pagas de alquiler : "))
otros_gastos_fijos = int(input("que otros gastos tenes todos los meses : "))


#calculos
bebidas_al_mes = cuantos_compras * 4 * cantidad_por_pack #4 semanas promedio
ingreso_mes = bebidas_al_mes * cuanto_vendes
compra_bebidas = (cuantos_compras * 4) * precio_pack
ganancias_mes = ingreso_mes - compra_bebidas
ganancias_mes_luz = ganancias_mes - luz


print(f"Excelente. Este mes estarias vendiendo aproximadamente {bebidas_al_mes} unidades ")
print("//////////////////////////////////////////////////////////////////")
print(f"Y estas teniendo un ingreso de ${ingreso_mes:,} al mes. ")
print("///////////////////////////////////////////////////////////////////")
print(f"pero si sacamos las bebidas que compras en un mes es de ${compra_bebidas:,}")
print("///////////////////////////////////////////////////////////////////")
print(f"Nos estaria dando una ganancia aproximada de ${ganancias_mes:,} al mes")

print("///////////////////////////////////////////////////////////////////")

if ganancias_mes > 400000:
    print("Bien nosotros te recomendamos que mejor vuelvas a invertir esa plata en tus bebidas")
    print("///////////////////////////////////////////////////////////////////")
elif ganancias_mes > 250000:
    print(f"con ese monto ${ganancias_mes:,} te recomendamos cubrir la luz")
    print("///////////////////////////////////////////////////////////////////")
    print(f"dandote una ganancia de ${ganancias_mes_luz:,} pesos ")
elif ganancias_mes > 180000:
    print("Tene en cuenta que esta ganancia viene exclusivamente de la bebida seleccionada , podria ser recomendable invertir en otro aspecto del negocio")
    print("///////////////////////////////////////////////////////////////////")
else:
    print("No alcanzaste el minimo requerido , por favor complementalo con otro producto")





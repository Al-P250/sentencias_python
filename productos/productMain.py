from productos.Product import Product

carrito=[]
val=True
while val:
    print("1. Añadir productos al carrito")
    print("2. Ver mi carrito")
    print("3. Ver si mis productos están activos")
    print("4. Salir")
    opcion=int(input(">> "))
    try:
        if opcion==1:
            nombre=input("Introduce el nombre del producto: ")
            precio=float(input("Introduce el precio del producto: "))
            carrito.append(Product(nombre,precio))
        elif opcion==2:
            if len(carrito)==0:
                print("No hay productos en el carrito")
            else:
                for producto in carrito:
                    print(producto)

        elif opcion==3:
            if len(carrito)==0:
                print("No hay productos en el carrito")
            else:
                for producto in carrito:
                    print(producto, producto.isActive, sep="\t\t")


        elif opcion==4:
            val=False
        else:
            raise ValueError("Introduzca una opción válida")
    except ValueError as e:
        print(e)


# Clases de reservas de Hotel

"""Vamos a crear un sistema de reservas de Hotel.
Cada reserva va a tener la siguiente estructura:
- code (Código generado aleatoriamente de 16 caracteres)
- nombre (Nombre del huésped)
- tipo_habitacion (doble o individual)
- noches (número entero aleatorio entre 1 y 7)
- tarifa por noche (número aleatorio float entre 30 y 60)
- descuento (numero float asignado aleatoriamente de 1 a 100)

### Validación (Control de errores de tipo ValueError):
1. nombre no puede estar vacio
2. tipo_habitacion (Debe de ser una opció
n de estas: doble o individual).

### Implementación de propiedades:
Descuento -> esta propiedad tiene que aplicar el descuento al precio y retornar el precio final (Con descuento incluido)

### StaticMethod:
Las funciones usadas para validación deben de ser estáticas.

Implementa correctamente el método __str__:
[code] nombre : tipo_habitacion -> [noches] noches x [precio_con_descuento]

Nuestro menú del hotel tiene:
1. Añadir huésped
2. Ver los huéspedes
3. Filtrar los que tengan habitación individual o doble
4. Suma total del dinero pagado por los huéspedes en mi hotel
5. Salir 
"""






































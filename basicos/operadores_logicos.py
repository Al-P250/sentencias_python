color="azul"
otro_color="rojo"
num_1=12
num_2=13
usuario_activo=True
user=None
arr_1=[1,2,3,4]

if num_1< num_2 and color=="azul":# En JAVA se usan && y em Python and
    print(num_1)
if num_2< num_1 or otro_color=="rojo":# En JAVA se usan || y em Python or
    print(num_1)

# En JAVA la negación es el signo ! pero en Python es not
if not usuario_activo:
    print("Usuario no activo")
else:
    print("Usuario activo")

if user is None:
    print("Usuario anónimo")

if user is not None:
    print("Usuario loggeado")

if arr_1 is arr_1:
    print("Es el mismo array")

if 4 in arr_1:
    print("El 4 se encuentra")

if 5 not in arr_1:
    print("El 5 no se encuentra")
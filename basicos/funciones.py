def nombre_fn():
    print("Hola mundo")

def suma_fn(x,y):
    print(x+y)

def resta_fn(x,y):
    return x-y
# args es una tupla de n elementos
def multiplicar_n_fn(*args):
    for i in args:
        print(i)
    print()
def division_fn(**kwargs):
    a=kwargs['a']
    b=kwargs.get('b')
    z=kwargs.get('z',12)
    print(kwargs)
    print(a)
    print(b)
    print(z)

nombre_fn()
suma_fn(1,2)

resta=resta_fn(1,2)
print(resta)


multiplicar_n_fn(1,2,3,50)

division_fn(a=1,b=2,c=34,d=5)
from biblioteca.Book import Book

biblioteca=[]
val=True

while val:
    print("1. Crear libro")
    print("2. Ver mis libros")
    print("3. Salir")
    opt=int(input(">> "))

    try:
        if opt==1:
            print("\n")
            title=input(">> >> Título: ")
            author=input(">> >> Autor: ")
            price=float(input(input(">> >> Precio: ")))
            book=Book(title, author,price)
            biblioteca.append(book)
        elif opt==2:
            for book in biblioteca:
                print(book)
        elif opt==3:
            val=False
        else:
            print("Opción no válida")
    except ValueError as e:
        print("[Error]", e, sep=" => ")
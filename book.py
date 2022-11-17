import json
#Funcion para crear un JSON de book y mostrarlo en consola
def crearLibros():
    books = """
    {
        "book":[
            {"title":"Don quijote",
            "cover":"Dura",
            "year":"1615",
            "pages":"462"
            },
            {"title":"Pinocho",
            "cover":"Blanda",
            "year":"1985",
            "pages":"357"
            },
            {"title":"365 dni",
            "cover":"Blanda",
            "year":"2018",
            "pages":"496"
            },
            {"title":"Cocina fácil y rico",
            "cover":"Dura",
            "year":"2022",
            "pages":"704"
            }
        ]S
    }
    """
    with open("books","w") as libros:
        json.dump(books,libros)
        print("Se ha creado el archivo")

    with open("books", "r") as libros:
         mustra = json.load(libros)
         print(mustra)
# Funcion para mostrar por consola el JSON anterior
def muestraConsola():
    with open("books", "r") as libros:
        mustra = json.load(libros)
        print(mustra)

print(crearLibros())
print("Funcion de mostrar")
print(muestraConsola())
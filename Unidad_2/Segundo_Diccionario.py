import json

biblioteca = {
    "978-84-376-0494-7": {
        "título": "Cien años de soledad",
        "autor": ["Gabriel García Márquez"],
        "géneros": ["Realismo mágico", "Novela histórica"]
    },
    "978-84-204-1625-5": {
        "título": "Don Quijote de la Mancha",
        "autor": ["Miguel de Cervantes Saavedra"],
        "géneros": ["Novela de caballería", "Satira"]
    },
    "978-84-670-5334-6": {
        "título": "La sombra del viento",
        "autor": ["Carlos Ruiz Zafón"],
        "géneros": ["Misterio", "Ficción histórica"]
    },
    "978-84-339-7534-9": {
        "título": "Rayuela",
        "autor": ["Julio Cortázar"],
        "géneros": ["Novela experimental", "Boom latinoamericano"]
    },
    "978-84-9742-132-9": {
        "título": "La ciudad y los perros",
        "autor": ["Mario Vargas Llosa"],
        "géneros": ["Realismo social", "Ficción militar"]
    }
}

isbn = "978-84-376-0494-7"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:", info_libro)

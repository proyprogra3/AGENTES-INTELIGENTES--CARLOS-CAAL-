import random

# Diccionario de películas por género
peliculas = {
    "acción": ["Mad Max: Fury Road", "Die Hard", "John Wick"],
    "comedia": ["The Hangover", "Superbad", "Step Brothers"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"],
    "ciencia ficción": ["Inception", "Interstellar", "The Matrix"],
    "terror": ["The Conjuring", "Get Out", "A Nightmare on Elm Street"]
}

# Solicitar al usuario su género favorito
print("¿Cuál es tu género favorito? (acción, comedia, drama, ciencia ficción, terror)")
genero = input().lower()

# Validar que el género sea válido
if genero in peliculas:
    recomendacion = random.choice(peliculas[genero])
    print(f"Te recomiendo ver: {recomendacion}")
else:
    print("Género no válido. Por favor, elige entre: acción, comedia, drama, ciencia ficción, terror.")

import random
dic = {
    "colores" : ["azul", "rojo", "verde", "violeta", "amarillo", "negro"],
    "deportes" : ["futbol", "handball", "tenis", "ajedrez", "natacion"],
    "paises" : ["Argentina", "Peru", "Bolivia", "Francia", "Alemania", "Bulgaria"]
}

print("¡Bienvenido al Ahorcado!")
print()
print(f"Categorias disponibles: ")
for elem in dic:
    print(elem)

categoria = input("Ingrese con que categoria jugar: ")
while categoria not in dic:
    categoria = input("Categoria invalida ingrese otra: ")
words = random.sample(dic[categoria], len(dic[categoria]))
print()

for word in words:   #vamos a jugar con todas las palabras de la categoria elegida
    guessed = []  
    attempts = 6
    while attempts > 0:
# Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
# Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}") #Concatena elementos en un string con , 
        letter = input("Ingresá una letra: ")
        if len(letter) == 1 and letter.isalpha():
            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                print("Esa letra no está en la palabra.")
            print()
        else:
            print("Entrada no valida")
    else:
        print(f"¡Perdiste! La palabra era: {word}")
    print(f"Puntaje final: {attempts}") #Los intentos podrian servir como puntaje de ronda, ya que arranca en 6 y por cada error resta uno.
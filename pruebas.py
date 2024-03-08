#juego del casino
import random

while  True:
    jugador = random.randint(2, 26)
    dealer = random.randint(2, 26)
    while True:
        print(jugador,dealer)
        quiere_mas_cartas = input("Quiere mas cartas s/n")
        if quiere_mas_cartas == "s":
            jugador = jugador + random.randint(1, 13)
        else:
            if jugador == 21 or (jugador > dealer and jugador < 21):
                print("Ganaste!")
                break
         elif jugador == dealer : 
            print("gano el dealer")
            break
     else:
    print("gano el dealer")
        
            
    

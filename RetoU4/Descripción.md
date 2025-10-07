# Ejercicio a usar para el reto 
De nuestro codigo usaremos el caso 110 , que tiene que ver con velocidad de perdida.
## Listas
Las listas las usaremos para ver las condiciones de la aeronave durante diferemntes intervalos durante el vuelo.
## Diccionarios
Usaremos diccionarios para presentar el registro completo del simulador donde se describe el tipo de aeronave que se uso ya que dependiendo de la aeronave las condicones cambia


``` python
while contr == True:
    print("ingrese la seccion que desea ver")
    print(" 1. que es \n 2. simulacion \n 3. aeronaves \n 0. salir \n")
    opcio = input("Elija una opcion ")
    match opcio:
        case "1":
            print("Que es")
            print("fenómeno aerodinámico donde el ala de un avión pierde sustentación porque el ángulo de ataque excede un límite crítico, haciendo que el flujo de aire sobre el ala se vuelva turbulento. Esto resulta en una pérdida de control y una rápida caída de altura. La recuperación implica disminuir el ángulo de ataque y aumentar la velocidad, generalmente bajando el morro del avión y añadiendo potencia. ")
            break
        case "2":
            print("Simulacion stall")
            print("El programa simulará el vuelo de una aeronave en el cual verificará en cada instante si la aeronave se encentra en condiciones seguras o si está entrando en perdida.")
            conta = 0
            while conta < 10 :
                w = int(input("Ingrese el peso: "))
                s = int(input("Ingrese la superficie alar: "))
                c = int(input("ingrese el coeficiente de sustentacion: "))
                d = int(input("Ingrese la densidad del aire:"))
                v_stall = (2*w)/(d*s*c)
                v_stal = pow(v_stall, 0.5)
                print("calculando procedimiento "),v_stal
                print("Ingrese 0 si desea salir o ingrese el valor de la velocidad para continuar")
                v_actual = int(input("Ingrese el valor de la velocidad: "))

                conta = conta + 1
                if v_actual == 0 :
                    break
                if v_actual > v_stal:
                    print("Seguro, el avion esta por encima de la velocidad de perdida")
                else:
                    print("Precaucion, velocidad de perdida, aumentar velocidad")
        case "3":
            print("Aeronaves disponibles")
            aeronaves = {
                "Boeing 747": {"peso": "183,500 kg", "superficie_alar": "511 m²", "velocidad_crucero": "917 km/h"},
                "Airbus A320": {"peso": "78,000 kg", "superficie_alar": "122.6 m²", "velocidad_crucero": "828 km/h"},
                "Cessna 172": {"peso": "1,157 kg", "superficie_alar": "16.2 m²", "velocidad_crucero": "226 km/h"}
            }
            for aeronave, datos in aeronaves.items():
                print(f"Aeronave: {aeronave}")
                for key, value in datos.items():
                    print(f"  {key}: {value}")
                print()
        case "0":
            print("Regresando")
            break
        case _:
            print("modo no valido")     
```
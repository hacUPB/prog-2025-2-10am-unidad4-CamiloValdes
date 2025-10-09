# Ejercicio a usar para el reto 
De nuestro codigo usaremos el caso 110 , que tiene que ver con velocidad de perdida.
## Listas
Las listas las usaremos para ver (Imprimir en pantalla los resultados )las condiciones de la aeronave durante diferemntes intervalos durante el vuelo. Tambien con base en las listas se realizaran varias operaciones matematicas (estadisticas) usando los datos que conforman dicha lista. 
## Diccionarios

Usaremos un diccionario para dar al usuario opciones de aeronaves con las cuales quiera realizar la similación, cada aeronave tiene sus condiciones diferentes (como por ejemplo superficie alar). Pusimos el diccionario en el incio del codigo para que desde el principio del codigo el usuario tenga la posibilidad de escoger. 

## Tabla de variables del codigo
|Variable|Tipo|Comentario|
|--------|----|----------|
|w|Entrada|Peso total de la aeronave|
|s|Entrada|Area total de las alas del avión|
|c|Entrada|Coeficiente de sustentación segun perfil|
|d|Entrada|Densidad del aire por el que se está desplazando la aeronave|
|v_stal|Salida|Calculo del Stall de la aeronave en ese momento|
|v_actual|Entrada|Velocidad actual de la aeronave|

|Variable         |Tipo    |Comentario                                                                 |
|-----------------|--------|--------------------------------------------------------------------------|
|contr            |Control |Variable booleana para controlar el ciclo principal del programa           |
|aeronaves        |Control |Diccionario con datos de aeronaves disponibles para simulación             |
|opcio            |Entrada |Opción seleccionada en el menú principal                                   |
|seleccion        |Entrada |Número de aeronave seleccionada por el usuario                             |
|nombre_aeronave  |Control |Nombre de la aeronave seleccionada                                         |
|datos_aeronave   |Control |Diccionario con los datos de la aeronave seleccionada                      |
|w                |Entrada |Peso total de la aeronave (puede venir del diccionario o ingresarse manual)|
|s                |Entrada |Área total de las alas del avión (puede venir del diccionario o manual)    |
|c                |Entrada |Coeficiente de sustentación según perfil                                   |
|d                |Entrada |Densidad del aire por el que se está desplazando la aeronave               |
|v_stall          |Salida  |Resultado intermedio para calcular la velocidad de pérdida                  |
|v_stal           |Salida  |Velocidad de pérdida calculada                                             |
|v_actual         |Entrada |Velocidad actual de la aeronave                                            |
|margen_seguridad |Salida  |Diferencia entre velocidad actual y velocidad de pérdida                   |
|resultados       |Salida  |Lista que almacena [v_stal, v_actual, margen_seguridad] de cada iteración  |
|conta            |Control |Contador de iteraciones en la simulación                                   |
|v_stal_list      |Salida  |Lista de velocidades de pérdida para estadísticas                          |
|v_actual_list    |Salida  |Lista de velocidades actuales para estadísticas                            |
|margen_list      |Salida  |Lista de márgenes de seguridad para estadísticas                           |



``` python
contr = True
while contr:
    print("ingrese la seccion que desea ver")
    print(" 1. Qué es \n 2. Simulacion \n 3. Aeronaves \n 0. Salir \n")
    opcio = input("Elija una opcion ")
    match opcio:
        case "1":
            print("Qué es")
            print("fenómeno aerodinámico donde el ala de un avión pierde sustentación porque el ángulo de ataque excede un límite crítico, haciendo que el flujo de aire sobre el ala se vuelva turbulento. Esto resulta en una pérdida de control y una rápida caída de altura. La recuperación implica disminuir el ángulo de ataque y aumentar la velocidad, generalmente bajando el morro del avión y añadiendo potencia. ")
        case "2":
            print("Simulacion stall")
            print("El programa simulará el vuelo de una aeronave en el cual verificará en cada instante si la aeronave se encentra en condiciones seguras o si está entrando en perdida.")
            conta = 0
            while conta < 10:
                w = int(input("Ingrese el peso: "))
                s = int(input("Ingrese la superficie alar: "))
                c = int(input("ingrese el coeficiente de sustentacion: "))
                d = int(input("Ingrese la densidad del aire:"))
                v_stall = (2*w)/(d*s*c)
                v_stal = pow(v_stall, 0.5)
                print("calculando procedimiento ", v_stal)
                print("Ingrese 0 si desea salir o ingrese el valor de la velocidad para continuar")
                v_actual = int(input("Ingrese el valor de la velocidad: "))

                conta += 1
                if v_actual == 0:
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
            contr = False
        case _:
            print("modo no valido")     
```
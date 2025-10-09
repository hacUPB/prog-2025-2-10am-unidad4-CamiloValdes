aeronaves = {
    "Boeing 747": {"peso": 183500, "superficie_alar": 511, "velocidad_crucero": 917},
    "Airbus A320": {"peso": 78000, "superficie_alar": 122.6, "velocidad_crucero": 828},
    "Cessna 172": {"peso": 1157, "superficie_alar": 16.2, "velocidad_crucero": 226}
}
resultados = []
co = True
while co == True:
    print("Abriendo el menu del programa")
    print("Ingrese la opcion que desea realizar")
    print("1. Ejecutar el Programa\n2. Salir\n")
    op = input("Elija una opcion ")
    match op:
        case "1":
            contr = True
            while contr == True:
                print("ingrese la seccion que desea ver")
                print(" 1. Qué es \n 2. Simulacion \n 3. Aeronaves\n 4. Listas\n 0. Regresar \n")
                opcio = input("Elija una opcion ")
                match opcio:
                    case "1":
                        print("Qué es")
                        print("fenómeno aerodinámico donde el ala de un avión pierde sustentación porque el ángulo de ataque excede un límite crítico, haciendo que el flujo de aire sobre el ala se vuelva turbulento. Esto resulta en una pérdida de control y una rápida caída de altura. La recuperación implica disminuir el ángulo de ataque y aumentar la velocidad, generalmente bajando el morro del avión y añadiendo potencia. ")
                    case "2":
                        print("Simulacion stall")
                        print("El programa simulará el vuelo de una aeronave en el cual verificará en cada instante si la aeronave se encuentra en condiciones seguras o si está entrando en perdida.")
                        print("Seleccione una aeronave para la simulación:")
                        for idx, nombre in enumerate(aeronaves.keys()):                     #Uso de la IA para seleccionar una aeronave 
                            print(f"{idx+1}. {nombre}")
                        seleccion = input("Ingrese el número de la aeronave: ")
                        try:
                            seleccion = int(seleccion)
                            nombre_aeronave = list(aeronaves.keys())[seleccion-1]
                            datos_aeronave = aeronaves[nombre_aeronave]
                            print(f"Seleccionaste: {nombre_aeronave}")
                        except (ValueError, IndexError):
                            print("Selección inválida. Usando datos manuales.")
                            datos_aeronave = None
                        resultados = []
                        conta = 0
                        while conta < 10:
                            if datos_aeronave:
                                w = datos_aeronave["peso"]
                                s = datos_aeronave["superficie_alar"]
                                print(f"Peso: {w} kg, Superficie alar: {s} m²")
                            else:
                                w = float(input("Ingrese el peso: "))
                                s = float(input("Ingrese la superficie alar: "))
                            c = float(input("Ingrese el coeficiente de sustentacion: "))
                            d = float(input("Ingrese la densidad del aire: "))
                            v_stall = (2*w)/(d*s*c)
                            v_stal = pow(v_stall, 0.5)
                            print("calculando procedimiento ", v_stal)
                            print("Ingrese 0 si desea salir o ingrese el valor de la velocidad para continuar")
                            v_actual = float(input("Ingrese el valor de la velocidad: "))
                            margen_seguridad = v_actual - v_stal
 
                            resultados.append([v_stal, v_actual, margen_seguridad])
 
                            conta += 1
                            if v_actual == 0:
                                break
                            if v_actual > v_stal:
                                print("Seguro, el avion esta por encima de la velocidad de perdida")
                            else:
                                print("Precaucion, velocidad de perdida, aumentar velocidad")

                    # Estadísticas de la simulación: sólo los tres promedios (sin comprensiones)                       #Uso de la IA para hacer las operaciones estadisticas
                        if resultados:
                            sum_v_stal = 0.0
                            sum_v_actual = 0.0
                            sum_margen = 0.0
                            count = 0

                        for r in resultados:
                            # r == [v_stal, v_actual, margen]
                            sum_v_stal += float(r[0])
                            sum_v_actual += float(r[1])
                            sum_margen += float(r[2])
                            count += 1

                        # calcular promedios
                        promedio_v_stal = sum_v_stal / count
                        promedio_v_actual = sum_v_actual / count
                        promedio_margen = sum_margen / count

                        print("\n--- Promedios de la simulación ---")
                        print(f"Promedio velocidad de pérdida: {promedio_v_stal:.2f}")
                        print(f"Promedio velocidad actual: {promedio_v_actual:.2f}")
                        print(f"Promedio margen de seguridad: {promedio_margen:.2f}")
                    case "3":
                        print("Aeronaves disponibles")
                        for aeronave, datos in aeronaves.items():
                            print(f"Aeronave: {aeronave}")
                            for key, value in datos.items():
                                print(f"  {key}: {value}")
                            print()
                        print("Puede usar estos datos en la simulación seleccionando una aeronave.")
                    case "4":
                        print("Ejecución lista (Resultados)")
                        if resultados:
                            print("Velocidad de perdida, velocidad actual, margen de seguridad")
                        for r in resultados:
                            print(f"| {r[0]:} | {r[1]} | {r[2]}")
                    case "0":
                        print("Regresando")
                        break
                    case _:
                        print("modo no valido")
        case "2":
            print("Saliendo del programa")
            break
        case _:
            print("opcion no valida")
con = True
while con == True:
    print("MENU PRINCIPAL")
    print("1. Ejecutar el programa completo")
    print("2. Salir definitivamente")
    opcmen = int(input("Elija una de las dos opciones"))
    if opcmen =="1":
        
        contr = True
        aeronaves = {
        "Boeing 747": {"peso": 183500, "superficie_alar": 511, "velocidad_crucero": 917},
        "Airbus A320": {"peso": 78000, "superficie_alar": 122.6, "velocidad_crucero": 828},
        "Cessna 172": {"peso": 1157, "superficie_alar": 16.2, "velocidad_crucero": 226}
        }

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
                    print("El programa simulará el vuelo de una aeronave en el cual verificará en cada instante si la aeronave se encuentra en condiciones seguras o si está entrando en perdida.")
                    print("Seleccione una aeronave para la simulación:")
                    for idx, nombre in enumerate(aeronaves.keys()):                     #Uso de la IA para seleccionar una aeronave  Lineas 20 - 30
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

                    # Estadísticas de la simulación
                    if resultados:                                                                      #Uso de la IA para mostrar estadisticas Lineas 62 - 75
                        v_stal_list = [r[0] for r in resultados]
                        v_actual_list = [r[1] for r in resultados]
                        margen_list = [r[2] for r in resultados]
                        print("\n--- Estadísticas de la simulación ---")
                        print(f"Promedio velocidad de pérdida: {sum(v_stal_list)/len(v_stal_list):.2f}")
                        print(f"Máxima velocidad de pérdida: {max(v_stal_list):.2f}")
                        print(f"Mínima velocidad de pérdida: {min(v_stal_list):.2f}")
                        print(f"Promedio velocidad actual: {sum(v_actual_list)/len(v_actual_list):.2f}")
                        print(f"Máxima velocidad actual: {max(v_actual_list):.2f}")
                        print(f"Mínima velocidad actual: {min(v_actual_list):.2f}")
                        print(f"Promedio margen de seguridad: {sum(margen_list)/len(margen_list):.2f}")
                        print(f"Máximo margen de seguridad: {max(margen_list):.2f}")
                        print(f"Mínimo margen de seguridad: {min(margen_list):.2f}")
                case "3":
                    print("Aeronaves disponibles")
                    for aeronave, datos in aeronaves.items():
                        print(f"Aeronave: {aeronave}")
                        for key, value in datos.items():
                            print(f"  {key}: {value}")
                        print()
                    print("Puede usar estos datos en la simulación seleccionando una aeronave.")
                case "0":
                    print("Regresando")
                    break
                    
                case _:
                    print("Modo no valido")
    elif opcmen == "2":
        print("Usted ha salido del programa, hasta luego")
    else:
        print("La ocion ingresada no es valida")

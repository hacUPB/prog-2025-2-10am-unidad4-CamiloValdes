control = True
while control == True:
    print("ingrese el numero del simulador")
    print(" 110. Velocidad de perdida \n 220. Ascendencia y Densidad \n 330. Angulo de ascenso \n 000. Salir\n")
    opcion = input("Elija una opcion ")
    match opcion:
        case "110":
            print("Modo seleccionado, Velocidad de perdida")
            contr = True
            while contr == True:
                print("ingrese la seccion que desea ver")
                print(" 1. que es \n 2. simulacion \n 0. salir \n")
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
                        def cont(v_stal, v_actual):
                            result = [v_stal, v_actual]
                            return result
                    case "0":
                        print("Regresando")
                        break
                    case _:
                        print("modo no valido")
        case "220":
            print("Modo seleccionado, Ascendencia y Densidad")
            cont = True
            while cont == True:
                print("ingrese la seccion que desea ver")
                print(" 1. que es\n 2. simulacion\n 0. salir\n")
                opci = input("Elija una opcion")
                match opci:
                    case "1":
                        print("Que es")
                        print("Cuando un avión asciende, la densidad del aire disminuye y, por tanto, la potencia disponible del motor también se reduce. Esto afecta directamente la capacidad del avión para seguir ganando altitud.")
                        break
                    case "2":
                        print("Simulación de ascenso del avión por 10 segundos")
                        print("El programa simulara durante 10 segundos de ascenso en los que el usuario decide si aumentar, mantener o disminuir la potencia del motor, y observar cómo cambia la altitud alcanzada.")
                        import math                             #Uso de IA para el uso de la raiz cuadrada
                        def calcular_ROC(potencia, densidad):
                            return (potencia * densidad) // 100
                        potencia_inicial = int(input("Ingrese la potencia inicial: "))
                        altitud = 0
                        potencia = potencia_inicial
                        for t in range(1, 11):
                            print("Segundo", t),t
                            print("Potencia actual:", potencia)
                            print("Altitud actual:", altitud)
                            densidad = int(1.225 * math.exp(-altitud / 10000))
                            roc = calcular_ROC(potencia, densidad)                        #Uso de IA
                            altitud = altitud + roc
                            print("Nueva altitud:", altitud)
                            if roc < 1:
                                print("¡Advertencia! El avión no asciende lo suficiente.")
                                print("¿Desea cambiar la potencia?")
                                print("1. Aumentar potencia")
                                print("2. Mantener potencia")
                                print("3. Disminuir potencia")
                            decision = int(input("Opción: "))
                            if decision == 1:
                                potencia = potencia + 10
                            elif decision == 3:
                                potencia = potencia - 10
                        print("Simulación terminada. Altitud final:", altitud)
                    case "0":
                        print("regresando")
                        break
                    case _:
                        print("modo no valido")
        case "330":
            print("Modo seleccionado, Angulo de ascenso")
            con = True
            while con == True:
                print("ingrese la seccion que desea ver")
                print(" 1. que es\n 2. simulacion\n 0. salir\n")
                opc = input("Elija una opcion")
                match opc:
                    case "1":
                        print("Qué es")
                        print("El ángulo de ascenso es la inclinación de la trayectoria de vuelo con respecto a la horizontal. Este ángulo de ascenso está directamente relacionado con la sustentación y el arrastre, ya que el lift es la fuerza que mantiene el avión en el aire y el drag es la resistencia que se opone al movimiento. En general, aumentar el ángulo de ataque (el ángulo entre el ala y la corriente de aire) incrementa tanto la sustentación como el arrastre, aunque el arrastre aumenta más rápidamente y puede llevar a una pérdida de sustentación. Para un ascenso eficiente, la aeronave debe generar la sustentación suficiente para superar su peso y el arrastre, manteniendo un equilibrio")
                        break
                    case "2":
                        print("Simulación de angulo de ataque con relacion al drag y lifting")
                        print("El programa simulara 10 segundos de vuelo de una aeronave, el usuario podra aumentar o disminuir o mantener constante la velocidad. En cada segundo el drag, el lifting y el angulo de ascenso. Si el angulo de ascenso se vuelve negativo se debe alertar que el avion no puede seguir subiendo")
                        import math                                #Uso de IA para el uso de degrees
                        def calcular_angulo(rho, V, S, CL, CD, W):
                            L = (rho * (V ** 2) * S * CL) // 2
                            D = (rho * (V ** 2) * S * CD) // 2
                            relacion = (L - D) // W
                            theta = int(math.degrees(math.atan(relacion)))
                            return theta            #Uso de IA

                        print(" Simulación del Ángulo de Ascenso")

                        W = int(input("Ingrese el peso del avión (N): "))
                        rho = int(input("Ingrese la densidad del aire (kg/m^3): "))
                        S = int(input("Ingrese la superficie alar (m^2): "))
                        CL = int(input("Ingrese el coeficiente de sustentación: "))
                        CD = int(input("Ingrese el coeficiente de arrastre: "))
                        V = int(input("Ingrese la velocidad inicial del avión (m/s): "))

                        contador = 0

                        while contador < 10:
                            theta = calcular_angulo(rho, V, S, CL, CD, W)

                            print("\nSegundo:", contador + 1)
                            print("Velocidad:", V, "m/s")
                            print("Ángulo de ascenso:", theta, "grados")

                            if theta < 0:
                                print("El avión no puede seguir ascendiendo.")
                                break

                            print("Ingrese 1 para aumentar velocidad, 2 para disminuir, 3 para mantener, 0 para salir")
                            decision = int(input("Decisión: "))

                            if decision == 0:
                                print(" Saliendo de la simulación por decisión del usuario.")
                                break
                            elif decision == 1:
                                V = V + 10
                            elif decision == 2:
                                V = V - 10
                            contador = contador + 1

                        print("\nSimulación terminada.")

                    case "0":
                        print("Regresando")
                        break
                    case _:
                        print("modo no valido")
        case "000":
            break
        case _:
            print("modo no valido")


# Programa con listas y diccionarios 

control = True

# Diccionario para guardar parámetros de cada simulador
simuladores = {
    "110": {"nombre": "Velocidad de perdida", "resultados": []},
    "220": {"nombre": "Ascendencia y Densidad", "resultados": []},
    "330": {"nombre": "Angulo de ascenso", "resultados": []}
}

while control:
    print("ingrese el numero del simulador")
    print(" 110. Velocidad de perdida \n 220. Ascendencia y Densidad \n 330. Angulo de ascenso \n 000. Salir\n")
    opcion = input("Elija una opcion ")
    match opcion:
        case "110":
            print("Modo seleccionado, Velocidad de perdida")
            contr = True
            while contr:
                print("ingrese la seccion que desea ver")
                print(" 1. que es \n 2. simulacion \n 0. salir \n")
                opcio = input("Elija una opcion ")
                match opcio:
                    case "1":
                        print("Que es")
                        print("fenómeno aerodinámico donde el ala de un avión pierde sustentación porque el ángulo de ataque excede un límite crítico, haciendo que el flujo de aire sobre el ala se vuelva turbulento. Esto resulta en una pérdida de control y una rápida caída de altura. La recuperación implica disminuir el ángulo de ataque y aumentar la velocidad, generalmente bajando el morro del avión y añadiendo potencia. ")
                        break
                    case "2":
                        print("Simulacion stall")
                        print("El programa simulará el vuelo de una aeronave en el cual verificará en cada instante si la aeronave se encentra en condiciones seguras o si está entrando en perdida.")
                        resultados_stall = []  # Lista para guardar resultados de cada iteración
                        conta = 0
                        while conta < 10:
                            parametros = {}  # Diccionario para guardar parámetros de cada simulación
                            parametros['peso'] = int(input("Ingrese el peso: "))
                            parametros['superficie'] = int(input("Ingrese la superficie alar: "))
                            parametros['coef_sustentacion'] = int(input("ingrese el coeficiente de sustentacion: "))
                            parametros['densidad'] = int(input("Ingrese la densidad del aire:"))
                            v_stall = (2 * parametros['peso']) / (parametros['densidad'] * parametros['superficie'] * parametros['coef_sustentacion'])
                            v_stal = pow(v_stall, 0.5)
                            print("calculando procedimiento ", v_stal)
                            parametros['v_stal'] = v_stal
                            v_actual = int(input("Ingrese el valor de la velocidad: "))
                            parametros['v_actual'] = v_actual
                            conta += 1
                            if v_actual == 0:
                                break
                            if v_actual > v_stal:
                                print("Seguro, el avion esta por encima de la velocidad de perdida")
                                parametros['estado'] = "Seguro"
                            else:
                                print("Precaucion, velocidad de perdida, aumentar velocidad")
                                parametros['estado'] = "Precaucion"
                            resultados_stall.append(parametros)
                        simuladores["110"]["resultados"].extend(resultados_stall)
                        print("Resultados de la simulación:")
                        for res in resultados_stall:
                            print(res)
                    case "0":
                        print("Regresando")
                        break
                    case _:
                        print("modo no valido")
        case "220":
            print("Modo seleccionado, Ascendencia y Densidad")
            cont = True
            while cont:
                print("ingrese la seccion que desea ver")
                print(" 1. que es\n 2. simulacion\n 0. salir\n")
                opci = input("Elija una opcion")
                match opci:
                    case "1":
                        print("Que es")
                        print("Cuando un avión asciende, la densidad del aire disminuye y, por tanto, la potencia disponible del motor también se reduce. Esto afecta directamente la capacidad del avión para seguir ganando altitud.")
                        break
                    case "2":
                        print("Simulación de ascenso del avión por 10 segundos")
                        print("El programa simulara durante 10 segundos de ascenso en los que el usuario decide si aumentar, mantener o disminuir la potencia del motor, y observar cómo cambia la altitud alcanzada.")
                        import math
                        def calcular_ROC(potencia, densidad):
                            return (potencia * densidad) // 100
                        potencia_inicial = int(input("Ingrese la potencia inicial: "))
                        altitud = 0
                        potencia = potencia_inicial
                        resultados_ascenso = []  # Lista para guardar resultados de cada segundo
                        for t in range(1, 11):
                            densidad = int(1.225 * math.exp(-altitud / 10000))
                            roc = calcular_ROC(potencia, densidad)
                            altitud = altitud + roc
                            print("Segundo", t)
                            print("Potencia actual:", potencia)
                            print("Altitud actual:", altitud)
                            print("Nueva altitud:", altitud)
                            if roc < 1:
                                print("¡Advertencia! El avión no asciende lo suficiente.")
                                print("¿Desea cambiar la potencia?")
                                print("1. Aumentar potencia")
                                print("2. Mantener potencia")
                                print("3. Disminuir potencia")
                            decision = int(input("Opción: "))
                            if decision == 1:
                                potencia += 10
                            elif decision == 3:
                                potencia -= 10
                            # Guardar resultados en diccionario
                            resultados_ascenso.append({
                                "segundo": t,
                                "potencia": potencia,
                                "altitud": altitud,
                                "roc": roc
                            })
                        simuladores["220"]["resultados"].extend(resultados_ascenso)
                        print("Simulación terminada. Altitud final:", altitud)
                        print("Resultados de la simulación:")
                        for res in resultados_ascenso:
                            print(res)
                    case "0":
                        print("regresando")
                        break
                    case _:
                        print("modo no valido")
        case "330":
            print("Modo seleccionado, Angulo de ascenso")
            con = True
            while con:
                print("ingrese la seccion que desea ver")
                print(" 1. que es\n 2. simulacion\n 0. salir\n")
                opc = input("Elija una opcion")
                match opc:
                    case "1":
                        print("Qué es")
                        print("El ángulo de ascenso es la inclinación de la trayectoria de vuelo con respecto a la horizontal. Este ángulo de ascenso está directamente relacionado con la sustentación y el arrastre, ya que el lift es la fuerza que mantiene el avión en el aire y el drag es la resistencia que se opone al movimiento. En general, aumentar el ángulo de ataque (el ángulo entre el ala y la corriente de aire) incrementa tanto la sustentación como el arrastre, aunque el arrastre aumenta más rápidamente y puede llevar a una pérdida de sustentación. Para un ascenso eficiente, la aeronave debe generar la sustentación suficiente para superar su peso y el arrastre, manteniendo un equilibrio")
                        break
                    case "2":
                        print("Simulación de angulo de ataque con relacion al drag y lifting")
                        print("El programa simulara 10 segundos de vuelo de una aeronave, el usuario podra aumentar o disminuir o mantener constante la velocidad. En cada segundo el drag, el lifting y el angulo de ascenso. Si el angulo de ascenso se vuelve negativo se debe alertar que el avion no puede seguir subiendo")
                        import math
                        def calcular_angulo(rho, V, S, CL, CD, W):
                            L = (rho * (V ** 2) * S * CL) // 2
                            D = (rho * (V ** 2) * S * CD) // 2
                            relacion = (L - D) // W
                            theta = int(math.degrees(math.atan(relacion)))
                            return theta
                        print(" Simulación del Ángulo de Ascenso")
                        W = int(input("Ingrese el peso del avión (N): "))
                        rho = int(input("Ingrese la densidad del aire (kg/m^3): "))
                        S = int(input("Ingrese la superficie alar (m^2): "))
                        CL = int(input("Ingrese el coeficiente de sustentación: "))
                        CD = int(input("Ingrese el coeficiente de arrastre: "))
                        V = int(input("Ingrese la velocidad inicial del avión (m/s): "))
                        contador = 0
                        resultados_angulo = []  # Lista para guardar resultados de cada segundo
                        while contador < 10:
                            theta = calcular_angulo(rho, V, S, CL, CD, W)
                            print("\nSegundo:", contador + 1)
                            print("Velocidad:", V, "m/s")
                            print("Ángulo de ascenso:", theta, "grados")
                            if theta < 0:
                                print("El avión no puede seguir ascendiendo.")
                                break
                            print("Ingrese 1 para aumentar velocidad, 2 para disminuir, 3 para mantener, 0 para salir")
                            decision = int(input("Decisión: "))
                            if decision == 0:
                                print(" Saliendo de la simulación por decisión del usuario.")
                                break
                            elif decision == 1:
                                V += 10
                            elif decision == 2:
                                V -= 10
                            resultados_angulo.append({
                                "segundo": contador + 1,
                                "velocidad": V,
                                "angulo": theta
                            })
                            contador += 1
                        simuladores["330"]["resultados"].extend(resultados_angulo)
                        print("\nSimulación terminada.")
                        print("Resultados de la simulación:")
                        for res in resultados_angulo:
                            print(res)
                    case "0":
                        print("Regresando")
                        break
                    case _:
                        print("modo no valido")
        case "000":
            print("Saliendo del programa.")
            break
        case _:
            print("modo no valido")
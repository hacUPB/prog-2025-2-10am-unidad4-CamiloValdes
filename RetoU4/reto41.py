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
                    case "0":
                        print("Regresando")
                        break
                    case _:
                        print("modo no valido")     
def conversomoneda():

    #variables monedas
    dolar = 909.09
    euro = 1073.83  
    libra = 1219


    print("Bienvenido al conversor de moneda chile clp")
    respuesta_usuario= input("Deseas ingresar al conversor").lower()

    if respuesta_usuario =="si":
        print("Bienvenido, escoje una de las siguientes monedas a cambiar")

        opciones = 0

        while opciones!=4:
            print("1-dolar")
            print("2-euro")
            print("3-libra esterlina")
            print("4-salir")
            try:
                opciones = int(input("escoge una de las siguientes opciones que deseas convertir"))
                if opciones==1:
                    monto_usuario =float(input("has seleccionado convertir dolar a peso chileno, ingresa el monto"))
                    resultado=monto_usuario*dolar
                    print("la conversion es:",resultado)
                elif opciones ==2:
                    monto_usuario =float(input("has seleccionado convertir euro a peso chileno, ingresa el monto"))
                    resultado=monto_usuario*euro
                    print("la conversion es:",resultado)
                elif opciones ==3:
                    monto_usuario =float(input("has seleccionado convertir libra a peso chileno, ingresa el monto"))
                    resultado=monto_usuario*libra
                    print("la conversion es:",resultado)

                elif opciones ==4:
                    print("haz salido del conversor")
                    break
                else:
                    print("opcion numerica no valida, vuelva a intentarlo")
                    
                    

            except ValueError:
                print("No se admite texto, solo numero, por favor vuelva a intentarlo.")
                

    else:
        print("programa terminado con exito")

conversomoneda()
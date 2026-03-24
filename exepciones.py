def sumar():
    try:

        numero1=int(input("introduce un numero por favor"))
        numero2=int(input("introduce un numero por favor"))

    except:
        print("no se admiten texto solo numeros")
        return

    print("el resultado es " + str(numero1+numero2))
    

sumar()
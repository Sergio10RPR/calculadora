from calculadora import dividir, multiplicar, resta,suma
def menu():
    num=0
    while num!=5:
        print("*****MENU*****")
        print("1.SUMA")
        print("2.RESTA")
        print("3.MULTIPLICACION")
        print("4.DIVISION")
        print("5.SALIR")
        num=int(input("Ingrese la opcion: "))
        print(num)
        if num==1:
            print("--Suma--")
            print("Ingrese un numero: ")
            a=int(input(": "))
            print()
            print("Ingrese un numero: ")
            b=int(input(": "))
            print("El resultado es: " , (suma(a,b)))
      
        elif num==2:
            print("--Resta--")
            print("Ingrese un numero: ")
            a=int(input(": "))
            print()
            print("Ingrese un numero: ")
            b=int(input(": "))
            print("El resultado es: " , (resta(a,b)))
        elif num==3:
            print("--Multiplicacion")
            print("Ingrese un numero: ")
            a=int(input(": "))
            print("Ingrese un numero: ")
            b=int(input(": "))
            print("El resultado es: ",multiplicar(a,b))
        elif num==4:
            print("--Division")
            print("Ingrese un numero: ")
            a=int(input(": "))
            print("Ingrese un numero: ")
            b=int(input(": "))
            print("El resultado es: ",dividir(a,b))

            
from calculadora import resta,suma
def menu():
    num=0
    while num!=3:
        print("*****MENU*****")
        print("1.SUMA")
        print("2.RESTA")
        print("3.SALIR")
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
            
            
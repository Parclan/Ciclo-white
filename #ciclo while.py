#ciclo while

"""while True:
    num = int(input("Digite un numero del 1 al 10: "))
    if num == 2:
        break
print("ese es el numero correcto")"""
 
"""while True:
    print("Que es lo que dice miau?")
    nLinea = str(input(""))
    if nLinea == "gato":
        break #para romper el ciclo
print("correcto")"""

while True:
    
    def functionA():
        print("Carlos")
        
    def functionB():
        print("Pedro")
    
    def functionC():
        print("Juan")
        
    eleccion = input("Por que quien vas a votar A, B, C: ")
    
    if eleccion == "A":
        functionA()
        print("Tu papa es Carlos")
        break
        
        
    elif eleccion == "B":
    
        functionB()
        
    elif eleccion == "C":
    
        functionC()
    else:
        print("Elija una opción correcta")
        

    
    
    
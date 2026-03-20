print("===CALCULADORA===")

numero1 = float(input("Escribe el primer numero: "))
numero2 = float(input("Escribe el segundo numero: "))

operacion = input("Elige la operacion (+, -, *, /): ")

if operacion == "+":
    print("Resultado:", numero1 + numero2)
elif operacion == "-":
    print("Resultado:", numero1 - numero2)
elif operacion == "*":
    print("Resultado:", numero1 * numero2)
elif operacion == "/":
    if numero2 != 0:
        print("Resultado:", numero1 / numero2)
    else:
        print("Error: no dividir entre 0")
else:
    print("Operacion no valida")
# Ejercicio 1: Función para verificar si una contraseña es segura
def es_segura(contrasena):
    """
    Verifica si una contraseña contiene al menos una letra mayúscula,
    una letra minúscula y un número.
    
    Argumentos:
    contrasena -- string, la contraseña a verificar
    
    Retorna:
    True si la contraseña es segura, False en caso contrario
    """
    tiene_mayuscula = any(c.isupper() for c in contrasena)
    tiene_minuscula = any(c.islower() for c in contrasena)
    tiene_numero = any(c.isdigit() for c in contrasena)
    
    return tiene_mayuscula and tiene_minuscula and tiene_numero


# Ejercicio 2: Función recursiva para sumar números ingresados por el usuario
def sumar_numeros():
    """
    Lee números ingresados por el usuario hasta que se ingrese un espacio en blanco.
    
    Retorna:
    La suma de los números ingresados.
    """
    total = 0
    while True:
        numero = input("Ingresa un número o deja en blanco para finalizar: ")
        if numero == "":
            break
        try:
            total += int(numero)
        except ValueError:
            print("Por favor, ingresa solo números.")
    return total


# Ejercicio 3: Clase "Cuenta" para manejo bancario
class Cuenta:
    def __init__(self, numero, titular, saldo, tipo_cuenta):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.tipo_cuenta = tipo_cuenta

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes.")

    def obtener_balance(self):
        return self.saldo

    def mostrar_informacion(self):
        print(f"Cuenta número: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")
        print(f"Tipo de cuenta: {self.tipo_cuenta}")


# Ejecución de los ejercicios
# Ejercicio 1: Verificar contraseña
contrasena = input("Ingresa una contraseña para verificar si es segura: ")
segura = es_segura(contrasena)
print(f"La contraseña '{contrasena}' es segura: {segura}")

# Ejercicio 2: Sumar números
suma_total = sumar_numeros()
print(f"La suma total de los números ingresados es: {suma_total}")

# Ejercicio 3: Manejo de cuenta bancaria
numero_cuenta = input("Ingresa el número de cuenta: ")
titular = input("Ingresa el nombre del titular: ")
saldo_inicial = float(input("Ingresa el saldo inicial: "))
tipo_cuenta = input("Ingresa el tipo de cuenta: ")

cuenta = Cuenta(numero_cuenta, titular, saldo_inicial, tipo_cuenta)

cantidad_deposito = float(input("Ingresa la cantidad a depositar: "))
cuenta.depositar(cantidad_deposito)

cantidad_retiro = float(input("Ingresa la cantidad a retirar: "))
cuenta.retirar(cantidad_retiro)

# Mostrar toda la información de la cuenta
cuenta.mostrar_informacion()

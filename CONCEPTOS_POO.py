class Vehiculo:
    def __init__(self, marca, modelo, color):
        self._marca = marca  # Encapsulamiento: atributo protegido
        self._modelo = modelo
        self._color = color

    def acelerar(self):
        print("El vehículo está acelerando.")

    def frenar(self):
        print("El vehículo está frenando.")

    # Abstracción: Método abstracto para la función sonido
    def hacer_sonido(self):
        pass

    # Mensajes y métodos: Método para imprimir información del vehículo
    def imprimir_info(self):
        print(f"Marca: {self._marca}")
        print(f"Modelo: {self._modelo}")
        print(f"Color: {self._color}")

    # Destructor: Se puede implementar, pero no es común en Python


class Carro(Vehiculo):  # Herencia: Carro hereda de Vehiculo
    def __init__(self, marca, modelo, color, num_puertas):
        super().__init__(marca, modelo, color)
        self._num_puertas = num_puertas

    # Polimorfismo: Sobrescritura del método hacer_sonido
    def hacer_sonido(self):
        print("El carro hace un sonido de motor.")

    # Atributos y propiedades: Método getter para el número de puertas
    @property
    def num_puertas(self):
        return self._num_puertas

    # Constructores y destructores: No se implementa destructor en Python


class Moto(Vehiculo):  # Herencia: Moto hereda de Vehiculo
    def __init__(self, marca, modelo, color, cilindrada):
        super().__init__(marca, modelo, color)
        self._cilindrada = cilindrada

    # Polimorfismo: Sobrescritura del método hacer_sonido
    def hacer_sonido(self):
        print("La moto hace un sonido de motor.")

    # Atributos y propiedades: Método getter para la cilindrada
    @property
    def cilindrada(self):
        return self._cilindrada

    # Constructores y destructores: No se implementa destructor en Python


if __name__ == "__main__":
    # Crear un carro y una moto
    carro = Carro("Toyota", "Corolla", "Rojo", 4)
    moto = Moto("Honda", "CBR", "Negro", "600cc")

    # Usar métodos de Carro y Moto
    carro.acelerar()
    carro.imprimir_info()
    carro.hacer_sonido()
    print(f"Número de puertas del carro: {carro.num_puertas}")

    moto.frenar()
    moto.imprimir_info()
    moto.hacer_sonido()
    print(f"Cilindrada de la moto: {moto.cilindrada}")

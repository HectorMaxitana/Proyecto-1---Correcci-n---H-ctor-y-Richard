from abc import ABC


#Integrantes: Héctor Maxitana y Richard Constante


class persona (ABC):
    def __init__(self, cedula: str = None, nombre: str = None, apellido: str = None, email: str = None,
                 telefono: str = None, direccion: str = None, numero_libros: int = None, activo: bool = None,
                 carrera: str = None):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.numero_libros = numero_libros
        self.activo = activo
        self.carrera = carrera

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, nuevo_cedula):
        self._cedula = nuevo_cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, nuevo_email):
        self._email = nuevo_email

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        self._telefono = nuevo_telefono

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, nuevo_direccion):
        self._direccion = nuevo_direccion

    @property
    def numero_libros(self):
        return self._numero_libros

    @numero_libros.setter
    def numero_libros(self, nuevo_numero_libros):
        self._numero_libros = nuevo_numero_libros

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, nuevo_activo):
        self._activo = nuevo_activo

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, nuevo_carrera):
        self._carrera = nuevo_carrera

    def obtener_cedula(self):
        return self.cedula

    def obtener_nombre(self):
        return self.nombre

    def obtener_apellido(self):
        return self.apellido

    def obtener_email(self):
        return self.email

    def obtener_telefono(self):
        return self.telefono

    def obtener_direccion(self):
        return self.direccion

    def obtener_numero_libros(self):
        return self.numero_libros

    def obtener_activo(self):
        return self.activo

    def obtener_carrera(self):
        return self.carrera

    def modificar_cedula(self, nueva_cedula):
        self.cedula = nueva_cedula

    def modificar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def modificar_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def modificar_email(self, nuevo_email):
        self.email = nuevo_email

    def modificar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono

    def modificar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion

    def modificar_numero_libros(self, nuevo_numero_libros):
        self.numero_libros = nuevo_numero_libros

    def modificar_activo(self, nuevo_activo):
        self.activo = nuevo_activo

    def modificar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

    def __str__(self):
        return (f"Cédula: {self.cedula}, Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, "
                f"Teléfono: {self.telefono}, Dirección: {self.direccion}, Número de Libros: {self.numero_libros}, "
                f"Activo: {self.activo}, Carrera: {self.carrera}")

    def pedir_libro(self):
        if self.numero_libros > 0:
            self.numero_libros -= 1
            return True
        else:
            print("No hay libros disponibles para pedir.")
            return False


#persona1 = Persona(cedula="0927366578", nombre="Shon", apellido="Murfi", email="e1@example.com", telefono="0973678392",
#                   direccion="Dirección1", numero_libros=2, activo=True, carrera="Carrera1")

# Imprimir información antes de pedir un libro
#print("Antes de pedir un libro:")
#print(f"Nombre: {persona1.obtener_nombre()}")
#print(f"Número de Libros: {persona1.obtener_numero_libros()}")

# Pedir un libro
#persona1.pedir_libro()

# Imprimir información después de pedir un libro
#print("\nDespués de pedir un libro:")
#print(f"Nombre: {persona1.obtener_nombre()}")
#print(f"Número de Libros: {persona1.obtener_numero_libros()}")

# Imprimir toda la información de la persona
#print("\nInformación completa de la persona:")
#print(persona1)

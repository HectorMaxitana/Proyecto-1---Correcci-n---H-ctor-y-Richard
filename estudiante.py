from persona import persona


#Integrantes: Héctor Maxitana y Richard Constante


class estudiante(persona):
    contador_estudiante = 0

    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera,
                 id: int = None, nivel: int = None):
        persona.__init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera)
        estudiante.contador_estudiante += 1
        self.id = id
        self.nivel = nivel

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nueva_id):
        self._id = nueva_id

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nuevo_nivel):
        self._nivel = nuevo_nivel

    def obtener_id(self):
        return self.id

    def obtener_nivel(self):
        return self.nivel

    def modificar_nivel(self, nuevo_nivel):
        self.nivel = nuevo_nivel

    def pedir_libro(self):
        if self.numero_libros > 0:
            self.numero_libros -= 1
            return True
        else:
            print("No hay libros disponibles para pedir.")
            return False

    def devolver_libro(self):
        self.numero_libros += 1
        return True


#estudiante1 = Estudiante(cedula="0927366578", nombre="Shon", apellido="Murfi", email="e1@example.com",
#                         telefono="0973678392", direccion="Dirección1", numero_libros=2, activo=True,
#                         carrera="Carrera1", id=23845, nivel=2)

#print("Información del Estudiante antes de las operaciones:")
#print(estudiante1)

# Pedir un libro
#print("Número de libros antes de pedir: {}".format(estudiante1.obtener_numero_libros()))
#if estudiante1.pedir_libro():
#    print("Libro pedido con éxito.")
#else:
#    print("No se pudo pedir el libro.")
#print("Número de libros después de pedir: {}".format(estudiante1.obtener_numero_libros()))

# Devolver un libro
#print("Número de libros antes de devolver: {}".format(estudiante1.obtener_numero_libros()))
#estudiante1.devolver_libro()
#print("Número de libros después de devolver: {}".format(estudiante1.obtener_numero_libros()))

# Modificar el nivel del estudiante
#print("Nivel del estudiante antes de modificar: {}".format(estudiante1.obtener_nivel()))
#estudiante1.modificar_nivel(3)
#print("Nivel del estudiante después de modificar: {}".format(estudiante1.obtener_nivel()))

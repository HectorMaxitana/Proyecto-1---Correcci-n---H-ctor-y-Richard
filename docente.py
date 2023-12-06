from persona import persona


#Integrantes: Héctor Maxitana y Richard Constante


class docente(persona):
    contador_docente = 0

    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera,
                 id: int = None, titulo_3er_nivel: str = None, titulo_4to_nivel: str = None):
        persona.__init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera)
        docente.contador_docente += 1
        self.id = id
        self.titulo_3er_nivel = titulo_3er_nivel
        self.titulo_4to_nivel = titulo_4to_nivel

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nueva_id):
        self._id = nueva_id

    @property
    def titulo_3er_nivel(self):
        return self._titulo_3er_nivel

    @titulo_3er_nivel.setter
    def titulo_3er_nivel(self, nuevo_titulo):
        self._titulo_3er_nivel = nuevo_titulo

    @property
    def titulo_4to_nivel(self):
        return self._titulo_4to_nivel

    @titulo_4to_nivel.setter
    def titulo_4to_nivel(self, nuevo_titulo):
        self._titulo_4to_nivel = nuevo_titulo

    def obtener_id(self):
        return self.id

    def obtener_titulo_3er_nivel(self):
        return self.titulo_3er_nivel

    def obtener_titulo_4to_nivel(self):
        return self.titulo_4to_nivel

    def modificar_titulo_3er_nivel(self, nuevo_titulo):
        self.titulo_3er_nivel = nuevo_titulo

    def modificar_titulo_4to_nivel(self, nuevo_titulo):
        self.titulo_4to_nivel = nuevo_titulo

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


#docente1 = Docente(cedula="0927366578", nombre="Shon", apellido="Murfi", email="e1@example.com", telefono="0973678392",
#                   direccion="Dirección1", numero_libros=2, activo=True, carrera="Carrera1", id=23845,
#                   titulo_3er_nivel="Ing. Aeronautico", titulo_4to_nivel="Dr. en Ciencias Naturales")

# Imprimir información del docente antes de realizar operaciones
#print("Información del Docente antes de las operaciones:")
#print(docente1)

# Pedir un libro
#print("Número de libros antes de pedir: {}".format(docente1.obtener_numero_libros()))
#if docente1.pedir_libro():
#    print("Libro pedido con éxito.")
#else:
#    print("No se pudo pedir el libro.")
#print("Número de libros después de pedir: {}".format(docente1.obtener_numero_libros()))

# Devolver un libro
#print("Número de libros antes de devolver: {}".format(docente1.obtener_numero_libros()))
#docente1.devolver_libro()
#print("Número de libros después de devolver: {}".format(docente1.obtener_numero_libros()))

# Modificar el título de 3er nivel del docente
#print("Título de 3er nivel del docente antes de modificar: {}".format(docente1.obtener_titulo_3er_nivel()))
#docente1.modificar_titulo_3er_nivel("Ph.D. en Astronomía")
#print("Título de 3er nivel del docente después de modificar: {}".format(docente1.obtener_titulo_3er_nivel()))

# Modificar el título de 4to nivel del docente
#print("Título de 4to nivel del docente antes de modificar: {}".format(docente1.obtener_titulo_4to_nivel()))
#docente1.modificar_titulo_4to_nivel("Dr. en Ciencias Espaciales")
#print("Título de 4to nivel del docente después de modificar: {}".format(docente1.obtener_titulo_4to_nivel()))

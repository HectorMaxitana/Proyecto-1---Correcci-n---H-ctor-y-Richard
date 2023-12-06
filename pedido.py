from datetime import date


#Integrantes: Héctor Maxitana y Richard Constante


class pedido:
    contador_pedido = 0

    def __init__(self, id: int = None, solicitante: str = None, lista_material: str = None,
                 materia: str = None, fecha_prestamo: date = None, fecha_devolucion: date = None):
        pedido.contador_pedido += 1
        self.id = id
        self.solicitante = solicitante
        self.lista_material = lista_material
        self.materia = materia
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nuevo_id):
        self._id = nuevo_id

    @property
    def solicitante(self):
        return self._solicitante

    @solicitante.setter
    def solicitante(self, nuevo_solicitante):
        self._solicitante = nuevo_solicitante

    @property
    def lista_material(self):
        return self._lista_material

    @lista_material.setter
    def lista_material(self, nuevo_lista_material):
        self._lista_material = nuevo_lista_material

    @property
    def materia(self):
        return self._materia

    @materia.setter
    def materia(self, nuevo_materia):
        self._materia = nuevo_materia

    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @fecha_prestamo.setter
    def fecha_prestamo(self, nuevo_fecha_prestamo):
        self._fecha_prestamo = nuevo_fecha_prestamo

    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion

    @fecha_devolucion.setter
    def fecha_devolucion(self, nuevo_fecha_devolucion):
        self._fecha_devolucion = nuevo_fecha_devolucion

    def obtener_id(self):
        return self.id

    def obtener_lista_material(self):
        return self.lista_material

    def obtener_solicitante(self):
        return self.solicitante

    def obtener_materia(self):
        return self.materia

    def obtener_fecha_prestamo(self):
        return self.fecha_prestamo

    def obtener_fecha_devolucion(self):
        return self.fecha_devolucion

    def modificar_lista_material(self, nueva_lista_material):
        self.lista_material = nueva_lista_material

    def modificar_solicitante(self, nuevo_solicitante):
        self.solicitante = nuevo_solicitante

    def modificar_materia(self, nueva_materia):
        self.materia = nueva_materia

    def modificar_fecha_prestamo(self, nueva_fecha_prestamo):
        self.fecha_prestamo = nueva_fecha_prestamo

    def modificar_fecha_devolucion(self, nueva_fecha_devolucion):
        self.fecha_devolucion = nueva_fecha_devolucion

    def pedir_material(self, lista_material, solicitante, materia):
        self.lista_material = lista_material
        self.solicitante = solicitante
        self.materia = materia
        self.fecha_prestamo = date.today()

    def devolver_material(self):
        self.fecha_devolucion = date.today()
        self.solicitante.devolver_libro()
        return f"Material devuelto el {self.fecha_devolucion}"


# Crear instancias de libros, revistas, estudiantes, docentes, etc.
#libro1 = Libro(codigo="84723", autor="Autor1", titulo="Libro1", anio=2022, editorial="Editorial1", disponible=True,
#               cantidad_disponible=5, id=94694, tipo_pasta="Dura")

#revista1 = Revista(codigo="39484", autor="Autor2", titulo="Revista1", anio=2022, editorial="Editorial2",
#                   disponible=True, cantidad_disponible=10, id=16438, tipo="Científica")

#estudiante1 = Estudiante(cedula="0927366578", nombre="Shon", apellido="Murfi", email="e1@example.com",
#                         telefono="0973678392", direccion="Dirección1", numero_libros=2, activo=True,
#                         carrera="Carrera1", id=23845, nivel=2)

# Crear una instancia de Pedido
#pedido1 = Pedido(codigo="37749", autor="Autor3", titulo="El centro de la tierra", anio=2022, editorial="Editorial3",
#                 disponible=True, cantidad_disponible=3, id=28464, tipo_pasta="Suave",
#                 cedula="0927366578", nombre="Estudiante1", apellido="Apellido1", email="e1@example.com",
#                 telefono="0973678392", direccion="Dirección1", numero_libros=2, activo=True,
#                 carrera="Carrera1", nivel=4, solicitante="Estudiante1", lista_material="Libro1",
#                 materia="Materia1", fecha_prestamo=date.today(), titulo_3er_nivel="Cientifico",
#                 titulo_4to_nivel="Ingenniero", tipo="Científica")

# Realizar un pedido de material
#pedido1.pedir_material(lista_material=pedido1.titulo, solicitante=estudiante1, materia="Materia2")

# Pedir el material
#mensaje_devolucion = pedido1.devolver_material()

#print("Pedir el material:")
#print(f"Solicitante: {pedido1.obtener_solicitante().nombre} {pedido1.obtener_solicitante().apellido}")
#print(f"Material: {pedido1.obtener_lista_material()}")
#print(f"Fecha de préstamo: {pedido1.obtener_fecha_prestamo()}")

# Devolver el material

#print("\nDevolver el material:")
#print(f"Solicitante: {pedido1.obtener_solicitante().nombre} {pedido1.obtener_solicitante().apellido}")
#print(f"Material: {pedido1.obtener_lista_material()}")
#print(f"Fecha de devolución: {pedido1.obtener_fecha_devolucion()}")

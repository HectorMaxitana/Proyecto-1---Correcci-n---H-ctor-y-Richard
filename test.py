from libro import libro
from revista import revista
from estudiante import estudiante
from docente import docente
from pedido import pedido
from datetime import date


# Integrantes: Héctor Maxitana y Richard Constante


class test(libro, revista, estudiante, docente):

    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible, id,
                 tipo_pasta, tipo, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera,
                 nivel, titulo_3er_nivel, titulo_4to_nivel, solicitante: str = None, lista_material: str = None,
                 materia: str = None, fecha_prestamo: date = None, fecha_devolucion: date = None):
        libro.__init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible, id, tipo_pasta)
        revista.__init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible, id, tipo)
        estudiante.__init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera,
                            id, nivel)
        docente.__init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera, id,
                         titulo_3er_nivel, titulo_4to_nivel)
        pedido.__init__(self.id, solicitante, lista_material, materia, fecha_prestamo, fecha_devolucion)


# Crear instancias de libros, revistas, estudiantes, docentes, etc.
libro1 = libro(codigo="84723", autor="Autor1", titulo="Libro1", anio=2022, editorial="Editorial1", disponible=True,
               cantidad_disponible=5, id=94694, tipo_pasta="Dura")

revista1 = revista(codigo="39484", autor="Autor2", titulo="Revista1", anio=2022, editorial="Editorial2",
                   disponible=True, cantidad_disponible=10, id=16438, tipo="Científica")

estudiante1 = estudiante(cedula="0927366578", nombre="Shon", apellido="Murfi", email="e1@example.com",
                         telefono="0973678392", direccion="Dirección1", numero_libros=2, activo=True,
                         carrera="Carrera1", id=23845, nivel=2)

# Crear una instancia de Pedido
pedido1 = pedido(id=estudiante1.id, solicitante=estudiante1.nombre, lista_material="Libro1", materia="Materia1",
                 fecha_prestamo=date.today(), fecha_devolucion=date.today())

# Realizar un pedido de material
pedido1.pedir_material(lista_material=pedido1.lista_material, solicitante=estudiante1, materia="Materia2")
# Pedir el material
mensaje_devolucion = pedido1.devolver_material()

print("Pedir el material:")
print(f"Solicitante: {pedido1.obtener_solicitante().nombre} {pedido1.obtener_solicitante().apellido}")
print(f"Material: {pedido1.obtener_lista_material()}")
print(f"Fecha de préstamo: {pedido1.obtener_fecha_prestamo()}")

# Devolver el material

print("\nDevolver el material:")
print(f"Solicitante: {pedido1.obtener_solicitante().nombre} {pedido1.obtener_solicitante().apellido}")
print(f"Material: {pedido1.obtener_lista_material()}")
print(f"Fecha de devolución: {pedido1.obtener_fecha_devolucion()}")

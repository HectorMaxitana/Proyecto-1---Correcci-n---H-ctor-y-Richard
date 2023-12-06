from material import material


#Integrantes: Héctor Maxitana y Richard Constante


class libro(material):
    contador_libro = 0

    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible, id: int = None,
                 tipo_pasta: str = None):
        material.__init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible)
        libro.contador_libro += 1
        self.id = id
        self.tipo_pasta = tipo_pasta

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nueva_id):
        self._id = nueva_id

    @property
    def tipo_pasta(self):
        return self._tipo_pasta

    @tipo_pasta.setter
    def tipo_pasta(self, nueva_tipo_pasta):
        self._tipo_pasta = nueva_tipo_pasta

    def obtener_id(self):
        return self.id

    def obtener_tipo_pasta(self):
        return self.tipo_pasta

    def modificar_tipo_pasta(self, nuevo_tipo_pasta):
        self.tipo_pasta = nuevo_tipo_pasta

    def actualizar_disponibilidad(self, nueva_disponibilidad):
        self.modificar_disponible(nueva_disponibilidad)


#libro1 = Libro(codigo="84723", autor="Autor1", titulo="Libro1", anio=2022, editorial="Editorial1", disponible=True,
#               cantidad_disponible=5, id=94694, tipo_pasta="Dura")

# Imprimir información antes de actualizar la disponibilidad
#print("Antes de actualizar la disponibilidad:")
#print(f"ID: {libro1.obtener_id()}")
#print(f"Tipo de Pasta: {libro1.obtener_tipo_pasta()}")
#print(f"Disponible: {libro1.obtener_disponible()}")
#print(f"Cantidad Disponible: {libro1.obtener_cantidad_disponible()}")

# Actualizar disponibilidad
#libro1.actualizar_disponibilidad(False)

# Imprimir información después de actualizar la disponibilidad
#print("\nDespués de actualizar la disponibilidad:")
#print(f"ID: {libro1.obtener_id()}")
#print(f"Tipo de Pasta: {libro1.obtener_tipo_pasta()}")
#print(f"Disponible: {libro1.obtener_disponible()}")
#print(f"Cantidad Disponible: {libro1.obtener_cantidad_disponible()}")

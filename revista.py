from material import material


#Integrantes: Héctor Maxitana y Richard Constante


class revista(material):
    contador_revista = 0

    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible, id: int = None,
                 tipo: str = None):
        material.__init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible)
        revista.contador_revista += 1
        self.id = id
        self.tipo = tipo

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nueva_id):
        self._id = nueva_id

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo

    def obtener_id(self):
        return self.id

    def obtener_tipo(self):
        return self.tipo

    def modificar_tipo(self, nuevo_tipo):
        self.tipo = nuevo_tipo

    def actualizar_disponibilidad(self, nueva_disponibilidad):
        self.modificar_disponible(nueva_disponibilidad)


#revista1 = Revista(codigo="39484", autor="Autor2", titulo="Revista1", anio=2022, editorial="Editorial2",
#                   disponible=True, cantidad_disponible=10, id=16438, tipo="Científica")

# Imprimir información antes de actualizar la disponibilidad
#print("Antes de actualizar la disponibilidad:")
#print(f"ID: {revista1.obtener_id()}")
#print(f"Tipo: {revista1.obtener_tipo()}")
#print(f"Disponible: {revista1.obtener_disponible()}")
#print(f"Cantidad Disponible: {revista1.obtener_cantidad_disponible()}")

# Actualizar disponibilidad
#revista1.actualizar_disponibilidad(False)

# Imprimir información después de actualizar la disponibilidad
#print("\nDespués de actualizar la disponibilidad:")
#print(f"ID: {revista1.obtener_id()}")
#print(f"Tipo: {revista1.obtener_tipo()}")
#print(f"Disponible: {revista1.obtener_disponible()}")
#print(f"Cantidad Disponible: {revista1.obtener_cantidad_disponible()}")

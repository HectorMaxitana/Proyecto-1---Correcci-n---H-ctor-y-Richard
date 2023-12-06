from abc import ABC, abstractmethod


#Integrantes: Héctor Maxitana y Richard Constante


class material(ABC):
    def __init__(self, codigo: str = None, autor: str = None, titulo: str = None, anio: int = None,
                 editorial: str = None, disponible: bool = None, cantidad_disponible: int = None):
        self.codigo = codigo
        self.autor = autor
        self.titulo = titulo
        self.anio = anio
        self.editorial = editorial
        self.disponible = disponible
        self.cantidad_disponible = cantidad_disponible

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, nuevo_codigo):
        self._codigo = nuevo_codigo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, nuevo_autor):
        self._autor = nuevo_autor

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, nuevo_anio):
        self._anio = nuevo_anio

    @property
    def editorial(self):
        return self._editorial

    @editorial.setter
    def editorial(self, nuevo_editorial):
        self._editorial = nuevo_editorial

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, nuevo_estado):
        self._disponible = nuevo_estado

    @property
    def cantidad_disponible(self):
        return self._cantidad_disponible

    @cantidad_disponible.setter
    def cantidad_disponible(self, nueva_cantidad):
        self._cantidad_disponible = nueva_cantidad

    def obtener_codigo(self):
        return self.codigo

    def obtener_autor(self):
        return self.autor

    def obtener_titulo(self):
        return self.titulo

    def obtener_anio(self):
        return self.anio

    def obtener_editorial(self):
        return self.editorial

    def obtener_disponible(self):
        return self.disponible

    def obtener_cantidad_disponible(self):
        return self.cantidad_disponible

    def modificar_codigo(self, nuevo_codigo):
        self.codigo = nuevo_codigo

    def modificar_autor(self, nuevo_autor):
        self.autor = nuevo_autor

    def modificar_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def modificar_anio(self, nuevo_anio):
        self.anio = nuevo_anio

    def modificar_editorial(self, nueva_editorial):
        self.editorial = nueva_editorial

    def modificar_disponible(self, nueva_disponibilidad):
        self.disponible = nueva_disponibilidad

    def modificar_cantidad_disponible(self, nueva_cantidad):
        self.cantidad_disponible = nueva_cantidad

    @abstractmethod
    def actualizar_disponibilidad(self, nuevo_estado):
        pass

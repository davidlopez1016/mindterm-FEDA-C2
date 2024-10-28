class Contact:

    """
    Atributos:
    datos: Lista que contiene los valores de los atributos del contacto (nombre, apellido, organización, teléfono, dirección).
    
    Métodos:
    __init__: Inicializa el contacto con los atributos necesarios y los almacena en una lista.
    obtener_datos: Retorna la lista con los datos del contacto.

    """

    def __init__(self, nombre, apellido, organizacion, telefono, direccion):
       self.datos = [nombre, apellido, organizacion, telefono, direccion]
    
    def get_data(self):
        return self.datos
from .contact import Contact
class Directory:
    """
    Clase Directorio:

    Atributos:
    contactos: Matriz que contiene todos los contactos, incluyendo la primera fila como encabezado.

    Métodos:
    __init__: Inicializa la matriz contactos con la primera fila como encabezado de atributos.
    agregar_contacto: Agrega un nuevo contacto a la matriz.
    listar_contactos: Muestra todos los contactos en la matriz, incluyendo el encabezado.
    """

    def __init__(self):
        self.contactos = [["Nombre", "Apellido", "Organización", "Teléfono", "Dirección"]]

    def add_contact(self, nombre, apellido, organizacion, telefono, direccion):
        contacto = Contact(nombre, apellido, organizacion, telefono, direccion)
        self.contactos.append(contacto.get_data())

    def list_contacts(self):
        print("Directorio de Contactos:\n")
        for i, fila in enumerate(self.contactos):
            linea = "|"
            for item in fila:
                linea += f"{str(item):<14} | "
            print(linea)
            if i == 0:  
                print("|" + "_______________|_" * len(fila))
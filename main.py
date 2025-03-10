#Clase libro, con los atributos que conforman la información básica de un libro
class Libro:
  def __init__(self, nombre,autor,isbn, anno,editorial,disponibilidad):
    self.nombre = nombre
    self.autor = autor
    self.isbn = isbn
    self.anno = anno
    self.editorial = editorial
    self.disponibilidad = True

#Método para mostrar la información del libro
  def mostrar_info(self):
    print(f"Nombre: {self.nombre}\n Autor: {self.autor}\nEditorial: {self.editorial}\n")


#Método para actualizar la disponibilidad del libro  
  def disponible(self,disponibilidad):
    self.disponibilidad = disponibilidad
    if self.disponibilidad:
      estado = "Disponible"
    else:
      estado = "No disponible"
    print(f"Por ahora el libro {self.nombre} esta {estado} en la biblioteca")

class Usuario:
  def __init__(self, id_usuario, nombre, correo):
      self.id_usuario = id_usuario
      self.nombre = nombre  
      self.correo = correo
      self.libros_prestados = [] #Una lista para poder guardar más de un libro prestado

  def prestar_libro(self, libro):
    if libro.disponible: 
      self.libros_prestados.append(libro)
      libro.disponible = False
      print(f"Se le ha prestado al usuario {self.nombre} el libro {libro.nombre}")
    else:
      print(f"El libro {libro.nombre} no esta disponible")
  
  
  def devolver_libro(self, libro):
    if libro in self.libros_prestados:
      self.libros_prestados.remove(libro)
      print(f"El usuario {self.nombre} ha devuelto el libro {libro.nombre}")
      libro.disponible = True


class Bibliotecario:
  def __init__ (self,id_bibliotecario, nombre):
    self.id_bibliotecario = id_bibliotecario
    self.nombre = nombre

  def annadir_libro(self, biblioteca,libro):
    biblioteca.libros.append(libro)
    print(f"El libro {libro.nombre} ha sido añadido a la biblioteca")

  def eliminar_libro(self, biblioteca, libro):
    if libro in biblioteca.libros:
      biblioteca.libros.remove(libro)
      print(f"El libro {libro.nombre} ha sido eliminado de la biblioteca")

  def buscar_libro(self, biblioteca, titulo):
    for i in biblioteca.libros:   
      if i.nombre == titulo:
        print(f"El libro {i.nombre} de {i.autor} se encuentra en la biblioteca")
        break
      else:
        print(f"El libro {titulo} no se encuentra en la biblioteca")
        break





class Biblioteca:
  def __init__(self):
    self.libros = []
    self.usuarios = []
    self.bibliotecarios = []


  def registrar_usuarios(self, biblioteca,usuario):
    self.usuarios.append(usuario)
    print(f"El usuario {usuario.nombre} ha sido registrado en la biblioteca")

  def eliminar_usuario(self, biblioteca, usuario):
    if usuario in self.usuarios:
      self.usuarios.remove(usuario)
      print(f"El usuario {usuario.nombre} ha sido eliminado de la biblioteca")
    else:
      print(f"El usuario {usuario.nombre} no esta registrado en la biblioteca")


  def listar_usuarios(self, biblioteca):
    for usuario in self.usuarios:
      print(f"Nombre: {usuario.nombre}\nCorreo: {usuario.correo}\n")

  def listar_libros(self, biblioteca):
    for libro in self.libros:
      print(f"Nombre: {libro.nombre}\nAutor: {libro.autor}\nEditorial: {libro.editorial}\n")



#Creación de objetos
#Verificamos el funcionamiento de las clases

biblioteca1 = Biblioteca()
libro1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez","9780451524398",1967,"Editorial Sudamericana", True)
libro2 = Libro("1984", "George Orwell", "9783161484100",1949,"Editorial Seix Barral", True)

usuario1 = Usuario("001", "Juan Perez", "ejeyd@example.com")
usuario2 = Usuario("002", "Maria Lopez", "rdlnk@example.com")
bibliotecario1 = Bibliotecario("001", "Maria Rodriguez")


biblioteca1.listar_libros(biblioteca1)



bibliotecario1.annadir_libro(biblioteca1, libro1)
bibliotecario1.annadir_libro(biblioteca1, libro2)

print("\n")
biblioteca1.listar_libros(biblioteca1)
bibliotecario1.buscar_libro(biblioteca1, "Cien años de soledad")

bibliotecario1.eliminar_libro(biblioteca1, libro1)


libro1.mostrar_info()


biblioteca1.listar_usuarios(biblioteca1)

biblioteca1.registrar_usuarios(biblioteca1, usuario1)

biblioteca1.registrar_usuarios(biblioteca1, usuario2)

biblioteca1.listar_usuarios(biblioteca1)



usuario1.prestar_libro(libro1)
print("\n")
usuario2.prestar_libro(libro1)


usuario1.devolver_libro(libro1)
print("\n")
usuario2.prestar_libro(libro1)

biblioteca1.eliminar_usuario(biblioteca1, usuario1)
biblioteca1.eliminar_usuario(biblioteca1, usuario1)
biblioteca1.listar_usuarios(biblioteca1)
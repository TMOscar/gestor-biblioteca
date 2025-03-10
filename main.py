import datetime


#Clase libro, con los atributos que conforman la información básica de un libro
class Libro:

  def __init__(self, nombre, autor, isbn, anno, editorial):
    self.nombre = nombre
    self.autor = autor
    self.isbn = isbn
    self.anno = anno
    self.editorial = editorial
    self.disponibilidad = True

#Método para mostrar la información del libro

  def mostrar_info(self):
    print(
        f"Nombre: {self.nombre}\n Autor: {self.autor}\nEditorial: {self.editorial}\n"
    )

#Método para actualizar la disponibilidad del libro

  def disponible(self, estado):
    self.disponibilidad = estado
    if self.disponibilidad:
      estado = "Disponible"
    else:
      estado = "No disponible"
    print(f"Por ahora el libro {self.nombre} esta {estado} en la biblioteca")


#Clase usuario con los atributos que lo identifican
class Usuario:
  def __init__(self, id_usuario, nombre, correo):
    self.id_usuario = id_usuario
    self.nombre = nombre
    self.correo = correo
    self.libros_prestados = [
    ]  #Una lista para poder guardar más de un libro prestado



#Clase para identificar al bibliotecario, quien se encargara de añadir, eliminar y buscar libros
class Bibliotecario:

  def __init__(self, id_bibliotecario, nombre):
    self.id_bibliotecario = id_bibliotecario
    self.nombre = nombre

  def annadir_libro(self, biblioteca, libro):
    biblioteca.libros.append(libro)
    print(f"El libro {libro.nombre} ha sido añadido a la biblioteca")

  def eliminar_libro(self, biblioteca, libro):
    if libro in biblioteca.libros:
      biblioteca.libros.remove(libro)
      print(f"El libro {libro.nombre} ha sido eliminado de la biblioteca")

  def buscar_libro(self, biblioteca, titulo):
    for i in biblioteca.libros:
      if i.nombre.lower() == titulo.lower():
        print(
            f"El libro {i.nombre} de {i.autor} se encuentra en la biblioteca")
        return i
       
      
    print(f"El libro {titulo} no se encuentra en la biblioteca")
      


#Clase biblioteca, que sera la clase que guarde el repertorio de libros, registro de usuarios, aliminacion y listado de los mismos
class Biblioteca:

  def __init__(self):
    self.libros = []
    self.usuarios = []
    self.prestamos = []

  def registrar_usuarios(self,  usuario):
    self.usuarios.append(usuario)
    print(f"El usuario {usuario.nombre} ha sido registrado en la biblioteca")

  def eliminar_usuario(self, usuario):
    if usuario in self.usuarios:
      self.usuarios.remove(usuario)
      print(f"El usuario {usuario.nombre} ha sido eliminado de la biblioteca")
    else:
      print(f"El usuario {usuario.nombre} no esta registrado en la biblioteca")

  def listar_usuarios(self):
    for usuario in self.usuarios:
      print(f"Nombre: {usuario.nombre}\nCorreo: {usuario.correo}\n")

  def listar_libros(self):
    for libro in self.libros:
      print(
          f"Nombre: {libro.nombre}\nAutor: {libro.autor}\nEditorial: {libro.editorial}\n"
      )


#Clase prestamo, que sera la clase que guarde los prestamos de los usuarios para mantener un registro de los mismos
class Prestamo:

  def __init__(self):
    self.fecha_prestamo = 0
    self.fecha_devolucion = 0


  
  def prestar_libro(self, usuario, libro):
    if libro.disponibilidad:
      libro.disponible(False)
      usuario.libros_prestados.append(libro)
      self.fecha_prestamo = datetime.datetime.now()
      self.fecha_devolucion = datetime.datetime.now() + datetime.timedelta(days=7)
      print(f"El libro {libro.nombre} ha sido prestado al usuario {usuario.nombre} el día {self.fecha_prestamo}, se espera su devolución antes del día {self.fecha_devolucion}")
    else:
      print(f"El libro {libro.nombre} no esta disponible para prestar")
  

  def devolver_libro(self, usuario,libro):
    if libro in usuario.libros_prestados:
      usuario.libros_prestados.remove(libro)
      libro.disponible(True)
      print(f"El usuario {usuario.nombre} ha devuelto el libro {libro.nombre} el día {self.fecha_devolucion}")


  def info_prestamo(self, usuario):
    if usuario.libros_prestados:
      print(f"Usuario: {usuario.nombre} tienes los siguientes libros prestados:\n")
      for libro in usuario.libros_prestados:
        libro.mostrar_info()
    else:
      print(f"El usuario {usuario.nombre} no tiene libros prestados")



#######################################################################################
#Pruebas de ejecución

# Crear instancias de libros
libro1 = Libro("Python para principiantes", "Juan Pérez", "123456789", 2022, "Editorial ABC")
libro2 = Libro("Aprendiendo Django", "Ana Gómez", "987654321", 2021, "Editorial XYZ")

# Crear instancia de un usuario
usuario1 = Usuario(1, "Carlos Sánchez", "carlos.sanchez@example.com")
usuario2 = Usuario(2, "Laura García", "laura.garcia@example.com")

# Crear instancia de bibliotecario
bibliotecario = Bibliotecario(1, "Elena Martínez")

# Crear instancia de biblioteca
biblioteca = Biblioteca()

# Registrar usuarios en la biblioteca
print("\nProbando el registro de usuarios:")
biblioteca.registrar_usuarios(usuario1)
biblioteca.registrar_usuarios(usuario2)

# Añadir libros a la biblioteca
print("\nProbando la inserción de libros a la biblioteca:")
bibliotecario.annadir_libro(biblioteca, libro1)
bibliotecario.annadir_libro(biblioteca, libro2)

# Listar libros disponibles en la biblioteca
print("\nProbando la lista de libros disponibles en la biblioteca:")
biblioteca.listar_libros()

# Listar usuarios registrados
print("\nProbando la lista de usuarios registrados:")
biblioteca.listar_usuarios()

# Crear instancia de préstamo
prestamo = Prestamo()

# Prestar libros a los usuarios
print("\nProbando el préstamo de libros:")
prestamo.prestar_libro(usuario1, libro1)  # Prestar "Python para principiantes" a usuario1
print()
print()
prestamo.prestar_libro(usuario2, libro2)  # Prestar "Aprendiendo Django" a usuario2
print()
print()
prestamo.prestar_libro(usuario1, libro2)


# Ver información de los libros prestados por usuario1
print("\nProbando la visualización de los libros prestados por el usuario 1:")
prestamo.info_prestamo(usuario1)
print()
print()
# Ver información de los libros prestados por usuario2
print("\nProbando la visualización de los libros prestados por el usuario 2:")
prestamo.info_prestamo(usuario2)

# Devolver libros
print("\nProbando la devolución de libros:")
prestamo.devolver_libro(usuario1, libro1)  # Devolver "Python para principiantes"
print()
print()
prestamo.devolver_libro(usuario2, libro2)  # Devolver "Aprendiendo Django"
print()
print()
# Ver información después de la devolución
print("\nProbando la visualización de los libros prestados después de la devolución:")
prestamo.info_prestamo(usuario1)
prestamo.info_prestamo(usuario2)

# Listar libros después de las devoluciones
print("\nProbando la lista de libros disponibles después de la devolución:")
biblioteca.listar_libros()

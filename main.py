import datetime
import os


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
    print(f"\nPor ahora el libro {self.nombre} se encuentra {estado} en la biblioteca\n")


#Clase usuario con los atributos que lo identifican
class Usuario:

  def __init__(self, nombre, correo):
    self.nombre = nombre
    self.correo = correo
    self.libros_prestados = [
    ]  #Una lista para poder guardar más de un libro prestado


#Clase para identificar al bibliotecario, quien se encargara de añadir, eliminar y buscar libros
class Bibliotecario:

  def __init__(self, nombre):
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
        print(f"El libro {i.nombre} de {i.autor} se encuentra en la biblioteca")
        return i

    print(f"El libro {titulo} no se encuentra en la biblioteca")


#Clase biblioteca, que sera la clase que guarde el repertorio de libros, registro de usuarios, aliminacion y listado de los mismos
class Biblioteca:

  def __init__(self):
    self.libros = []
    self.usuarios = []
    self.prestamos = []

  def registrar_usuarios(self, usuario):
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
      self.fecha_devolucion = datetime.datetime.now() + datetime.timedelta(
          days=7)
      print(
          f"El libro {libro.nombre} ha sido prestado al usuario {usuario.nombre} el día {self.fecha_prestamo}, se espera su devolución antes del día {self.fecha_devolucion}"
      )
    else:
      print(f"El libro {libro.nombre} no esta disponible para prestar")

  def devolver_libro(self, usuario, libro):
    if libro in usuario.libros_prestados:
      usuario.libros_prestados.remove(libro)
      libro.disponible(True)
      print(
          f"El usuario {usuario.nombre} ha devuelto el libro {libro.nombre} el día {self.fecha_devolucion}"
      )

  def info_prestamo(self, usuario):
    if usuario.libros_prestados:
      print(
          f"Usuario: {usuario.nombre} tienes los siguientes libros prestados:\n"
      )
      for libro in usuario.libros_prestados:
        libro.mostrar_info()
    else:
      print(f"El usuario {usuario.nombre} no tiene libros prestados")


def limpiar_pantalla():
  os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_menu():
  print("\n--- MENÚ PRINCIPAL ---")
  print("1. Registrar Usuario")
  print("2. Eliminar Usuario")
  print("3. Listar Usuarios")
  print("4. Añadir Libro")
  print("5. Eliminar Libro")
  print("6. Listar Libros")
  print("7. Buscar Libro")
  print("8. Prestar Libro")
  print("9. Devolver Libro")
  print("10. Ver Préstamos de un usuario")
  print("0. Salir")
  print("-----------------------")


def ejecutar_menu(biblioteca, prestamo,bibliotecario):
  while True:
    mostrar_menu()
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
      limpiar_pantalla()
      nombre = input("Ingresa el nombre del usuario: ")
      correo = input("Ingresa el correo del usuario: ")
      usuario_nuevo = Usuario(nombre, correo)
      biblioteca.registrar_usuarios(usuario_nuevo)

    

    elif opcion == 2:
      limpiar_pantalla()
      nombre = input("Ingresa el nombre del usuario a eliminar: ")
      usuario_eliminar = None

      #Se busca el usuario en la lista de usuarios por el nombre
      for usuario in biblioteca.usuarios:
        if usuario.nombre == nombre:
          usuario_eliminar = usuario  #Si se encuentra el usuario se guarda en la variable usuario_eliminar
          break

      #Si el usuario existe se elimina de la lista de usuarios, en caso contrario que no se haya encontrado el usuario en le for
      #se muestra un mensaje de error
      if usuario_eliminar:
        biblioteca.eliminar_usuario(usuario_eliminar)
      else:
        print("El usuario no existe en la biblioteca")

    elif opcion == 3:
      limpiar_pantalla()
      biblioteca.listar_usuarios()

    elif opcion == 4:
      limpiar_pantalla()
      nombre = input("Ingresa el nombre del libro: ")
      autor = input("Ingresa el autor del libro: ")
      #Para el ISBN verificamos que la entrada sea de un tamaño de 13 caracteres
      isbn = input("Ingresa el ISBN del libro: ")
      if len(isbn) != 13:
        print("El ISBN debe tener 13 dígitos")
        continue

      #De igual manera verificamos que el año sea de 4 dígitos
      anno = input("Ingresa el año de publicación del libro: ")
      if len(anno) != 4:
        print("El año debe tener 4 dígitos")
        continue

      editorial = input("Ingresa la editorial del libro: ")
      libro_nuevo = Libro(nombre, autor, isbn, anno, editorial)
      bibliotecario.annadir_libro(biblioteca, libro_nuevo)

    elif opcion == 5:
      limpiar_pantalla()
      nombre = input("Ingresa el nombre del libro a eliminar: ")
      libro_eliminar = None

      #Se busca el libro en la lista de libros por el nombre
      for libro in biblioteca.libros:
        if libro.nombre == nombre:
          libro_eliminar = libro  #Si se encuentra el libro se guarda en la variable libro_eliminar
          break

      if libro_eliminar:
        biblioteca.eliminar_libro(libro_eliminar)

      else:
        print("El libro no existe en la biblioteca")

    elif opcion == 6:
      limpiar_pantalla()
      biblioteca.listar_libros() 


    elif opcion == 7:
      limpiar_pantalla()
      titulo = input("Ingresa el título del libro a buscar: ")
      bibliotecario.buscar_libro(biblioteca,titulo)

    elif opcion == 8:
      limpiar_pantalla()
      nombre = input("Ingresa el nombre del usuario: ")
      usuario_prestamo = None

      #Se busca el usuario en la lista de usuarios por el nombre
      for usuario in biblioteca.usuarios:
        if usuario.nombre == nombre:
          usuario_prestamo = usuario  #Si se encuentra el usuario se guarda en la variable usuario_prestamo
          break  

      #Si el usuario existe se presta el libro, verificamos tambien la existencia del libro, si ambos son verdaderos se presta el libro
      if usuario_prestamo:
        libro = input("Ingresa el nombre del libro a prestar: ")
        print("\n")
        if bibliotecario.buscar_libro(biblioteca,libro):
          prestamo.prestar_libro(usuario_prestamo, bibliotecario.buscar_libro(biblioteca,libro))
        else:
          print(f"El libro {libro} no existe en la biblioteca")


    elif opcion == 9:
      limpiar_pantalla()
      nombre = input("Ingresa el nombre del usuario: ")
      usuario_devolucion = None
      #Se busca el usuario en la lista de usuarios por el nombre
      for usuario in biblioteca.usuarios:
        if usuario.nombre == nombre:
          usuario_devolucion = usuario  #Si se encuentra el usuario se guarda en la variable usuario_devolucion
          break
      #Si el usuario existe se devuelve el libro
      libro = input("Ingresa el nombre del libro a devolver: ")
      print("\n")
      if bibliotecario.buscar_libro(biblioteca,libro):
        prestamo.devolver_libro(usuario_devolucion, bibliotecario.buscar_libro(biblioteca,libro))


    elif opcion == 10:
      limpiar_pantalla()
      nombre = input("Ingresa el nombre del usuario: ")
      usuario_prestamo = None
      # Buscar usuario en la lista de usuarios
      for usuario in biblioteca.usuarios:
          if usuario.nombre == nombre:
              usuario_prestamo = usuario  # Se guarda el objeto usuario
              break  # Se detiene la búsqueda al encontrar el usuario

      # Mostrar información si el usuario existe
      if usuario_prestamo:
          prestamo.info_prestamo(usuario_prestamo)
      else:
          print(f"El usuario {nombre} no existe en la biblioteca")


    elif opcion == 0 :
      print("¡Hasta luego!")
      break
    else:
      print("Opción no válida, por favor elige una opción entre 0 y 10.")


def main():
  biblioteca = Biblioteca()
  prestamo = Prestamo()
  bibliotecario = Bibliotecario("Maure TM")
  ejecutar_menu(biblioteca, prestamo, bibliotecario)


if __name__ == "__main__":
  main()

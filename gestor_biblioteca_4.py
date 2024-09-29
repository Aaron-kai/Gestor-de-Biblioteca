class Libro:
    def __init__(self, isbn, titulo, autor, año, estado='disponible'):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.estado = estado

class Persona:
    def __init__(self, nombre, apellido, telefono, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.dni = dni

class Cliente(Persona):
    def __init__(self, codigoCliente, nombre, apellido, telefono, dni, libros_prestados = 0):
        super().__init__(nombre, apellido, telefono, dni)
        self.codigoCliente = codigoCliente
        self.libros_prestados = libros_prestados

class Prestamo:
    def __init__(self, idPrestamo, isbn, codigoCliente, fechaPrestamo, diasPrestamo):
        self.idPrestamo = idPrestamo
        self.isbn = isbn
        self.codigoCliente = codigoCliente
        self.fechaPrestamo = fechaPrestamo
        self.diasPrestamo = diasPrestamo
        self.estado = 'disponible'

class gestion_libros:
    def __init__(self):
        self.libros = []
        self.cant_libros_prestados = 0

    def nuevo_libro(self, isbn, titulo, autor, año):
        libro = Libro(isbn, titulo, autor, año)
        self.libros.append(libro)

    def listar_libros(self):
        for libro_mostrar in self.libros:
            print(f"\nISBN : {libro_mostrar.isbn} \nTitulo: {libro_mostrar.titulo} \nAutor: {libro_mostrar.autor} \nAño : {libro_mostrar.año} \nEstado : {libro_mostrar.estado}")
            #print(vars(libro_mostrar))
    
    def modificar_libros(self, isbn_libro):
        for libros_existentes in self.libros:
            if isbn_libro == libros_existentes.isbn:
                while True:
                    print("""======================
Modificar libro
======================
[1] isbn
[2] titulo
[3] Autor
[5] Año
[#] cerrar""")
                    modificacion_libro = input('Ingresar una opcion : ')

                    if modificacion_libro == '1':
                        nueva_modificacion = input('Ingresar el nuevo isbn : ')
                        libros_existentes.isbn = nueva_modificacion
                        print('Se ha modificado el ISBN del libro')

                    elif modificacion_libro == '2':
                        nueva_modificacion = input('Ingresar el nuevo titulo : ')
                        libros_existentes.titulo = nueva_modificacion
                        print('Se ha modificado el titulo del libro')

                    elif modificacion_libro == '3':
                        nueva_modificacion = input('Ingresar el nuevo titulo autor: ')
                        libros_existentes.autor = nueva_modificacion
                        print('Se ha modificado el autor del libro')

                    elif modificacion_libro == '5':
                        nueva_modificacion = input('Ingresar el nuevo titulo año: ')
                        libros_existentes.año = nueva_modificacion
                        print('Se ha modificado el año del libro')

                    elif modificacion_libro == '#':
                        break

                    else:
                        input('Opcion inexistente : ')

    def buscar_libro_isbn(self, buscar_libro):
        for libro_Existente in self.libros:
            if buscar_libro == libro_Existente.isbn:
                return True
        return False
    
    def cambio_estado_libro(self, buscar_libro, nuevo_estado):
        for libro_Existente in self.libros:
            if buscar_libro == libro_Existente.isbn:
                libro_Existente.estado = nuevo_estado

    def libros_prestados(self):
        for libro_prestado in self.libros:
            if libro_prestado.estado == 'Prestado':
                print(f"\nISBN : {libro_prestado.isbn} \nTitulo: {libro_prestado.titulo} \nAutor: {libro_prestado.autor} \nAño : {libro_prestado.año} \nEstado : {libro_prestado.estado}")

    def libros_disponibles(self):
        for libro_disponible in self.libros:
            if libro_disponible.estado == 'disponible':
                print(f"\nISBN : {libro_disponible.isbn} \nTitulo: {libro_disponible.titulo} \nAutor: {libro_disponible.autor} \nAño : {libro_disponible.año} \nEstado : {libro_disponible.estado}")

    #def devolver_estado_libro(self, isbn_libro):
    #    for buscar_libro in self.libros:
    #        if buscar_libro == isbn_libro:
    #            return buscar_libro.estado

    def verificar_estado_libro(self, isbn_libro):
        if self.buscar_libro_isbn(isbn_libro):
            for estado_libro in self.libros:
                if estado_libro.isbn == isbn_libro:
                    if estado_libro.estado == "Prestado":
                        return False
            return True

    #def Eliminar_un_libro(self, libro_eliminado):
    #    for eliminar_libro in self.libros:
    #        if libro_eliminado == eliminar_libro.isbn:
    #            self.libros.remove(eliminar_libro)
    #            print('Se ha eliminado el libro exitosamente')

    def Eliminar_un_libro(self, isbn_libro_delete):
        for eliminar_libro in self.libros:
            if self.verificar_estado_libro(isbn_libro_delete):
                if isbn_libro_delete == eliminar_libro.isbn:
                    self.libros.remove(eliminar_libro)
                    return True
        return False

class gestion_clientes:

    def __init__(self) :
        self.clients = []
        self.cliente_frecuente_list = []

    def agregar_clientes(self, codigoCliente, nombre, apellido, telefono, dni):
        nuevo_cliente = Cliente(codigoCliente, nombre, apellido, telefono, dni)
        self.clients.append(nuevo_cliente)

    def mostrar_clientes(self):
        for cliente in self.clients:
            print(f'\nCodigo Cliente : {cliente.codigoCliente} \nnombre : {cliente.nombre} \napellido : {cliente.apellido} \ntelefono : {cliente.telefono} \nDNI : {cliente.dni} \nLibros_prestados : {cliente.libros_prestados}')

    def buscar_cliente(self, code_client):
        for cliente_encontrar in self.clients:
            if code_client == cliente_encontrar.codigoCliente:
                return True
        return False
    
    def aumento_libros_prestados(self, codigo_cliente):
        for buscar_client in self.clients:
            if codigo_cliente == buscar_client.codigoCliente:
                buscar_client.libros_prestados += 1    
    
    def cliente_frecuente(self, codigo_cliente):
        for cliente_registrado in self.clients:
            if codigo_cliente == cliente_registrado.codigoCliente:
                self.aumento_libros_prestados(codigo_cliente)
                if cliente_registrado.libros_prestados >= 2:
                    self.cliente_frecuente_list.append(cliente_registrado)

    def lista_de_clientes_frecuentes(self):
        for cliente_frecuente in self.cliente_frecuente_list:
            print(f'\nCodigo Cliente : {cliente_frecuente.codigoCliente} \nnombre : {cliente_frecuente.nombre} \napellido : {cliente_frecuente.apellido} \ntelefono : {cliente_frecuente.telefono} \nDNI : {cliente_frecuente.dni} \nLibros_prestados : {cliente_frecuente.libros_prestados}')

    #def longitud_clientes_frecuentes(self):
    #    return len(self.cliente_frecuente_list)



class prestamos_devoluciones():
    def __init__(self, gestorCliente, gestorLibros):
        self.gestorCliente = gestorCliente
        self.gestorLibros = gestorLibros
        self.librosPrestados = []
    
    def prestar_libro(self, CODcliente):
        client = self.gestorCliente.buscar_cliente(CODcliente)
        if client:
            code_libro = input("Ingresar el isbn del libro : ")
            verificar_libro = self.gestorLibros.buscar_libro_isbn(code_libro)
            if verificar_libro:
                if gestor_libros.verificar_estado_libro(code_libro):
                    idPrestamo = len(self.librosPrestados) + 1
                    fechaPrestamo = input('Ingresar la fecha del prestamo : ')
                    diasPrestamo = input('Ingresar dias de prestamo : ')
                    prestamoRealizado = Prestamo(idPrestamo, code_libro, CODcliente, fechaPrestamo, diasPrestamo)
                    self.gestorLibros.cambio_estado_libro(code_libro, nuevo_estado = 'Prestado')
                    self.gestorCliente.cliente_frecuente(CODcliente)
                    self.librosPrestados.append(prestamoRealizado)
                    self.gestorLibros.cant_libros_prestados += 1
                    return True
                else:
                    print("El libro ya ha sido prestado")
            else:
                print("El libro no se ha encontrado")
        else:
            print("Cliente no encontrado")

    def mostrar_prestamos_realizados(self):
        for lista_prestamos in self.librosPrestados:
            print(vars(lista_prestamos))

    def Devolver_libro(self, CODcliente):

        client = self.gestorCliente.buscar_cliente(CODcliente)
        if client:
            code_libro = input("Ingresar el isbn del libro : ")
            verificar_libro = self.gestorLibros.buscar_libro_isbn(code_libro)
            if verificar_libro:
                for verificacion_prestamo in self.librosPrestados:
                    if CODcliente == verificacion_prestamo.codigoCliente:
                        self.gestorLibros.cambio_estado_libro(code_libro, nuevo_estado = 'disponible')
                        self.gestorLibros.cant_libros_prestados -= 1
                        return True

            else:
                print("El libro no se ha encontrado")
        else:
            print("Cliente no encontrado")

class Generacion_de_reportes():
    def __init__(self, gestor_cliente, gestor_libro):
        self.gestor_cliente = gestor_cliente
        self.gestor_libro = gestor_libro

    def lista_libros_prestados(self):
        gestor_libros.libros_prestados()

    def clientes_frecuentes(self):
        gestor_cliente.lista_de_clientes_frecuentes()

    def lista_libros_disponibles(self):
        gestor_libros.libros_disponibles()

    def longitud_clientes_F(self):
        return len(gestor_cliente.cliente_frecuente_list)

    def longitud_libros_prestados(self):
        return gestor_libros.cant_libros_prestados
        



#############################################################
#                 Inicio del programa                       #
#############################################################
        
gestor_libros = gestion_libros()
gestor_cliente = gestion_clientes()
pres_del_libros = prestamos_devoluciones(gestor_cliente, gestor_libros)
generacion_reportes = Generacion_de_reportes(gestor_cliente, gestor_libros)

gestor_libros.nuevo_libro('5555', 'Jujutsu Kaisen', 'Gege Akutami', '2016')
gestor_libros.nuevo_libro('1919', 'Shingeki no kyojin', 'Hajime Isayama', '2009')
gestor_libros.nuevo_libro('1111', 'chainsaw man', 'Fujimoto', '2018')
gestor_libros.nuevo_libro('1212', 'looc back', 'Fujimoto', '2022')

gestor_cliente.agregar_clientes('2323', 'Yugi', 'Itadori', '923923923', '292929')
gestor_cliente.agregar_clientes('1221', 'Kosei', 'Gege', '953232333', '199291')
gestor_cliente.agregar_clientes('9991', 'Nobara', 'Kugisaki', '979732992', '772233')
gestor_cliente.agregar_clientes('1112', 'Gojo', 'Satoru', '931213221', '723272')

while True:

    print("""\n===========================
Biblioteca Pochita
===========================
[1] Gestion de libros
[2] Gestion de clientes
[3] Prestamos y devoluciones
[5] Generacion de reportes
[#] Salir
===========================""")

    opcion_menu = input('Ingresa una opcion del menu : ')

    if opcion_menu == '1':

        while True:
            print("""\n============================
Gestor de libros  
============================
[1] Agregar un nuevo libro
[2] Mostrar lista de libros
[3] Modificar un libro
[5] Eliminar libros
[#] Salir
============================""")
            opcion_gestor_libros = input('Ingresa una opcion del menu : ')

            if opcion_gestor_libros == '1':
                new_isbn = input('Ingresa el isbn del libro : ')
                if not gestor_libros.buscar_libro_isbn(new_isbn):
                    new_titulo = input('Ingresa el titulo del libro : ')
                    new_autor = input('Ingresa el autor del libro : ')
                    new_año = input('Ingresa el año del libro : ')
                    confirmado = gestor_libros.nuevo_libro(new_isbn, new_titulo, new_autor, new_año)
                    print('El libro se ha agregado correctamente')
                else:
                    print(f"El libro con el isbn {new_isbn} ya esta registrado")

            elif opcion_gestor_libros == '2':
                gestor_libros.listar_libros()

            elif opcion_gestor_libros == '3':
                isbn_del_libro = input('Ingresar el isbn del libro : ')

                if gestor_libros.verificar_estado_libro(isbn_del_libro):
                    gestor_libros.modificar_libros(isbn_del_libro)
                else:
                    print("El libro fue prestado o no existe")

            elif opcion_gestor_libros == '5':
                isbn_libro_eliminar =  input('Ingresar el isbn del libro : ')
                if gestor_libros.Eliminar_un_libro(isbn_libro_eliminar):
                    print("El libro ha sido eliminado correctamente")
                else:
                    print("El libro esta prestado o no existe")

            elif opcion_gestor_libros == '#':
                break
            else:
                print('Opcion inexsistente')
        
    elif opcion_menu == '2':
        while True:
            print("""\n============================
Gestor de Clientes  
============================
[1] Agregar un nuevo cliente
[2] Mostrar lista de clientes
[#] Salir
============================""")
            opcion_Gestor_cliente = input('Ingresa una opcion del menu : ')

            if opcion_Gestor_cliente == '1':
                C_cliente = input('Ingresar el codigo del cliente : ')
                if not gestor_cliente.buscar_cliente(C_cliente):
                    nombre_cliente = input('Ingresar el nombre del cliente : ')
                    apellido_cliente = input('Ingresar el apellido del cliente : ')
                    telefono_cliente = input('Ingresar el telefono del cliente : ')
                    dni_cliente = input('Ingresar el dni del cliente : ')
                    gestor_cliente.agregar_clientes(C_cliente, nombre_cliente, apellido_cliente, telefono_cliente, dni_cliente)
                    print('Se ha ingresado un nuevo cliente exitosamente')
                else:
                    print(f"ya hay un cliente registrado con el codigo {C_cliente}")

            elif opcion_Gestor_cliente == '2':
                gestor_cliente.mostrar_clientes()

            elif opcion_Gestor_cliente == '#':
                break
            else:
                print('Opcion inexsistente')

    elif opcion_menu == '3':
        while True:
            print("""\n============================
Prestamos y devoluciones  
============================
[1] Prestar un libro
[2] Devolver un libro
[#] Salir
============================""")
            
            opcion_prestamos_devoluciones = input('Ingresa una opcion del menu : ')

            if opcion_prestamos_devoluciones == '1':
                codigo_client = input("Ingresar el codigo del cliente : ")
                if pres_del_libros.prestar_libro(codigo_client):
                #gestor_cliente.cliente_frecuente(codigo_client)
                    print('El prestamo del libro se ha realizado correctamente')

            elif opcion_prestamos_devoluciones == '2':
                codigo_client = input("Ingresar el codigo del cliente : ")
                if pres_del_libros.Devolver_libro(codigo_client):
                    print("Se ha devuelto el libro exitosamente")

            elif opcion_prestamos_devoluciones == '#':
                break
            else:
                print('Opcion inexsistente')
                
    elif opcion_menu == '5':
        while True:
            print("""\n============================
Generacion de reportes  
============================
[1] Informes de libros prestados
[2] Clientes frecuentes
[3] Libros disponibles
[#] Salir
============================""")
            
            opcion_reportes = input('Ingresa una opcion del menu : ')

            if opcion_reportes == '1':
                if  generacion_reportes.longitud_libros_prestados() == 0:
                    print("No se han prestado libros")
                else:
                    generacion_reportes.lista_libros_prestados()

            elif opcion_reportes == '2':
                if generacion_reportes.longitud_clientes_F() == 0:
                    print("No hay clientes registrados como frecuentes")
                else:
                    generacion_reportes.clientes_frecuentes()

            elif opcion_reportes == '3':
                generacion_reportes.lista_libros_disponibles()

            elif opcion_reportes == '#':
                break
            else:
                print('Opcion inexsistente')
    elif opcion_menu == '#':
        break
    else:
        print('Opcion inexistente')

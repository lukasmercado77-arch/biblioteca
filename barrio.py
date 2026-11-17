"""
biblioteca del barrio (programa de consola).

Permite registrar libros y usuarios, prestar y devolver libros,
renovar prestamos y calcular / cobrar multas por retraso.
Todos los datos viven en listas y diccionarios dentro del programa.
"""

from datetime import date, timedelta  # solo para calcular fechas de prestamo


# -----------Configuracion de la biblioteca.-----------------

DIAS_PRESTAMO = 7        # dias que dura un prestamo.
MULTA_POR_DIA = 1000     # pesos por cada dia de retraso.
MAX_PRESTAMOS = 3        # libros que un usuario puede tener a la vez.
MAX_RENOVACIONES = 1     # veces que se puede renovar un prestamo.
MAX_TEXTO = 100          # largo maximo de cualquier texto escrito.

# --------Listas principales: cada elemento es un diccionario.-----------

lista_libros = []
lista_usuarios = []
lista_prestamos = []

# ----------Libros que trae la biblioteca al abrir el programa: (codigo, titulo, autor).--------

LIBROS_INICIALES = [
    ("001", "El principito", "Antoine de Saint-Exupéry"),
    ("002", "1984", "George Orwell"),
    ("003", "Matar a un ruiseñor", "Harper Lee"),
    ("004", "Orgullo y prejuicio", "Jane Austen"),
    ("005", "El gran Gatsby", "F. Scott Fitzgerald"),
    ("006", "Cien años de soledad", "Gabriel García Márquez"),
    ("007", "El amor en los tiempos del cólera", "Gabriel García Márquez"),
    ("008", "Don Quijote de la Mancha", "Miguel de Cervantes"),
    ("009", "La vorágine", "José Eustasio Rivera"),
    ("010", "María", "Jorge Isaacs"),
    ("011", "Crónica de una muerte anunciada", "Gabriel García Márquez"),
    ("012", "El coronel no tiene quien le escriba", "Gabriel García Márquez"),
    ("013", "La casa de los espíritus", "Isabel Allende"),
    ("014", "Rayuela", "Julio Cortázar"),
    ("015", "Ficciones", "Jorge Luis Borges"),
    ("016", "El túnel", "Ernesto Sabato"),
    ("017", "Pedro Páramo", "Juan Rulfo"),
    ("018", "La ciudad y los perros", "Mario Vargas Llosa"),
    ("019", "Los juegos del hambre", "Suzanne Collins"),
    ("020", "Harry Potter y la piedra filosofal", "J. K. Rowling"),
    ("021", "Harry Potter y la cámara secreta", "J. K. Rowling"),
    ("022", "Harry Potter y el prisionero de Azkaban", "J. K. Rowling"),
    ("023", "El señor de los anillos", "J. R. R. Tolkien"),
    ("024", "El hobbit", "J. R. R. Tolkien"),
    ("025", "Las crónicas de Narnia", "C. S. Lewis"),
    ("026", "Alicia en el país de las maravillas", "Lewis Carroll"),
    ("027", "Peter Pan", "J. M. Barrie"),
    ("028", "La isla del tesoro", "Robert Louis Stevenson"),
    ("029", "Robinson Crusoe", "Daniel Defoe"),
    ("030", "Viaje al centro de la Tierra", "Julio Verne"),
    ("031", "Veinte mil leguas de viaje submarino", "Julio Verne"),
    ("032", "La vuelta al mundo en ochenta días", "Julio Verne"),
    ("033", "Frankenstein", "Mary Shelley"),
    ("034", "Drácula", "Bram Stoker"),
    ("035", "El extraño caso del doctor Jekyll y el señor Hyde", "Robert Louis Stevenson"),
    ("036", "El retrato de Dorian Gray", "Oscar Wilde"),
    ("037", "Los miserables", "Victor Hugo"),
    ("038", "Nuestra señora de París", "Victor Hugo"),
    ("039", "Crimen y castigo", "Fiódor Dostoyevski"),
    ("040", "Los hermanos Karamázov", "Fiódor Dostoyevski"),
    ("041", "Guerra y paz", "León Tolstói"),
    ("042", "Ana Karenina", "León Tolstói"),
    ("043", "La metamorfosis", "Franz Kafka"),
    ("044", "El proceso", "Franz Kafka"),
    ("045", "El viejo y el mar", "Ernest Hemingway"),
    ("046", "Por quién doblan las campanas", "Ernest Hemingway"),
    ("047", "Moby Dick", "Herman Melville"),
    ("048", "Las aventuras de Tom Sawyer", "Mark Twain"),
    ("049", "Las aventuras de Huckleberry Finn", "Mark Twain"),
    ("050", "Mujercitas", "Louisa May Alcott"),
    ("051", "Jane Eyre", "Charlotte Brontë"),
    ("052", "Cumbres borrascosas", "Emily Brontë"),
    ("053", "Grandes esperanzas", "Charles Dickens"),
    ("054", "Oliver Twist", "Charles Dickens"),
    ("055", "David Copperfield", "Charles Dickens"),
    ("056", "El llamado de la selva", "Jack London"),
    ("057", "Colmillo blanco", "Jack London"),
    ("058", "La Odisea", "Homero"),
    ("059", "La Ilíada", "Homero"),
    ("060", "La divina comedia", "Dante Alighieri"),
    ("061", "El arte de la guerra", "Sun Tzu"),
    ("062", "El príncipe", "Nicolás Maquiavelo"),
    ("063", "La República", "Platón"),
    ("064", "Ética a Nicómaco", "Aristóteles"),
    ("065", "Meditaciones", "Marco Aurelio"),
    ("066", "El mundo de Sofía", "Jostein Gaarder"),
    ("067", "Sapiens", "Yuval Noah Harari"),
    ("068", "Homo Deus", "Yuval Noah Harari"),
    ("069", "El hombre en busca de sentido", "Viktor Frankl"),
    ("070", "Los cuatro acuerdos", "Miguel Ruiz"),
    ("071", "Padre rico, padre pobre", "Robert Kiyosaki"),
    ("072", "Piense y hágase rico", "Napoleon Hill"),
    ("073", "Cómo ganar amigos e influir sobre las personas", "Dale Carnegie"),
    ("074", "Hábitos atómicos", "James Clear"),
    ("075", "El poder de los hábitos", "Charles Duhigg"),
    ("076", "La psicología del dinero", "Morgan Housel"),
    ("077", "El alquimista", "Paulo Coelho"),
    ("078", "Veronika decide morir", "Paulo Coelho"),
    ("079", "Once minutos", "Paulo Coelho"),
    ("080", "El diario de Ana Frank", "Ana Frank"),
    ("081", "La ladrona de libros", "Markus Zusak"),
    ("082", "Bajo la misma estrella", "John Green"),
    ("083", "Ciudades de papel", "John Green"),
    ("084", "El código Da Vinci", "Dan Brown"),
    ("085", "Ángeles y demonios", "Dan Brown"),
    ("086", "La chica del tren", "Paula Hawkins"),
    ("087", "Asesinato en el Orient Express", "Agatha Christie"),
    ("088", "Diez negritos", "Agatha Christie"),
    ("089", "Sherlock Holmes: Estudio en escarlata", "Arthur Conan Doyle"),
    ("090", "El sabueso de los Baskerville", "Arthur Conan Doyle"),
    ("091", "El principito ilustrado", "Antoine de Saint-Exupéry"),
    ("092", "El conde de Montecristo", "Alexandre Dumas"),
    ("093", "Los tres mosqueteros", "Alexandre Dumas"),
    ("094", "El fantasma de la ópera", "Gaston Leroux"),
    ("095", "La peste", "Albert Camus"),
    ("096", "El extranjero", "Albert Camus"),
    ("097", "Ensayo sobre la ceguera", "José Saramago"),
    ("098", "El señor de las moscas", "William Golding"),
    ("099", "Rebelión en la granja", "George Orwell"),
    ("100", "Fahrenheit 451", "Ray Bradbury"),
]


def cargar_libros_iniciales():
    """Convierte la lista de tuplas en diccionarios y los agrega a la biblioteca."""
    for codigo, titulo, autor in LIBROS_INICIALES:
        lista_libros.append({
            "codigo": codigo,
            "titulo": titulo,
            "autor": autor,
            "disponible": True,
        })



# ----------Entradas seguras: nada de lo que escriba el usuario debe romper el programa.-------------

def leer(mensaje):
    """Pide un texto. Si se presiona Ctrl+C no se cierra: avisa y vuelve a preguntar."""
    while True:
        try:
            return input(mensaje).strip()
        except KeyboardInterrupt:
            print("\n(Se presionó Ctrl+C. Escriba 'cancelar' para volver al menú.)")


def pedir_texto(mensaje, obligatorio=True, validar=None, error="Valor no válido."):
    """Pide un texto hasta que sea correcto. Devuelve None si escriben 'cancelar'."""
    while True:
        valor = leer(mensaje)
        if valor.lower() == "cancelar":
            print("Operación cancelada.")
            return None
        if not valor and not obligatorio:
            return ""
        if not valor:
            print("Este campo es obligatorio (o escriba 'cancelar' para salir).")
            continue
        if len(valor) > MAX_TEXTO:
            print(f"El texto es muy largo (máximo {MAX_TEXTO} caracteres).")
            continue
        if validar is not None and not validar(valor):
            print(error)
            continue
        return valor


def pedir_si_no(mensaje):
    """Devuelve True (si), False (no) o None (cancelar)."""
    while True:
        respuesta = leer(mensaje).lower()
        if respuesta == "cancelar":
            print("Operación cancelada.")
            return None
        if respuesta in ("si", "sí", "s"):
            return True
        if respuesta in ("no", "n"):
            return False
        print("Respuesta incorrecta. Escriba si o no.")


def pedir_entero(mensaje, minimo=1):
    """Pide un número entero. Usa try/except para que un texto no cause error."""
    while True:
        texto = pedir_texto(mensaje)
        if texto is None:
            return None
        try:
            valor = int(texto)
        except ValueError:
            print("Debe escribir un número entero, por ejemplo 5000.")
            continue
        if valor < minimo:
            print(f"El número debe ser mayor o igual a {minimo}.")
            continue
        return valor


# --------------Validadores sencillos. -------------------------

def es_numero(texto):
    """Solo dígitos del 0 al 9 (rechaza letras, signos y símbolos raros)."""
    return texto.isascii() and texto.isdigit()


def es_codigo(texto):
    return " " not in texto


def es_correo(texto):
    """Revisa lo básico de un correo: una sola @, sin espacios y con dominio."""
    if " " in texto or texto.count("@") != 1:
        return False
    usuario, dominio = texto.split("@")
    return (usuario != "" and "." in dominio
            and not dominio.startswith(".") and not dominio.endswith("."))


TILDES = str.maketrans("áéíóúüñëï", "aeiouunei")


def normalizar(texto):
    """Pasa a minúsculas y quita tildes para comparar textos."""
    return texto.lower().translate(TILDES)



# ----------------Busquedas internas.---------------------

def buscar_libro(codigo):
    for libro in lista_libros:
        if libro["codigo"] == codigo:
            return libro
    return None


def buscar_usuario(cedula):
    for usuario in lista_usuarios:
        if usuario["cedula"] == cedula:
            return usuario
    return None


def correo_ya_registrado(correo, cedula_actual=None):
    """True si otro usuario (distinto a cedula_actual) ya usa ese correo."""
    for usuario in lista_usuarios:
        if usuario["correo"].lower() == correo.lower() and usuario["cedula"] != cedula_actual:
            return True
    return False


def prestamo_activo_de(codigo):
    for prestamo in lista_prestamos:
        if prestamo["codigo_libro"] == codigo and prestamo["estado"] == "Activo":
            return prestamo
    return None


def prestamos_activos_de_usuario(cedula):
    return [p for p in lista_prestamos
            if p["cedula_usuario"] == cedula and p["estado"] == "Activo"]


def vencidos_de_usuario(cedula):
    hoy = date.today()
    return [p for p in prestamos_activos_de_usuario(cedula)
            if hoy > p["fecha_vencimiento"]]


def deuda_de_usuario(cedula):
    """Suma lo que el usuario todavía debe de multas ya generadas."""
    total = 0
    for prestamo in lista_prestamos:
        if prestamo["cedula_usuario"] == cedula:
            total += prestamo["multa"] - prestamo["multa_pagada"]
    return total


def titulo_de(codigo):
    libro = buscar_libro(codigo)
    return libro["titulo"] if libro else "(libro eliminado)"



# Libros.

def mostrar_un_libro(libro):
    estado = "Disponible" if libro["disponible"] else "Prestado"
    print(f"  Código: {libro['codigo']} | Título: {libro['titulo']} | "
          f"Autor: {libro['autor']} | Estado: {estado}")


def registrar_libro():
    print("\n--- REGISTRAR LIBRO --- (escriba 'cancelar' para salir)")
    codigo = pedir_texto("Código: ", validar=es_codigo,
                         error="El código no puede tener espacios.")
    if codigo is None:
        return
    if buscar_libro(codigo) is not None:
        print("Ya existe un libro con ese código.")
        return
    titulo = pedir_texto("Título: ")
    if titulo is None:
        return
    autor = pedir_texto("Autor: ")
    if autor is None:
        return

    # Un libro nuevo siempre queda disponible
    lista_libros.append({"codigo": codigo, "titulo": titulo,
                         "autor": autor, "disponible": True})
    print("Libro agregado correctamente.")


def mostrar_libros():
    print("\n--- LIBROS REGISTRADOS ---")
    if not lista_libros:
        print("No hay libros registrados.")
        return
    for libro in lista_libros:
        mostrar_un_libro(libro)
    print(f"Total: {len(lista_libros)} libros.")


def mostrar_libros_disponibles():
    print("\n--- LIBROS DISPONIBLES ---")
    disponibles = [libro for libro in lista_libros if libro["disponible"]]
    if not disponibles:
        print("No hay libros disponibles.")
        return
    for libro in disponibles:
        mostrar_un_libro(libro)
    print(f"Total: {len(disponibles)} libros disponibles.")


def buscar_libros_menu():
    print("\n--- BUSCAR LIBRO ---")
    termino = pedir_texto("Código, título o autor a buscar: ")
    if termino is None:
        return
    palabras = normalizar(termino).split()
    encontrados = []
    for libro in lista_libros:
        texto = normalizar(f"{libro['codigo']} {libro['titulo']} {libro['autor']}")
        # El libro debe contener todas las palabras escritas (en cualquier orden)
        if all(palabra in texto for palabra in palabras):
            encontrados.append(libro)
    if not encontrados:
        print("No se encontraron libros con esa búsqueda.")
        return
    for libro in encontrados:
        mostrar_un_libro(libro)


def modificar_libro():
    print("\n--- MODIFICAR LIBRO ---")
    codigo = pedir_texto("Código del libro a modificar: ")
    if codigo is None:
        return
    libro = buscar_libro(codigo)
    if libro is None:
        print("El libro no está registrado.")
        return
    mostrar_un_libro(libro)
    print("Deje vacío el campo que no quiera cambiar.")
    titulo = pedir_texto(f"Nuevo título [{libro['titulo']}]: ", obligatorio=False)
    if titulo is None:
        return
    autor = pedir_texto(f"Nuevo autor [{libro['autor']}]: ", obligatorio=False)
    if autor is None:
        return
    if titulo:
        libro["titulo"] = titulo
    if autor:
        libro["autor"] = autor
    print("Libro modificado correctamente.")


def eliminar_libro():
    print("\n--- ELIMINAR LIBRO ---")
    codigo = pedir_texto("Código del libro a eliminar: ")
    if codigo is None:
        return
    libro = buscar_libro(codigo)
    if libro is None:
        print("El libro no está registrado.")
        return
    if prestamo_activo_de(codigo) is not None:
        print("No se puede eliminar: el libro está prestado en este momento.")
        return
    mostrar_un_libro(libro)
    if pedir_si_no("¿Seguro que desea eliminarlo? (si/no): ") is True:
        lista_libros.remove(libro)
        print("Libro eliminado.")
    else:
        print("No se eliminó ningún libro.")



# Usuarios.

def mostrar_un_usuario(usuario):
    nombre = f"{usuario['nombre']} {usuario['segundo_nombre']}".strip()
    apellido = f"{usuario['primer_apellido']} {usuario['segundo_apellido']}".strip()
    print(f"  Cédula: {usuario['cedula']} | Nombre: {nombre} {apellido} | "
          f"Correo: {usuario['correo']} | Teléfono: {usuario['telefono']}")


def agregar_usuario(primer_nombre, segundo_nombre, primer_apellido,
                    segundo_apellido, correo, cedula, telefono):
    """Guarda el usuario si la cédula y el correo no existen. Devuelve True/False."""
    if buscar_usuario(cedula) is not None:
        print("Ya existe un usuario con esa cédula.")
        return False
    if correo_ya_registrado(correo):
        print("Ese correo ya está registrado.")
        return False
    lista_usuarios.append({
        "nombre": primer_nombre,
        "segundo_nombre": segundo_nombre,
        "primer_apellido": primer_apellido,
        "segundo_apellido": segundo_apellido,
        "correo": correo,
        "cedula": cedula,
        "telefono": telefono,
    })
    print("\nUsuario agregado correctamente.")
    return True


def registrar_usuario():
    print("\n--- REGISTRAR USUARIO --- (escriba 'cancelar' para salir)")
    cedula = pedir_texto("Cédula (solo números): ", validar=es_numero,
                         error="La cédula solo debe tener números.")
    if cedula is None:
        return
    if buscar_usuario(cedula) is not None:
        print("Ya existe un usuario con esa cédula.")
        return
    primer_nombre = pedir_texto("Primer nombre: ")
    if primer_nombre is None:
        return
    segundo_nombre = pedir_texto("Segundo nombre (opcional): ", obligatorio=False)
    if segundo_nombre is None:
        return
    primer_apellido = pedir_texto("Primer apellido: ")
    if primer_apellido is None:
        return
    segundo_apellido = pedir_texto("Segundo apellido (opcional): ", obligatorio=False)
    if segundo_apellido is None:
        return
    correo = pedir_texto("Correo electrónico: ", validar=es_correo,
                         error="Correo no válido. Ejemplo: nombre@correo.com")
    if correo is None:
        return
    if correo_ya_registrado(correo):
        print("Ese correo ya está registrado.")
        return
    telefono = pedir_texto("Teléfono (solo números): ", validar=es_numero,
                           error="El teléfono solo debe tener números.")
    if telefono is None:
        return
    agregar_usuario(primer_nombre, segundo_nombre, primer_apellido,
                    segundo_apellido, correo, cedula, telefono)


def mostrar_usuarios():
    print("\n--- USUARIOS REGISTRADOS ---")
    if not lista_usuarios:
        print("No hay usuarios registrados.")
        return
    for usuario in lista_usuarios:
        mostrar_un_usuario(usuario)


def buscar_usuarios_menu():
    print("\n--- BUSCAR USUARIO ---")
    termino = pedir_texto("Cédula, nombre, apellido o correo: ")
    if termino is None:
        return
    palabras = normalizar(termino).split()
    encontrados = []
    for usuario in lista_usuarios:
        texto = normalizar(" ".join([
            usuario["cedula"], usuario["nombre"], usuario["segundo_nombre"],
            usuario["primer_apellido"], usuario["segundo_apellido"], usuario["correo"],
        ]))
        if all(palabra in texto for palabra in palabras):
            encontrados.append(usuario)
    if not encontrados:
        print("No se encontraron usuarios con esa búsqueda.")
        return
    for usuario in encontrados:
        mostrar_un_usuario(usuario)
        activos = len(prestamos_activos_de_usuario(usuario["cedula"]))
        deuda = deuda_de_usuario(usuario["cedula"])
        print(f"     Libros prestados: {activos}/{MAX_PRESTAMOS} | Deuda: ${deuda:,}")


def modificar_usuario():
    print("\n--- MODIFICAR USUARIO ---")
    cedula = pedir_texto("Cédula del usuario: ", validar=es_numero,
                         error="La cédula solo debe tener números.")
    if cedula is None:
        return
    usuario = buscar_usuario(cedula)
    if usuario is None:
        print("El usuario no está registrado.")
        return
    mostrar_un_usuario(usuario)
    print("Deje vacío el campo que no desea modificar.")

    # Se recogen todos los cambios primero; solo se aplican si no cancelan..
    cambios = {}
    campos_texto = [
        ("nombre", "Nuevo primer nombre"),
        ("segundo_nombre", "Nuevo segundo nombre"),
        ("primer_apellido", "Nuevo primer apellido"),
        ("segundo_apellido", "Nuevo segundo apellido"),
    ]
    for clave, mensaje in campos_texto:
        valor = pedir_texto(f"{mensaje} [{usuario[clave]}]: ", obligatorio=False)
        if valor is None:
            return
        if valor:
            cambios[clave] = valor

    correo = pedir_texto(f"Nuevo correo [{usuario['correo']}]: ", obligatorio=False,
                         validar=es_correo, error="Correo no válido.")
    if correo is None:
        return
    if correo and correo_ya_registrado(correo, cedula):
        print("Ese correo ya lo usa otro usuario. No se hicieron cambios.")
        return
    if correo:
        cambios["correo"] = correo

    telefono = pedir_texto(f"Nuevo teléfono [{usuario['telefono']}]: ", obligatorio=False,
                           validar=es_numero, error="El teléfono solo debe tener números.")
    if telefono is None:
        return
    if telefono:
        cambios["telefono"] = telefono

    usuario.update(cambios)
    print("Usuario modificado correctamente.")


def eliminar_usuario():
    print("\n--- ELIMINAR USUARIO ---")
    cedula = pedir_texto("Cédula del usuario: ", validar=es_numero,
                         error="La cédula solo debe tener números.")
    if cedula is None:
        return
    usuario = buscar_usuario(cedula)
    if usuario is None:
        print("El usuario no está registrado.")
        return
    # Si tiene préstamos registrados se conserva para no perder el historial...
    for prestamo in lista_prestamos:
        if prestamo["cedula_usuario"] == cedula:
            print("No se puede eliminar: el usuario tiene préstamos registrados.")
            print("Se conserva para proteger el historial de la biblioteca.")
            return
    mostrar_un_usuario(usuario)
    if pedir_si_no("¿Seguro que desea eliminar este usuario? (si/no): ") is True:
        lista_usuarios.remove(usuario)
        print("Usuario eliminado correctamente.")
    else:
        print("No se eliminó ningún usuario.")



# Préstamos y devoluciones.

def prestar_libro():
    print("\n--- PRÉSTAMO DE LIBROS ---")
    codigo = pedir_texto("Código del libro: ")
    if codigo is None:
        return
    libro = buscar_libro(codigo)
    if libro is None:
        print("El libro no está registrado.")
        return
    if not libro["disponible"]:
        print("Este libro ya se encuentra prestado.")
        return
    cedula = pedir_texto("Cédula del usuario: ")
    if cedula is None:
        return
    usuario = buscar_usuario(cedula)
    if usuario is None:
        print("El usuario no está registrado.")
        return

    # Reglas de la biblioteca.

    deuda = deuda_de_usuario(cedula)
    if deuda > 0:
        print(f"No se puede prestar: el usuario tiene una multa pendiente de ${deuda:,}.")
        return
    if len(vencidos_de_usuario(cedula)) > 0:
        print("No se puede prestar: el usuario tiene libros vencidos sin devolver.")
        return
    if len(prestamos_activos_de_usuario(cedula)) >= MAX_PRESTAMOS:
        print(f"No se puede prestar: el usuario ya tiene {MAX_PRESTAMOS} libros prestados.")
        return

    hoy = date.today()
    vence = hoy + timedelta(days=DIAS_PRESTAMO)
    lista_prestamos.append({
        "codigo_libro": codigo,
        "cedula_usuario": cedula,
        "fecha_prestamo": hoy,
        "fecha_vencimiento": vence,
        "fecha_devolucion": None,
        "estado": "Activo",
        "multa": 0,
        "multa_pagada": 0,
        "renovaciones": 0, 
    })
    libro["disponible"] = False

    print("\n¡Préstamo realizado correctamente!")
    print("Libro:", libro["titulo"])
    print("Usuario:", usuario["nombre"], usuario["primer_apellido"])
    print("Fecha del préstamo:", hoy)
    print("Fecha límite de devolución:", vence)


def devolver_libro():
    print("\n--- DEVOLUCIÓN DE LIBROS ---")
    codigo = pedir_texto("Código del libro: ")
    if codigo is None:
        return
    libro = buscar_libro(codigo)
    if libro is None:
        print("El libro no está registrado.")
        return
    prestamo = prestamo_activo_de(codigo)
    if prestamo is None:
        print("Ese libro no tiene un préstamo activo (no está prestado).")
        return

    hoy = date.today()
    retraso = (hoy - prestamo["fecha_vencimiento"]).days
    if retraso > 0:
        multa = retraso * MULTA_POR_DIA
        prestamo["multa"] = multa
        print("\nEl libro fue devuelto con retraso.")
        print("Días de retraso:", retraso)
        print(f"Multa por día: ${MULTA_POR_DIA:,}")
        print(f"Total de la multa: ${multa:,}")
        print("La multa queda pendiente: use 'Registrar pago de multa'.")
    else:
        print("\nEl libro fue devuelto a tiempo. No se generó multa.")

    prestamo["fecha_devolucion"] = hoy
    prestamo["estado"] = "Devuelto"
    libro["disponible"] = True
    print("Devolución registrada correctamente.")


def renovar_prestamo():
    print("\n--- RENOVAR PRÉSTAMO ---")
    codigo = pedir_texto("Código del libro: ")
    if codigo is None:
        return
    prestamo = prestamo_activo_de(codigo)
    if prestamo is None:
        print("Ese libro no tiene un préstamo activo.")
        return
    if date.today() > prestamo["fecha_vencimiento"]:
        print("No se puede renovar: el préstamo ya está vencido.")
        return
    if prestamo["renovaciones"] >= MAX_RENOVACIONES:
        print("Este préstamo ya fue renovado. Solo se permite una renovación.")
        return
    nueva_fecha = prestamo["fecha_vencimiento"] + timedelta(days=DIAS_PRESTAMO)
    prestamo["fecha_vencimiento"] = nueva_fecha
    prestamo["renovaciones"] += 1
    print("Préstamo renovado correctamente.")
    print("Nueva fecha límite:", nueva_fecha)



# Multas.

def mostrar_multas_pendientes():
    print("\n--- MULTAS PENDIENTES ---")
    hay_deudas = False
    for usuario in lista_usuarios:
        deuda = deuda_de_usuario(usuario["cedula"])
        if deuda > 0:
            hay_deudas = True
            print(f"  Cédula: {usuario['cedula']} | "
                  f"{usuario['nombre']} {usuario['primer_apellido']} | Debe: ${deuda:,}")
    if not hay_deudas:
        print("No hay multas pendientes.")


def registrar_pago_multa():
    print("\n--- REGISTRAR PAGO DE MULTA ---")
    cedula = pedir_texto("Cédula del usuario: ", validar=es_numero,
                         error="La cédula solo debe tener números.")
    if cedula is None:
        return
    if buscar_usuario(cedula) is None:
        print("El usuario no está registrado.")
        return
    deuda = deuda_de_usuario(cedula)
    if deuda <= 0:
        print("Este usuario no tiene multas pendientes.")
        return

    print(f"Deuda pendiente: ${deuda:,}")
    pago = pedir_entero("Valor que va a pagar: ")
    if pago is None:
        return
    if pago > deuda:
        print("El pago no puede ser mayor que la deuda pendiente.")
        return

    # El pago se aplica primero a las multas más antiguas.

    restante = pago
    for prestamo in lista_prestamos:
        if prestamo["cedula_usuario"] != cedula:
            continue
        pendiente = prestamo["multa"] - prestamo["multa_pagada"]
        if pendiente > 0:
            abono = min(restante, pendiente)
            prestamo["multa_pagada"] += abono
            restante -= abono
            if restante == 0:
                break

    print(f"Pago registrado: ${pago:,}")
    print(f"Saldo pendiente: ${deuda_de_usuario(cedula):,}")



# Reportes.

def mostrar_un_prestamo(prestamo):
    multa = prestamo["multa"]
    pagada = prestamo["multa_pagada"]
    print(f"\nLibro: {titulo_de(prestamo['codigo_libro'])} (código {prestamo['codigo_libro']})")
    print("Cédula del usuario:", prestamo["cedula_usuario"])
    print("Fecha del préstamo:", prestamo["fecha_prestamo"])
    print("Fecha límite:", prestamo["fecha_vencimiento"])
    print("Fecha de devolución:", prestamo["fecha_devolucion"] or "Pendiente")
    print("Estado:", prestamo["estado"])
    print(f"Multa: ${multa:,} | Pagado: ${pagada:,} | Pendiente: ${multa - pagada:,}")


def mostrar_prestamos_activos():
    print("\n--- PRÉSTAMOS ACTIVOS ---")
    hoy = date.today()
    activos = [p for p in lista_prestamos if p["estado"] == "Activo"]
    if not activos:
        print("No hay préstamos activos.")
        return
    for prestamo in activos:
        print(f"\nLibro: {titulo_de(prestamo['codigo_libro'])}")
        print("Cédula del usuario:", prestamo["cedula_usuario"])
        print("Fecha del préstamo:", prestamo["fecha_prestamo"])
        print("Fecha límite:", prestamo["fecha_vencimiento"])
        if hoy > prestamo["fecha_vencimiento"]:
            dias = (hoy - prestamo["fecha_vencimiento"]).days
            print(f"Estado: VENCIDO ({dias} días) | Multa acumulada: ${dias * MULTA_POR_DIA:,}")
        else:
            print("Estado: Dentro del plazo")


def mostrar_vencidos():
    print("\n--- LIBROS VENCIDOS ---")
    hoy = date.today()
    vencidos = [p for p in lista_prestamos
                if p["estado"] == "Activo" and hoy > p["fecha_vencimiento"]]
    if not vencidos:
        print("No hay libros vencidos.")
        return
    for prestamo in vencidos:
        dias = (hoy - prestamo["fecha_vencimiento"]).days
        print(f"\nLibro: {titulo_de(prestamo['codigo_libro'])} | "
              f"Cédula: {prestamo['cedula_usuario']}")
        print(f"Venció el {prestamo['fecha_vencimiento']} | {dias} días de retraso | "
              f"Multa acumulada: ${dias * MULTA_POR_DIA:,}")


def mostrar_historial():
    print("\n--- HISTORIAL DE PRÉSTAMOS ---")
    if not lista_prestamos:
        print("Todavía no hay préstamos registrados.")
        return
    for prestamo in lista_prestamos:
        mostrar_un_prestamo(prestamo)


def consultar_prestamos_usuario():
    print("\n--- PRÉSTAMOS ACTIVOS DE UN USUARIO ---")
    cedula = pedir_texto("Cédula del usuario: ", validar=es_numero,
                         error="La cédula solo debe tener números.")
    if cedula is None:
        return
    usuario = buscar_usuario(cedula)
    if usuario is None:
        print("El usuario no está registrado.")
        return
    mostrar_un_usuario(usuario)
    activos = prestamos_activos_de_usuario(cedula)
    if not activos:
        print("Este usuario no tiene préstamos activos.")
        return
    for prestamo in activos:
        print(f"  Libro: {titulo_de(prestamo['codigo_libro'])} | "
              f"Préstamo: {prestamo['fecha_prestamo']} | Vence: {prestamo['fecha_vencimiento']}")


def historial_usuario():
    print("\n--- HISTORIAL DE UN USUARIO ---")
    cedula = pedir_texto("Cédula del usuario: ", validar=es_numero,
                         error="La cédula solo debe tener números.")
    if cedula is None:
        return
    usuario = buscar_usuario(cedula)
    if usuario is None:
        print("El usuario no está registrado.")
        return
    mostrar_un_usuario(usuario)
    encontrados = 0
    for prestamo in lista_prestamos:
        if prestamo["cedula_usuario"] == cedula:
            mostrar_un_prestamo(prestamo)
            encontrados += 1
    if encontrados == 0:
        print("Este usuario todavía no tiene préstamos registrados.")


# Menú principal.

ACCIONES = {
    "1": ("Registrar un libro", registrar_libro),
    "2": ("Registrar un usuario", registrar_usuario),
    "3": ("Buscar un libro", buscar_libros_menu),
    "4": ("Ver libros registrados", mostrar_libros),
    "5": ("Ver libros disponibles", mostrar_libros_disponibles),
    "6": ("Ver usuarios registrados", mostrar_usuarios),
    "7": ("Modificar un libro", modificar_libro),
    "8": ("Eliminar un libro", eliminar_libro),
    "9": ("Prestar un libro", prestar_libro),
    "10": ("Devolver un libro", devolver_libro),
    "11": ("Ver préstamos activos", mostrar_prestamos_activos),
    "12": ("Ver libros vencidos", mostrar_vencidos),
    "13": ("Ver historial de préstamos", mostrar_historial),
    "14": ("Buscar un usuario", buscar_usuarios_menu),
    "15": ("Modificar un usuario", modificar_usuario),
    "16": ("Eliminar un usuario", eliminar_usuario),
    "17": ("Renovar un préstamo", renovar_prestamo),
    "18": ("Registrar pago de multa", registrar_pago_multa),
    "19": ("Ver multas pendientes", mostrar_multas_pendientes),
    "20": ("Ver préstamos activos de un usuario", consultar_prestamos_usuario),
    "21": ("Ver historial de un usuario", historial_usuario),
}

GRUPOS_MENU = {
    "REGISTROS": ["1", "2"],
    "CONSULTAS Y BÚSQUEDAS": ["3", "4", "5", "6", "14"],
    "GESTIÓN DE LIBROS Y USUARIOS": ["7", "8", "15", "16"],
    "PRÉSTAMOS Y DEVOLUCIONES": ["9", "10", "17"],
    "MULTAS": ["18", "19"],
    "REPORTES": ["11", "12", "13", "20", "21"],
}


def mostrar_menu():
    print("\n" + "=" * 50)
    print("       SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("=" * 50)
    for grupo, opciones in GRUPOS_MENU.items():
        print(f"\n--- {grupo} ---")
        for clave in opciones:
            print(f"{clave:>2}. {ACCIONES[clave][0]}")
    print("\n 0. Salir del sistema")
    print("=" * 50)


def main():
    cargar_libros_iniciales()

    while True:
        try:
            mostrar_menu()
            opcion = leer("\nSeleccione una opción: ")

            if opcion == "0":
                if pedir_si_no("¿Seguro que desea salir? (si/no): ") is True:
                    print("\nGracias por utilizar el sistema. ¡Hasta pronto!")
                    break
            elif opcion in ACCIONES:
                ACCIONES[opcion][1]()
            else:
                print(f"\nOpción incorrecta. Escriba un número entre 0 y {len(ACCIONES)}.")

        except EOFError:
            # El teclado se cerró: no se puede seguir pidiendo datos.

            print("\nLa entrada de datos se cerró. Fin del programa.")
            break
        except KeyboardInterrupt:
            print("\nPara salir use la opción 0 del menú.")
        except Exception as error:
            # Último salvavidas: explica el problema y vuelve al menú,
            print(f"\nOcurrió un problema inesperado ({error}).")
            print("No se cerró el programa. Intente de nuevo.")


if __name__ == "__main__":
    main()

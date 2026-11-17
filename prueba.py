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
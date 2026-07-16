from utils import cargar_datos, guardar_datos

while True:
    print("\n======= MENU =======")
    print("1. Agregar vehiculo")
    print("2. Buscar vehiculo por patente")
    print("3. Actualizar vehiculo")
    print("4. Ver listado de vehiculos")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        vehiculos = cargar_datos()

        vehiculo = {
            "marca": input("Marca: "),
            "modelo": input("Modelo: "),
            "kilometraje": input("Kilometraje: "),
            "precio": input("Precio: "),
            "patente": input("Patente: ").upper()
        }

        vehiculos.append(vehiculo)
        guardar_datos(vehiculos)
        print("Vehiculo agregado.")

    elif opcion == "2":
        patente = input("Ingrese la patente: ").upper()
        vehiculos = cargar_datos()

        encontrado = False

        for v in vehiculos:
            if v["patente"] == patente:
                print("\nMarca:", v["marca"])
                print("Modelo:", v["modelo"])
                print("Kilometraje:", v["kilometraje"])
                print("Precio:", v["precio"])
                print("Patente:", v["patente"])
                encontrado = True
                break

        if not encontrado:
            print("Vehiculo no encontrado.")

    elif opcion == "3":
        patente = input("Ingrese la patente: ").upper()
        vehiculos = cargar_datos()

        encontrado = False

        for v in vehiculos:
            if v["patente"] == patente:
                print("Ingrese los nuevos datos")

                v["marca"] = input("Marca: ")
                v["modelo"] = input("Modelo: ")
                v["kilometraje"] = input("Kilometraje: ")
                v["precio"] = input("Precio: ")
                v["patente"] = input("Patente: ").upper()

                guardar_datos(vehiculos)
                print("Vehiculo actualizado.")
                encontrado = True
                break

        if not encontrado:
            print("Vehiculo no encontrado.")

    elif opcion == "4":
        vehiculos = cargar_datos()

        if len(vehiculos) == 0:
            print("No hay vehiculos cargados.")
        else:
            for v in vehiculos:
                print("----------------------------")
                print("Marca:", v["marca"])
                print("Modelo:", v["modelo"])
                print("Kilometraje:", v["kilometraje"])
                print("Precio:", v["precio"])
                print("Patente:", v["patente"])

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opcion incorrecta.")
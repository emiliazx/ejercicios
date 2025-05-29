sueldo_base = 50000
ventas_mensuales = 100000
tasa_iva = 0.19  # Tasa de IVA (19% en Chile)

# menu de opciones
while True:
    print("menu de opciones")
    print("1. seleccionar para saber sueldo (sin IVA)")
    print("2. seleccionar para saber sueldo (con IVA)")
    print("3. seleccionar para saber ventas_mensuales")
    print("4. seleccionar para saber monto total de ambas (sin IVA)")
    print("5. seleccionar para saber monto total de ambas (con IVA)")
    print("6. seleccionar para salir")

    opcion = input("ingrese la opcion: ")

    if opcion == '1':
        print(f"el sueldo original (sin IVA) es: $ {sueldo_base}")

    elif opcion == '2':
        monto_iva_sueldo = sueldo_base * tasa_iva
        sueldo_con_iva = sueldo_base + monto_iva_sueldo
        print(f"el sueldo con IVA es: $ {sueldo_con_iva:.0f}")  # Formateado sin decimales

    elif opcion == '3':
        print(f"las ventas_mensuales son: $ {ventas_mensuales}")

    elif opcion == '4':
        total_sin_iva = sueldo_base + ventas_mensuales
        print(f"el monto total (sin IVA) es: $ {total_sin_iva}")

    elif opcion == '5':
        monto_iva_total = (sueldo_base + ventas_mensuales) * tasa_iva
        total_con_iva = sueldo_base + ventas_mensuales + monto_iva_total
        print(f"el monto total (con IVA) es: $ {total_con_iva:.0f}") # Formateado sin decimales

    elif opcion == '6':
        break

    else:
        print("Opción inválida. Por favor, elige una opción del menú (1-6).")
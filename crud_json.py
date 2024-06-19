import json, time # os

# with open("compras.json", mode = "r") as archivoCompras:
#     leerJson = json.load(archivoCompras)
#     # leerJson ["productos"]
#     for i in leerJson["productos"]:
#         print(i)
#         time.sleep(1)
#         # os.system("cls")

# def menuPrincipal():
#     print("*******************************")
#     print("*        HappyStore 😂        *")
#     print("*******************************")
#     print("1 - Mantenedor de Servicios")
#     print("2 - Tienda")
#     print("3 - Reportes")
#     print("0 - Salir")
#     print("*******************************")
#     opcion = int(input("Seleccione una opción: "))
#     match opcion:
#         case 1:
#         print("""
#                 1 - Mantenedor de productos
#                 2 -Mantenedor de usuarios
#                 3 - Mantenedor de vendedores
#                 4 - Mantenedor de boletas (solo buscar)
#                 5 - Muestra el detalle boleta
#                 6 - Exportar información:
#                 7 - Crear un json de cada mantenedor
#                 8 - Importar información:
#                 0 - Importar un json de cada mantenedor""")

#         case 2:

#         case 3:

#         case 0:

    
    
# menuPrincipal()










           
           #        ********* LISTO **********

# def agregarProducto(): # Mantenedor de productos # EJEMPLO DE AGREGAR CLIENTE,        MODIFICAR     CON     PRODUCTOS
#     try:
#         with open ("compras.json", mode = "r") as archivoCompras:
#             leerProducto = json.load(archivoCompras)
#             producto_cli = {
#                 "id": len(leerProducto["productos"]) + 1,
#                 "nombre": nombre ,
#                 "precio": precio
#             }
#             leerProducto["productos"].append(producto_cli)
#         with open ("compras.json", mode = "w") as archivoCompras:
#             json.dump(leerProducto,archivoCompras, indent = 4)
#         print("Se agrego correctamente")
#     except:
#         print("Error")
# nombre = input("Ingrese el nombre del producto: ")
# precio = int(input("Ingrese el precio del producto: "))

# agregarProducto() # nombre precio 






def leerProducto(): # Mantenedor de productos
    with open ("compras.json", mode = "r") as archivoCompra:
        leerProducto = json.load(archivoCompra)
        for i in range(len(leerProducto["productos"])):
            print(i)
            


leerProducto()

# def actualizarProducto(): # Mantenedor de productos

# def borrarProducto(): # Mantenedor de productos
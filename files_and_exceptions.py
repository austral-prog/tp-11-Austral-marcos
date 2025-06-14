def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    ventas = {}
    with open(filename, "r") as file:
        contenido = file.read().strip()
        if not contenido:
            return ventas
        items = contenido.split(";")
        for item in items:
            if not item:
                continue
            if ":" not in item:
                continue
            producto, valor = item.split(":", 1)
            producto = producto.strip()
            valor = float(valor.strip())
            if producto not in ventas:
                ventas[producto] = []
            ventas[producto].append(valor)
    return ventas


def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    data = {
    'producto1': [100.0, 150.0],
    'producto2': [200.0, 100.0],
    'producto3': [50.0]
    }
    for producto, montos in data.items():
        total = sum(montos)
        promedio = int("")
        if montos:
            promedio = total / length(montos)
        else:
            promedio = 0
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")

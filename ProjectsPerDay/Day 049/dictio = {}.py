dictio = {0:"MAIGAASH"}
try:
    # Intenta acceder a un elemento del diccionario
    print(dictio[0])

except KeyError:
    # La excepción se produce si el diccionario está vacío
    print("Hello")
def verificar_disponibilidad(reservas, nueva):
    for rer in reservas:
        if rer["sala"] == nueva["sala"] and rer["hora"] == nueva["hora"]:
            return False
    return True
def verificar_disponibilidad(reservas, nueva):
    for reser in reservas:
        if reser["sala"] == nueva["sala"] and r["hora"] == nueva["hora"]:
            return False
    return True
def test_input(arrays, mensaje):
    arrays = list(map(lambda x: x.upper(), arrays))
    resp = input(mensaje).upper()
    while resp not in arrays:
        print("Debe de ser una de las sigientes opciones", arrays)
        resp = input(mensaje)
    return resp

def output(is_ok,cripto,fiat,data):
    if is_ok:
        print(f"1 {cripto} vale {data:.2f} {fiat}")
    else:
        print(f"Se ha producido el error: {data}")


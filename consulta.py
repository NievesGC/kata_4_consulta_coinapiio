import requests

apikey = "1B731114-B858-433E-89F1-A792584BE95B"

criptos =["BTC","ETH","USDT","BNB","USCD"]
fiats = ["EUR","USD","JPY"]

def test_input(arrays, mensaje):
    money = input(mensaje)
    while money not in arrays:
        print("Debe de ser una de las sigientes opciones", arrays)
        money = input(mensaje)
    return money

def get_rate(cripto,fiat):
    url = f"https://rest.coinapi.io/v1/exchangerate/{cripto}/{fiat}?apikey={apikey}"
    try:
        response = requests.get(url)

        data = response.json()

        if response.status_code == 200:
            return True,data['rate']
            #print(f"1{cripto} vale {data['rate']:.2f}{fiat}")
        else: 
            return False, data['error']
            print(response.status_code,"-",data["error"])
    except requests.exceptions.RequestException as e:
        return False, str(e)
        #print("Se ha producido un error en la petición:\n", url)



cripto = test_input(criptos,"¿Qué criptomoneda quieres saber? " )
fiat = test_input(fiats,"¿En qué la quieres? ")


is_OK, data = get_rate(cripto,fiat)

if is_OK:
    print(f"1{cripto} vale {data:.2f}{fiat}")
else:
    print(f"Se ha producido el error: {data}")



"""
cripto = input("¿Qué criptomoneda quieres saber? ")
while cripto not in criptos:
    print("La criptomoneda debe estar entre", criptos)
    cripto = input("¿Qué criptomoneda quieres saber? ")

fiat = input("¿En qué la quieres? ")
while fiat not in fiats:
    print("La moneda fiat debe esar entre", fiats)
    fiat = input("¿En qué la quieres? ")
"""   


url = f"https://rest.coinapi.io/v1/exchangerate/{cripto}/{fiat}?apikey={apikey}"
"""
try:
    response = requests.get(url)

    data = response.json()

    if response.status_code == 200:
        print(f"1{cripto} vale {data['rate']:.2f}{fiat}")
    else: 
        print(response.status_code,"-",data["error"])
except requests.exceptions.RequestException:
    print("Se ha producido un error en la petición:\n", url)
"""



"""
print(response.status_code)
print(response.text)
"""
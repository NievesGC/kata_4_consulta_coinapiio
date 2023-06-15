import requests

apikey = "1B731114-B858-433E-89F1-A792584BE95B"

def get_rate(cripto,fiat):
    url = f"https://rest.coinapi.io/v1/exchangerate/{cripto}/{fiat}?apikey={apikey}"
    try:
        response = requests.get(url)

        data = response.json()

        if response.status_code == 200:
            return True,data['rate']
            
        else: 
            return False, data['error']
    except requests.exceptions.RequestException as e:
        return False, str(e)
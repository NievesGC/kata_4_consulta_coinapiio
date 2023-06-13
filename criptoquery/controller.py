from criptoquery.view import test_input,output
from criptoquery.models import criptos, fiats, get_rate

class Controller:
    def mainloop(self):

        while True:
            #USANDO LA VISTA PARA ENTRADA DE DATOS DEL USUSARIO
            cripto = test_input(criptos,"¿Qué criptomoneda quieres saber? " )
            fiat = test_input(fiats,"¿En qué la quieres? ")



            #USAR EL MODELO PARA OBTENBER UN DATO DE INTERNET
            is_OK, data = get_rate(cripto,fiat)


            #TENDRIA QUE IR A LA VISTA, ,PERO TODAVIA NO
            output(is_OK,cripto,fiat,data)

            #PREGUNTAR SI SEGUIMOS, LA PRIGUNTA LA DELEGAMOS EN LA VISTA
            more_conversion = test_input(('S','N'),"Quieres introducir mas monedas:")
            if more_conversion != "S":
                break

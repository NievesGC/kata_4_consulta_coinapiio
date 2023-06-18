import tkinter as tk
import requests
from tkcriptoquery.views import Desplegable
from tkcriptoquery.models import get_rate
     

class Converter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.criptos = Desplegable(self,"CRIPTO","BTC","ETH","USDT","BNB","USDC")
        self.criptos.grid(column=0,row=0)
        #self.criptos.selected_option.trace("w", self.validate_button)

        self.fiats = Desplegable(self,"FIAT","EUR","USD","JPY")
        self.fiats.grid(column=1,row=0)
        #self.fiats.selected_option.trace("w", self.validate_button)

        self.result = tk.Label(self)
        self.result.grid(row=1,column=0)

        tk.Button(self, text="Consultar",command=self.get_rate).grid(column=1,row=1)

    

    def get_rate(self): 
        cripto = self.criptos.selected_option.get()
        fiat = self.fiats.selected_option.get()

        if cripto != "CRIPTO" and fiat != "FIAT":
            is_ok,data= get_rate(cripto,fiat)
            if is_ok:
                self.result.config(text=data)
            else:
                self.result.config(text="Se ha producido un error en la consulta")
                    
        else: 
            self.result.config(text="Dwbwa seleccionar ambos valores")
            


    
        
class Cliente:
    
    def __init__(self, config_cliente = None):

        if config_cliente:
            self.umbral = config_cliente["umbral"]
            self.descuento = config_cliente["descuento"]
        else:
            self.umbral = []
            self.descuento =  []
    
    def set_umbral(self, umbral ):
        self.umbral = umbral

    def get_umbral(self):
        return self.umbral
            
    def set_facturacion(self, facturacion ):
        self.facturacion = facturacion

    def get_facturacion(self):
        return self.facturacion

    def set_descuento(self, descuento ):
        self.descuento = descuento

    def get_descuento(self):
        return self.descuento

    def has_descuento(self)-> bool:
        return self.umbral and list(filter(lambda x: self.facturacion > x ,self.umbral))

    def total(self):
        
        if self.has_descuento():
            valor_umbral = list(filter(lambda x: self.facturacion > x ,self.umbral))[-1]
            return self.facturacion - (self.facturacion * self.descuento[self.umbral.index(valor_umbral)])
        else:
            return self.facturacion
import unittest

from cliente import Cliente

class TestStringMethods(unittest.TestCase):

    
    def test_aplicar_descuento(self):
        config_cliente = {"umbral":[0, 10 ,15], "descuento":[0, 0.10, 0.15] }
        '''
        config_cliente = [ {"umbral": 10 , "descuento": 0.10 },
                          {"umbral": 0 , "descuento": 0.0 } ] 
        config_cliente =  {
            "nombre": "raul", 
            "umbral_descuento" : { 10 : 0.10 ,  0 : 0.0 } }
        '''
        cliente = Cliente(config_cliente)
        cliente.set_umbral( [100] )
        cliente.set_facturacion(1000)
        cliente.set_descuento([0.10])
        
        #self.assertTrue(cliente.has_descuento())
        self.assertLess(cliente.total(),cliente.get_facturacion())

    def test_no_aplica_descuento(self):
        #config_cliente = {"umbral":[0, 100 ,150], "descuento":[0, 0.10, 0.15] }
        cliente = Cliente()
        #cliente.set_umbral(100)
        cliente.set_facturacion(100)
        #cliente.set_descuento(0.10)
        
        #self.assertFalse(cliente.has_descuento())
        self.assertEquals(cliente.total(),cliente.get_facturacion())
        


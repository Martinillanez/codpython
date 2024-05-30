import unittest
from datetime import datetime
from lista import Lista
from serviciotransporte import ServicioTransporte
from servicioembalaje import ServicioEmbalaje

class TestLista(unittest.TestCase):
    
    def setUp(self):
        self.lista = Lista()
    
    def test_agregar_servicio_transporte(self):
        transporte = ServicioTransporte(
            nombreemp="Empresa A",
            nombrecon="Contratante A",
            direccion="Dirección A",
            fechaservicio=datetime.strptime("29/05/2024", "%d/%m/%Y"),
            comision=100.0,
            preciohora=50.0,
            pesocarga=200,
            direcciondestino="Destino A"
        )
        self.lista.agregar_servicio(transporte)
        servicios = list(self.lista)
        self.assertEqual(len(servicios), 1)
        self.assertIs(servicios[0], transporte)
    
    def test_agregar_servicio_embalaje(self):
        embalaje = ServicioEmbalaje(
            nombreemp="Empresa B",
            nombrecon="Contratante B",
            direccion="Dirección B",
            fechaservicio=datetime.strptime("29/05/2024", "%d/%m/%Y"),
            comision=100.0,
            preciouni=10.0,
            pesouni=60,
            cantidad=5
        )
        self.lista.agregar_servicio(embalaje)
        servicios = list(self.lista)
        self.assertEqual(len(servicios), 1)
        self.assertIs(servicios[0], embalaje)

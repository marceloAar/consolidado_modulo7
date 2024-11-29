from django.test import TestCase
from .models import Laboratorio

class LaboratorioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear datos iniciales para pruebas
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio XYZ",
            ciudad="Santiago",
            pais="Chile"
        )

    def test_model_str_method(self):
        # Verificar que __str__ retorna el nombre
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(str(laboratorio), "Laboratorio XYZ")

    def test_default_values(self):
        # Crear un laboratorio sin especificar ciudad ni país
        laboratorio = Laboratorio.objects.create(nombre="Laboratorio Beta")
        self.assertEqual(laboratorio.ciudad, "Ciudad")
        self.assertEqual(laboratorio.pais, "Pais")

    def test_data_saved_correctly(self):
        # Verificar que los datos del laboratorio se guardaron correctamente
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(laboratorio.nombre, "Laboratorio XYZ")
        self.assertEqual(laboratorio.ciudad, "Santiago")
        self.assertEqual(laboratorio.pais, "Chile")

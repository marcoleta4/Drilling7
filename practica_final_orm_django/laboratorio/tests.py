from django.test import TestCase
from laboratorio.models import Laboratorio
from django.test import TestCase
from django.urls import reverse

class LaboratorioTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear laboratorios de prueba
        Laboratorio.objects.create(nombre='Laboratorio Prueba 1')
        Laboratorio.objects.create(nombre='Laboratorio Prueba 2')

    def test_coincide_con_setup(self):
        # Verificar que se crearon
        laboratorios = Laboratorio.objects.all()
        self.assertEqual(laboratorios.count(), 2)
        self.assertEqual(laboratorios[0].nombre, 'Laboratorio Prueba 1')

    def test_lista_url(self):
        # Probar URL de lista de laboratorios
        response = self.client.get('/laboratorios/')  
        self.assertEqual(response.status_code, 200)

    def test_lista_uso_plantilla(self):
        # Probar uso plantilla correcta
        response = self.client.get(reverse('lista_laboratorios'))
        self.assertTemplateUsed(response, 'laboratorios/lista.html')

    def test_lista_contenido(self):
        # Probar contenido esperado
        response = self.client.get(reverse('lista_laboratorios'))
        self.assertContains(response, 'Laboratorio Prueba 1')
        self.assertContains(response, 'Laboratorio Prueba 2')
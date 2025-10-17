"""
Testes de integração para funcionalidade de seleção de país
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.template.loader import render_to_string
from quizzes.tests.fixtures.factories import ThemeFactory


class CountrySelectionIntegrationTest(TestCase):
    """Testes de integração para seleção de país"""

    def setUp(self):
        self.client = Client()
        self.theme = ThemeFactory.create(country='pt-BR')

    def test_country_form_present_in_template(self):
        """Testa se o formulário de país está presente no template base"""
        response = self.client.get(reverse('quizzes:home'))
        self.assertEqual(response.status_code, 200)
        
        # Verificar se o formulário está presente
        self.assertContains(response, 'id="countryFormHeader"')
        self.assertContains(response, 'action="/set-country/"')
        self.assertContains(response, 'name="country"')

    def test_country_selector_elements_present(self):
        """Testa se todos os elementos do seletor de país estão presentes"""
        response = self.client.get(reverse('quizzes:home'))
        self.assertEqual(response.status_code, 200)
        
        # Verificar elementos do seletor
        self.assertContains(response, 'id="selectButtonHeader"')
        self.assertContains(response, 'id="optionsListHeader"')
        self.assertContains(response, 'id="searchInputHeader"')
        self.assertContains(response, 'id="optionsContainerHeader"')

    def test_country_selector_javascript_present(self):
        """Testa se o JavaScript do seletor de país está presente"""
        response = self.client.get(reverse('quizzes:home'))
        self.assertEqual(response.status_code, 200)
        
        # Verificar se o JavaScript está presente
        self.assertContains(response, 'countries = [')
        self.assertContains(response, 'selectButtonHeader')
        self.assertContains(response, 'fetch(form.action')
        self.assertContains(response, 'window.location.href')

    def test_country_list_in_javascript(self):
        """Testa se a lista de países está correta no JavaScript"""
        response = self.client.get(reverse('quizzes:home'))
        self.assertEqual(response.status_code, 200)
        
        content = response.content.decode()
        
        # Verificar se países importantes estão na lista com flagCode
        self.assertIn("'pt-BR', name: 'Brasil', flagCode: '1f1e7-1f1f7'", content)
        self.assertIn("'en-US', name: 'United States', flagCode: '1f1fa-1f1f8'", content)
        self.assertIn("'es-ES', name: 'Spain', flagCode: '1f1ea-1f1f8'", content)

    def test_current_country_displayed(self):
        """Testa se o país atual é exibido corretamente"""
        # Definir país na sessão
        session = self.client.session
        session['country'] = 'en-US'
        session.save()
        
        response = self.client.get(reverse('quizzes:home'))
        self.assertEqual(response.status_code, 200)
        
        # Verificar se o país atual é exibido no JavaScript
        self.assertContains(response, "const currentCountry = 'en-US';")

    def test_country_change_workflow(self):
        """Testa o fluxo completo de mudança de país"""
        # 1. Acessar página inicial
        response = self.client.get(reverse('quizzes:home'))
        self.assertEqual(response.status_code, 200)
        
        # 2. Verificar país padrão
        self.assertEqual(self.client.session.get('country'), None)
        
        # 3. Simular mudança de país via POST
        response = self.client.post(reverse('quizzes:set_country'), {
            'country': 'es-ES'
        })
        self.assertEqual(response.status_code, 200)
        
        # 4. Verificar se país foi salvo na sessão
        self.assertEqual(self.client.session['country'], 'es-ES')
        
        # 5. Verificar resposta JSON
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['country'], 'es-ES')

    def test_country_filtering_works(self):
        """Testa se o filtro por país funciona nas views"""
        # Criar tema para outro país
        theme_us = ThemeFactory.create(country='en-US', title='US Theme')
        theme_br = ThemeFactory.create(country='pt-BR', title='BR Theme')
        
        # Testar sem país definido (deve mostrar pt-BR por padrão)
        response = self.client.get(reverse('quizzes:home'))
        self.assertContains(response, 'BR Theme')
        self.assertNotContains(response, 'US Theme')
        
        # Definir país como US
        session = self.client.session
        session['country'] = 'en-US'
        session.save()
        
        # Testar com país US
        response = self.client.get(reverse('quizzes:home'))
        self.assertContains(response, 'US Theme')
        self.assertNotContains(response, 'BR Theme')

    def test_country_context_in_all_views(self):
        """Testa se o contexto de país está presente em todas as views"""
        views_to_test = [
            ('quizzes:home', {}),
            ('quizzes:theme_detail', {'theme_slug': self.theme.slug}),
        ]
        
        for view_name, kwargs in views_to_test:
            response = self.client.get(reverse(view_name, kwargs=kwargs))
            self.assertEqual(response.status_code, 200)
            
            # Verificar se contexto de país está presente
            self.assertIn('current_country', response.context)
            self.assertIn('current_language', response.context)

    def test_country_selector_responsive_elements(self):
        """Testa se elementos responsivos do seletor estão presentes"""
        response = self.client.get(reverse('quizzes:home'))
        self.assertEqual(response.status_code, 200)
        
        # Verificar classes CSS responsivas
        self.assertContains(response, 'custom-select-header')
        self.assertContains(response, 'select-button-header')
        self.assertContains(response, 'options-list-header')
        self.assertContains(response, 'search-box-header')

    def test_country_selector_accessibility(self):
        """Testa se o seletor de país tem elementos de acessibilidade"""
        response = self.client.get(reverse('quizzes:home'))
        self.assertEqual(response.status_code, 200)
        
        # Verificar se tem placeholder para busca
        self.assertContains(response, 'placeholder="Buscar país..."')
        
        # Verificar se tem elementos semânticos
        self.assertContains(response, 'flag-header')
        self.assertContains(response, 'name-header')

    def test_country_change_with_csrf_protection(self):
        """Testa se a mudança de país funciona com proteção CSRF"""
        # Obter token CSRF
        csrf_response = self.client.get(reverse('quizzes:home'))
        csrf_token = csrf_response.cookies.get('csrftoken')
        
        if csrf_token:
            # Testar com token CSRF
            response = self.client.post(
                reverse('quizzes:set_country'),
                {'country': 'en-US'},
                HTTP_X_CSRFTOKEN=csrf_token.value
            )
            self.assertEqual(response.status_code, 200)
            
            data = response.json()
            self.assertTrue(data['success'])
            self.assertEqual(self.client.session['country'], 'en-US')

    def test_country_selector_error_handling(self):
        """Testa se o tratamento de erros funciona corretamente"""
        # Testar país inválido
        response = self.client.post(reverse('quizzes:set_country'), {
            'country': 'invalid-country'
        })
        self.assertEqual(response.status_code, 400)
        
        data = response.json()
        self.assertFalse(data['success'])
        self.assertIn('error', data)

    def test_country_selector_javascript_error_handling(self):
        """Testa se o JavaScript tem tratamento de erros"""
        response = self.client.get(reverse('quizzes:home'))
        self.assertEqual(response.status_code, 200)
        
        content = response.content.decode()
        
        # Verificar se tem tratamento de erros no JavaScript
        self.assertIn('console.error', content)
        self.assertIn('catch(error', content)
        self.assertIn('Revert flag display', content)

# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from apps.hello.models import Contact


class HomeViewTest(TestCase):
    """"
    Tests views
    """
    def setUp(self):
        """
        Set for working tests
        """
        self.client = Client()
        self.url = reverse('home')

    def create_obj(self):
        """
        Create instance of Contact table
        """
        Contact.objects.create(
            name='testName',
            surname='testSurname',
            date_birth='1986-11-07',
            bio='Django Python developer Dublh 3 '
                '\r\nJunior Django Python developer',
            email='email@email.com',
            jabber='jabber@co',
            skype='skype',
            other_contacts='test contact info')

    def test_home_view_without_data(self):
        """
        Table of DB is empty, must be presented 'No contact info'
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('42 Coffee Cups Test Assignment', response.content)
        self.assertIn('No contact info', response.content)
        self.assertNotIn('myName', response.content)
        self.assertNotIn('mySurname', response.content)

    def test_home_template_context(self):
        """
        Check home status code and context
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('info' in response.context)

    def test_home_template_content(self):
        """
        Check info to the template
        """
        self.create_obj()
        response = self.client.get(self.url)
        data = response.context['info']
        self.assertEqual(data.name, 'testName')
        self.assertEqual(data.surname, 'testSurname')
        self.assertEqual(data.date_birth.strftime('%d-%m-%Y'), '07-11-1986')
        self.assertEqual(data.bio, 'Django Python developer Dublh 3 '
                                   '\r\nJunior Django Python developer')
        self.assertEqual(data.email, 'email@email.com')
        self.assertEquals(data.skype, 'skype')
        self.assertEqual(data.jabber, 'jabber@co')

    def test_home_view_cyrillic(self):
        """Test for views.home in case object data is cyrillic"""
        Contact.objects.create(
            name='Артем',
            surname='Александрович',
            date_birth='1986-11-07',
            bio='Биография',
            email='test@email.com',
            jabber='АБВГДЕ',
            skype='ЖЗИЙК',
            other_contacts='Другие контакты'
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('42 Coffee Cups Test Assignment', response.content)
        self.assertIn('Артем', response.content)
        self.assertIn('Александрович', response.content)
        self.assertIn('Date of birth', response.content)
        self.assertIn('Био', response.content)
        self.assertIn('Другие контакты', response.content)

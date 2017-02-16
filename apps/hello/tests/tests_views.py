# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from apps.hello.models import Contact
import factory


class ContactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contact

    name = factory.Sequence(lambda n: 'testName%d' % n)
    surname = factory.Sequence(lambda n: 'testSurname%d' % n)
    date_birth = '1986-11-07'
    bio = factory.Sequence(lambda n: 'Django Python developer '
                                     'Dublh 3 \r\nJunior Django Python '
                                     'developer %d' % n)
    email = factory.LazyAttribute(lambda obj: '%s@email.com' % obj.name)
    jabber = factory.Sequence(lambda n: 'jabber%d@co' % n)
    skype = factory.Sequence(lambda n: 'skype%d' % n)
    other_contacts = factory.Sequence(lambda n: 'test contact info%d' % n)


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

    def test_home_view_without_data(self):
        """
        Test table of DB is empty, must be presented 'No contact info'
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('42 Coffee Cups Test Assignment', response.content)
        self.assertIn('No contact info', response.content)
        self.assertNotIn('testName', response.content)
        self.assertNotIn('testSurname', response.content)
        self.assertEqual(response.context['info'], None)
        print('test witout data ', Contact.objects.count())

    def test_home_view_template_base(self):
        """
        Test home view with base elements
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertInHTML('<link rel="stylesheet" href="/static/css/bootstrap/'
                          'bootstrap.min.css">', response.content)
        self.assertInHTML('<link rel="stylesheet" href="/static/css/style.css"'
                          ' media="screen, projection">', response.content)
        self.assertInHTML('<li class="active"><a href="/">Home</a></li>',
                          response.content)
        self.assertTrue('info' in response.context)
        self.assertContains(response, '42 Coffee Cups Test Assignment')
        print('test base ', Contact.objects.count())

    def test_home_template_content(self):
        """
        Check info to the template with one object
        """
        ContactFactory()
        response = self.client.get(self.url)
        data = response.context['info']
        self.assertEqual(data.name, 'testName0')
        self.assertEqual(data.surname, 'testSurname0')
        self.assertEqual(data.date_birth.strftime('%d-%m-%Y'), '07-11-1986')
        self.assertEqual(data.bio, 'Django Python developer Dublh 3 '
                                   '\r\nJunior Django Python developer 0')
        self.assertEqual(data.email, 'testName0@email.com')
        self.assertEquals(data.skype, 'skype0')
        self.assertEqual(data.jabber, 'jabber0@co')
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Last name')
        self.assertContains(response, 'email')
        print('test template content', Contact.objects.count())

    def test_home_view_cyrillic(self):
        """
        Test for views.home in case object data is cyrillic
        """
        ContactFactory.create(name='Артем', surname='Александрович',
                              date_birth='1986-11-07', bio='Биография',
                              email='test@email.com', skype='АБВГДЕ',
                              jabber='ЖЗИЙК',
                              other_contacts='Другие контакты')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('42 Coffee Cups Test Assignment', response.content)
        self.assertIn('Артем', response.content)
        self.assertIn('Александрович', response.content)
        self.assertIn('Date of birth', response.content)
        self.assertIn('Био', response.content)
        self.assertIn('Другие контакты', response.content)
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Last name')
        self.assertContains(response, 'Email')
        self.assertContains(response, 'Артем')
        print('test cyrilic ', Contact.objects.count())

    def test_home_view_two_object(self):
        """
        Test home view, table Contact has 2 objects,
        """
        first = ContactFactory()
        second = ContactFactory()
        response = self.client.get(self.url)
        data = response.context['info']
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(data, None)
        self.assertEqual(Contact.objects.first(), data)
        self.assertEqual(Contact.objects.count(), 2)
        self.assertEqual(data.name, first.name)
        self.assertEqual(data.surname, first.surname)
        self.assertEqual(data.date_birth.strftime('%d-%m-%Y'), '07-11-1986')
        self.assertEqual(data.bio, first.bio)
        self.assertEqual(data.email, first.email)
        self.assertEquals(data.skype, first.skype)
        self.assertEqual(data.jabber, first.jabber)
        self.assertEqual(Contact.objects.last().name, second.name)

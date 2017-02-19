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

    def test_home_template_content(self):
        """
        Check info to the template with one object
        """
        obj = ContactFactory()
        response = self.client.get(self.url)
        self.base_string_header(response, obj)

    def test_home_view_cyrillic(self):
        """
        Test for views.home in case object data is cyrillic
        """
        obj = ContactFactory.create(name='Артем', surname='Александрович',
                                    date_birth='1986-11-07', bio=u'Биография',
                                    email='test@email.com', skype='АБВГДЕ',
                                    jabber='ЖЗИЙК',
                                    other_contacts='Другие контакты')
        response = self.client.get(self.url)
        self.base_string_header(response, obj)

    def test_home_view_two_object(self):
        """
        Test home view, table Contact has 2 objects,
        """
        first = ContactFactory()
        second = ContactFactory()
        response = self.client.get(self.url)
        data = response.context['info']
        self.assertNotEqual(data, None)
        self.assertEqual(Contact.objects.first(), first)
        self.assertEqual(Contact.objects.last(), second)
        self.assertEqual(Contact.objects.count(), 2)
        self.base_string_header(response, first)

    def base_string_header(self, response, instance):
        """
        This method calls for tests base string header and header html
        """
        self.assertEqual(response.status_code, 200)
        self.assertInHTML('<link rel="stylesheet" href="/static/css/bootstrap/'
                          'bootstrap.min.css">', response.content)
        self.assertInHTML('<link rel="stylesheet" href="/static/css/style.css"'
                          ' media="screen, projection">', response.content)
        self.assertInHTML('<li class="active"><a href="/">Home</a></li>',
                          response.content)
        self.assertTrue('info' in response.context)
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Last name')
        self.assertContains(response, 'Date of birth')
        self.assertContains(response, 'Email')
        self.assertContains(response, 'Skype')
        self.assertContains(response, 'Jabber')
        self.assertContains(response, 'Contacts')
        self.assertContains(response, '42 Coffee Cups Test Assignment')
        self.assertContains(response, instance.name)
        self.assertContains(response, instance.surname)
        self.assertContains(response, instance.date_birth)
        self.assertIn(response.context['info'].bio, instance.bio)
        self.assertContains(response, instance.email)
        self.assertContains(response, instance.skype)
        self.assertContains(response, instance.jabber)
        self.assertContains(response, instance.other_contacts)

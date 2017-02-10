from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class HomeViewTest(TestCase):
    """"
    Tests views
    """
    def setUp(self):
        """
        Set base info for working tests
        """
        self.client = Client()
        self.url = reverse('home')
        self.response = self.client.get(self.url)

    def test_home_template_context(self):
        """
        Check home status code and context
        """
        self.assertEqual(self.response.status_code, 200)
        self.assertTrue('info' in self.response.context)

    def test_home_template_content(self):
        """
        Check personal info (name, surname, email, jabber, skype,
        other contacts) to the template
        """
        data = self.response.context['info']
        print data
        self.assertEqual(data.name, 'myName')
        self.assertEqual(data.surname, 'mySurname')
        self.assertEqual(data.date_birth.strftime('%d-%m-%Y'), '07-11-1986')
        self.assertEqual(data.bio, 'Django Python developer Dublh 3 '
                                   '\r\nJunior Django Python developer')
        self.assertEqual(data.email, 'email@email.com')
        self.assertEquals(data.skype, 'skype')
        self.assertEqual(data.jabber, 'jabber@co')

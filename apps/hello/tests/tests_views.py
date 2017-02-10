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
        self.assertContains(data['name'], 'myName')
        self.assertContains(data['surname'], 'mySurname')
        self.assertContains(data['date_birth'], '07-11-1986')
        self.assertContains(data['bio'], 'Django Python developer Dublh 3')
        self.assertContains(data['email'], 'email@email.com')
        self.assertContains(data['skype'], 'skype')
        self.assertContains(data['jabber'], 'jabber@co')
        self.assertContains(data['other_contacts'], 'other_contacts')

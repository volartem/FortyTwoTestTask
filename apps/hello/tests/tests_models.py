# -*- coding: utf-8 -*-
from django.test import TestCase
from apps.hello.models import Contact
from django.utils.encoding import smart_unicode
from datetime import datetime, date


class ContactModelTest(TestCase):
    """
    Test Contact model
    """

    def setUp(self):
        """
        Setup object to tests
        """
        Contact.objects.create(name="testName2",
                               surname='testSurname2',
                               date_birth="2002-02-03",
                               bio='test bio info3\n test bio info4',
                               email='test@email.com2',
                               jabber='test@jabber.com2',
                               skype='test_skype2',
                               other_contacts='test contact info2',)

    def test_unicode(self):
        """
        Test unicode returns correct
        """

        contact = Contact(name=u'Джуниор', surname=u'Джанго')
        self.assertEqual(smart_unicode(contact), u'Джуниор Джанго')

    def test_contact_instance_first(self):
        """
        Test first instance that would be in template
        """
        contact = Contact.objects.first()
        self.assertIsInstance(contact.created, datetime)
        self.assertIsInstance(contact.name, unicode)
        self.assertIsInstance(contact.date_birth, date)
        self.assertEqual(contact.date_birth.strftime('%d-%m-%Y'),
                         date(2002, 2, 3).strftime('%d-%m-%Y'))
        self.assertEqual(contact.name, u'testName2')
        self.assertEqual(contact.surname, u'testSurname2')
        self.assertEqual(contact.email, u'test@email.com2')
        self.assertEqual(contact.skype, u'test_skype2')
        self.assertEqual(contact.bio, u'test bio info3\n test bio info4')

    def test_contact_instance_last(self):
        """
        Test second instance that created
        """
        Contact.objects.create(
            name="testName22",
            surname='testSurname22',
            date_birth="2002-02-04",
            bio='test bio info5\n test bio info6',
            email='test@email.com22',
            jabber='test@jabber.com22',
            skype='test_skype22',
            other_contacts='test contact info22',)
        contact = Contact.objects.last()
        self.assertIsInstance(contact.created, datetime)
        self.assertIsInstance(contact.name, unicode)
        self.assertIsInstance(contact.date_birth, date)
        self.assertEqual(contact.date_birth, date(2002, 02, 04))
        self.assertEqual(contact.name, u'testName22')
        self.assertEqual(contact.surname, u'testSurname22')
        self.assertEqual(contact.email, u'test@email.com22')
        self.assertEqual(contact.skype, u'test_skype22')
        self.assertEqual(contact.bio, u'test bio info5\n test bio info6')

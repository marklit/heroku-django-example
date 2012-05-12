from about_us.models import Person, Role
from django.test import TestCase


class PeopleTest(TestCase):
    def test_person_creation(self):
        p = Person()
        p.first_name = 'Mark'
        p.last_name = 'Litwintschik'
        p.save()
        self.assertEqual(int(p.id), 1)

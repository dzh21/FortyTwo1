from django.test import TestCase
from tasks42.models import Person
from django.utils import timezone


class MainViewTest(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.response = self.client.get('/')

    def test_url_for_exist(self):
        """ test main page existing """
        self.assertEquals(self.response.status_code, 200)

    def test_for_template_usage(self):
        """ test base.html and home.html template usage """
        self.assertTemplateUsed(self.response, "base.html")
        self.assertTemplateUsed(self.response, "home.html")

    def test_for_my_contacts(self):
        """ test showing my contacts at main page """
        self.assertIn('Evhen', self.response.content)
        self.assertIn('Davliud', self.response.content)
        self.assertIn('dzh21@tut.by', self.response.content)

    def test_context_for_one_person(self):
        """ test only one person showing """
        self.assertEquals(len(self.response.context['persons']), 1)

    def test_for_invalid_data(self):
        """ test that contacts of over person not showing on main page """
        self.assertEquals('Vasya' in self.response.content, False)
        self.assertEquals('vasya@gmail.com' in self.response.content, False)

    def test_only_one_person_showing(self):
        """ test only my contacts show """
        new_person = Person(
            name="Frodo",
            surname="Baggins",
            date_of_birth=timezone.now()
        )
        new_person.save()

        self.assertEquals("Frodo" in self.response.content, False)
        self.assertIn("Evhen", self.response.content)

from django.test import TestCase


class MainViewTest(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.response = self.client.get('/')

    def test_url_for_exist(self):
        self.assertEquals(self.response.status_code, 200)

    def test_for_template_usage(self):
        self.assertTemplateUsed(self.response, "base.html")
        self.assertTemplateUsed(self.response, "home.html")

    def test_for_my_contacts(self):
        self.assertIn('Evhen', self.response.content)
        self.assertIn('Davliud', self.response.content)
        self.assertIn('dzh21@tut.by', self.response.content)

    def test_context_for_one_person(self):
        self.assertEquals(len(self.response.context['persons']), 1)
from django.test import TestCase


class MainViewTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_url_for_exist(self):
        self.assertEquals(self.response.status_code, 200)

    def test_for_template_usage(self):
        self.assertTemplateUsed(self.response, "base.html")
        self.assertTemplateUsed(self.response, "home.html")

from django.test import TestCase
from tasks42.models import RequestObject
from django.utils import timezone


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

    def test_for_invalid_data(self):
        self.assertEquals('Vasya' in self.response.content, False)
        self.assertEquals('vasya@gmail.com' in self.response.content, False)

    def test_for_request_link(self):
        self.assertIn('requests', self.response.content)

    def test_for_following_request_link(self):
        self.assertEquals(self.client.get('/requests/').status_code, 200)


class RequestsViewTest(TestCase):

    def setUp(self):
        for i in xrange(12):
            self.response = self.client.get('/requests/')

    def test_template_usage(self):
        self.assertTemplateUsed(self.response, 'requests.html')

    def test_request_records_showing(self):
        self.assertIn('Request #', self.response.content)

    def test_first_ten_requests_showing(self):
        requests_in_db = list(RequestObject.objects.order_by(
            'event_date_time'
        ))[:10]

        self.assertEquals(len(self.response.context['requests']), 10)

        self.assertIn(
            timezone.localtime(
                requests_in_db[0].event_date_time
            ).strftime('%Y-%m-%d %H:%M:%S'),
            self.response.content
        )
        self.assertIn(
            timezone.localtime(
                requests_in_db[9].event_date_time
            ).strftime('%Y-%m-%d %H:%M:%S'),
            self.response.content
        )




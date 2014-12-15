from django.test import TestCase
from tasks42.models import Person, RequestObject
from django.utils import timezone
from django.conf import settings
from tasks42.forms import PersonForm
from django.forms import model_to_dict


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
        self.assertIn('<img src=', self.response.content)

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

        response = self.client.get('/')

        self.assertEquals("Frodo" in response.content, False)
        self.assertIn("Evhen", response.content)

    def test_settings_in_context(self):
        """ test existing of project setting in page context """
        setting_in_context = self.response.context['settings']
        self.assertEquals(setting_in_context, settings)

    def test_edit_contacts_link(self):
        """ test edit contacts link existing on main page """
        self.assertIn('/edit_contacts/', self.response.content)


class RequestsViewTest(TestCase):

    def setUp(self):
        for i in xrange(12):
            self.response = self.client.get('/requests/')

    def test_template_usage(self):
        """ test template usage """
        self.assertTemplateUsed(self.response, 'requests.html')

    def test_request_records_showing(self):
        """ test requests showing """
        self.assertIn('Request #', self.response.content)

    def test_first_ten_requests_showing(self):
        """ test only 10 first request showing """
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


class EditContactsViewTest(TestCase):

    def setUp(self):
        self._login()
        self.assertEquals(self.response.context['user'].is_active, True)
        self.response = self.client.get('/edit_contacts/')

    def _login(self):
        """ login to edit data """
        logindata = {
            'username': 'admin',
            'password': 'admin'
        }
        self.response = self.client.post(
            '/accounts/login/',
            logindata,
            follow=True
        )

    def test_existing_page(self):
        """ test for edit contacts page existing """
        self.assertEquals(self.response.status_code, 200)

    def test_for_template_usage(self):
        """ test for template usage """
        self.assertTemplateUsed(self.response, "edit_contacts.html")

    def test_form_with_contacts_on_page(self):
        """ test my contact in form fields """
        self.assertIn('form', self.response.content)
        self.assertIn('value="Save"', self.response.content)

        self.assertIn('value="Evhen"', self.response.content)
        self.assertIn('value="dzh21@tut.by"', self.response.content)
        self.assertIn('value="dzh@default.rs"', self.response.content)

    def test_form_for_saving_data(self):
        person = Person.objects.get(pk=1)
        person.email = 'newemail@gmail.com'

        form = PersonForm(model_to_dict(person), instance=person)
        self.assertEquals(form.is_valid(), True)

        response = self.client.post(
            '/edit_contacts/',
            data=form.cleaned_data
        )

        self.assertEquals(response.status_code, 200)
        # self.assertIn(person.email, response.content)
        self.assertIn('Changes have been saved', response.content)
        response = self.client.get('/')
        self.assertIn(person.email, response.content)

    def test_datepicker_class_of_input(self):
        """ test for datepicker class of input element """
        self.assertIn('class="datepicker', self.response.content)


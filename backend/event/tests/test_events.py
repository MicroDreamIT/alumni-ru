import datetime

from django.test import TestCase
from ..models import Event
from faker import Faker


class EventModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        fake = Faker()
        Event.objects.create(
            title=fake.word(nb=5),
            description=fake.paragraph(nb_sentences=50),
            venue=fake.company(),
            street_address=fake.street_address(),
            state=fake.state(),
            city=fake.city(),
            country='Bangladesh',
            event_date_start=fake.date(),
            event_date_end=fake.date(),
            is_active=fake.boolean(),
            registration_start_date=fake.date(),
            registration_end_date=fake.date()
        )

    def test_title_field(self):
        event = Event.objects.get(id=1)
        title = event._meta.get_field('title')
        self.assertEqual(title.verbose_name, 'title')
        self.assertIsInstance(event.title, str)

    def test_description_field(self):
        event = Event.objects.get(id=1)
        description = event._meta.get_field('description')
        self.assertEqual(description.verbose_name, 'description')
        self.assertIsInstance(event.description, str)

    def test_venue_field(self):
        event = Event.objects.get(id=1)
        venue = event._meta.get_field('venue')
        self.assertEqual(venue.verbose_name, 'venue')
        self.assertIsInstance(event.venue, str)

    def test_street_address_field(self):
        event = Event.objects.get(id=1)
        street_address = event._meta.get_field('street_address')
        self.assertEqual(street_address.verbose_name, 'street address')
        self.assertIsInstance(event.street_address, str)

    def test_state_field(self):
        event = Event.objects.get(id=1)
        state = event._meta.get_field('state')
        self.assertEqual(state.verbose_name, 'state')
        self.assertIsInstance(event.state, str)

    def test_city_field(self):
        event = Event.objects.get(id=1)
        city = event._meta.get_field('city')
        self.assertEqual(city.verbose_name, 'city')
        self.assertIsInstance(event.city, str)

    def test_country_field(self):
        event = Event.objects.get(id=1)
        country = event._meta.get_field('country')
        self.assertEqual(country.verbose_name, 'country')
        self.assertEqual(event.country, 'Bangladesh')

    def test_event_date_start_field(self):
        event = Event.objects.get(id=1)
        event_date_start = event._meta.get_field('event_date_start')
        self.assertEqual(event_date_start.verbose_name, 'event date start')
        self.assertIsInstance(event.event_date_start, datetime.date)

    def test_event_date_end_field(self):
        event = Event.objects.get(id=1)
        event_date_end = event._meta.get_field('event_date_end')
        self.assertEqual(event_date_end.verbose_name, 'event date end')
        self.assertIsInstance(event.event_date_end, datetime.date)

    def test_registration_start_date_field(self):
        event = Event.objects.get(id=1)
        registration_start_date = event._meta.get_field('registration_start_date')
        self.assertEqual(registration_start_date.verbose_name, 'registration start date')
        self.assertIsInstance(event.registration_start_date, datetime.date)

    def test_registration_end_date_field(self):
        event = Event.objects.get(id=1)
        registration_end_date = event._meta.get_field('registration_end_date')
        self.assertEqual(registration_end_date.verbose_name, 'registration end date')
        self.assertIsInstance(event.registration_end_date, datetime.date)

    def test_string_representation(self):
        event = Event.objects.get(id=1)
        self.assertIsInstance(str(event), str)

    # Add more test methods for other model behaviors

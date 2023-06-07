from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from faker import Faker

fake = Faker()


class UserModelTest(TestCase):

    def create_fake_user(self):
        return User.objects.create_user(
            username=fake.user_name(),
            email=fake.email(),
            password='Test@12@3%',
            first_name=fake.first_name(),
            last_name=fake.last_name(),
        )

    def test_create_user(self):
        user = self.create_fake_user()

        self.assertEqual(user.email, user.email)
        self.assertEqual(user.first_name, user.first_name)
        self.assertEqual(user.last_name, user.last_name)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

        self.assertEqual(get_user_model().objects.count(), 1)

    def test_create_user(self):
        user = self.create_fake_user()
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.username, user.username)

    def test_get_full_name(self):
        user = self.create_fake_user()
        self.assertEqual(user.get_full_name(), f"{user.first_name} {user.last_name}")

    def test_get_short_name(self):
        user = self.create_fake_user()
        self.assertEqual(user.get_short_name(), user.first_name)


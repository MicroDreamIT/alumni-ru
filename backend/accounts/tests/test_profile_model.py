from django.test import TestCase
from faker import Faker
from ..models import Profile
from .test_user_model import UserModelTest

fake = Faker()


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = UserModelTest().create_fake_user()
        self.profile = Profile.objects.create(
            user=self.user,
            gender=fake.random_element(elements=('M', 'F')),
            subject=fake.job(),
            batch_no=fake.random_number(digits=4),
            enroll_year=fake.random_number(digits=4),
            graduation_year=fake.random_number(digits=4),
            street_address=fake.street_address(),
            city=fake.city(),
            state=fake.state(),
            postal_code=fake.postcode(),
            phone_number=fake.phone_number()[:15],
            paid_amount=0
        )

    def test_profile_creation(self):
        self.assertTrue(isinstance(self.profile, Profile))
        self.assertEqual(self.profile.user, self.user)
        # Add more assertions for other profile fields

    def test_profile_str(self):
        expected_str = f"{self.user.username}"
        self.assertEqual(str(self.profile), expected_str)

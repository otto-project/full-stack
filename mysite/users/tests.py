from django.test import TestCase
from django.urls import reverse

from .forms import SignUpForm
from .models import CustomUser


class CustomUserModelTestCase(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(
            username="testuser",
            password="testpass123",
            gender="male",
            height=175,
            weight=70
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.gender, "male")
        self.assertEqual(user.height, 175)
        self.assertEqual(user.weight, 70)
        self.assertTrue(user.check_password("testpass123"))


class SignUpFormTest(TestCase):
    def test_signup_form_valid(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'gender': 'male',
            'height': 175,
            'weight': 70,
        }
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_signup_form_invalid_password_mismatch(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpass123',
            'password2': 'testpass456',
            'gender': 'male',
            'height': 175,
            'weight': 70,
        }
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)


class SignUpViewTest(TestCase):
    def test_signup_view(self):
        url = reverse('users:signup')
        form_data = {
            'username': 'testuser',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'gender': 'male',
            'height': 175,
            'weight': 70,
        }
        response = self.client.post(url, form_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful signup
        self.assertTrue(CustomUser.objects.filter(username='testuser').exists())

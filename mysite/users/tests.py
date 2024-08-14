from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from products.models import ProductTable

from .forms import SignUpForm
from .models import CustomUser
from .models import UserMLResult


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


class UserMLResultsTest(TestCase):
    def setUp(self):
        # 테스트에 사용할 유저와 제품을 생성
        self.user = CustomUser.objects.create_user(
            username="testuser",
            password="testpass123",
            gender="male",
            height=175,
            weight=70
        )
        self.product = ProductTable.objects.create(
            product_id="1",
            product_name="Test Product",
            platform="musinsa",
            category="top",
            rank=1,
            price=10000,
            image_url="http://example.com/image.jpg",
            description="A test product",
            color="black",
            size="M"
        )

    def test_needs_api_call_no_results(self):
        # 사용자의 MLResult가 없는 경우, needs_api_call은 True를 반환해야 함
        self.assertTrue(UserMLResult.needs_api_call(self.user))

    def test_needs_api_call_old_result(self):
        # 오래된 결과가 있는 경우, needs_api_call은 True를 반환해야 함
        old_timestamp = timezone.now() - timedelta(days=2)
        old_timestamp = old_timestamp.replace(tzinfo=timezone.get_current_timezone())  # 타임존 명시적 설정
        UserMLResult.objects.create(user=self.user, product=self.product, score=0.9, size='M', timestamp=old_timestamp)
        self.assertTrue(UserMLResult.needs_api_call(self.user))

    def test_needs_api_call_recent_result(self):
        # 최근의 결과가 있는 경우, needs_api_call은 False를 반환해야 함
        recent_timestamp = timezone.now() - timedelta(hours=12)
        UserMLResult.objects.create(user=self.user, product=self.product, score=0.9, size='M',
                                    timestamp=recent_timestamp)
        self.assertFalse(UserMLResult.needs_api_call(self.user))

    def test_some(self):
        result = UserMLResult.objects.create(user=self.user, product=self.product, score=0.9, size='M')
        print(result.timestamp)

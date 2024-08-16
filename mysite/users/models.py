from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import IntegrityError
from django.db import models
from django.utils import timezone
from products.models import ProductTable


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('male', '남'),
        ('female', '여'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()


class UserMLResult(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductTable, on_delete=models.CASCADE)
    size = models.CharField(max_length=100, blank=True, null=True)
    score = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'product')

    @staticmethod
    def create(user: CustomUser, product: ProductTable, size: str, score: float):
        try:
            return UserMLResult.objects.create(
                user=user,
                product=product,
                size=size,
                score=score
            )
        except IntegrityError as e:
            return None

    @staticmethod
    def needs_api_call(user):
        last_result = UserMLResult.objects.filter(user=user).order_by('-timestamp').first()

        if not last_result:
            return True

        now = timezone.now()

        time_diff = now - last_result.timestamp

        if time_diff > timedelta(days=1):
            return True

        return False

    @staticmethod
    def get_ml_results(user):
        pass

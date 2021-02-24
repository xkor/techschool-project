from django.db import models
from django.contrib.auth import get_user_model
from datetime import date


User = get_user_model()


class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.full_name
    #
    # @property
    # def age(self):
    #     today = date.today()
    #
    #     age = today.year - self.date_of_birth.year - ((today.month, today.day) <
    #              (self.date_of_birth.month, self.date_of_birth.day))
    #     return age
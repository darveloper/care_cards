from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True, max_length=200)
    address = models.CharField(max_length=300)
    address_line_2 = models.CharField(blank=True, null=True, max_length=200)
    city = models.CharField(default=None, max_length=200)
    state = models.CharField(default=None, max_length=3)
    zip_code = models.CharField(max_length=12)
    phone = models.CharField(blank=True, null=True, max_length=20)

    def __str__(self):
        return self.name
    
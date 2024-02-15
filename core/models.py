from django.db import models


# Create your models here.
class Contact(models.Model):
    class Meta:
        ordering = ("name", "phone_number")

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    date_of_event = models.DateField()
    additional_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)

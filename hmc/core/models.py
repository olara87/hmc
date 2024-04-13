from django.db import models


# Create your models here.

# The bottom class was moved to the Order class in the 'orders' app
class Contact(models.Model):
    class Meta:
        ordering = ("first_name", "phone_number")

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    # the bottom two lines of code were moved to the Order class in the 'orders' app
    date_of_event = models.DateField()
    additional_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.phone_number}"
        # return str(self.first_name)

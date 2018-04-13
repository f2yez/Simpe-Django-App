from django.db import models

class Client(models.Model):
    client_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=100)
    contact_name = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    phone_number = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        db_table = "client"

    def __str__(self):
        return self.client_name

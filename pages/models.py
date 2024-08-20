from django.db import models

class NamostuteQRFormData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_QRscanned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.phone_number}"

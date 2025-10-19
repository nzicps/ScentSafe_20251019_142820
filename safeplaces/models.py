from django.db import models

class SafePlace(models.Model):
    address = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

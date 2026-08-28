from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=80)
    is_available = models.BooleanField(default=True)
    borrower_first_name = models.CharField(max_length=80, blank=True)
    borrower_last_name = models.CharField(max_length=80, blank=True)
    borrowed_at = models.DateTimeField(null=True, blank=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["category", "name"]

    def __str__(self):
        return self.name

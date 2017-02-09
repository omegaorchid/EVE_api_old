from django.db import models


class Join(models.Model):
    first_name = models.CharField(max_length=128, blank=True)
    email = models.EmailField(max_length=128, unique=True, help_text="eg: 123@esp.ext")
    ref_id = models.CharField(max_length=32, default="default", unique=True)
    ip_address = models.GenericIPAddressField(default='default')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.email

    class Meta:
        unique_together = ('email', 'ref_id')
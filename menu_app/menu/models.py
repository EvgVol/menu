from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class MenuItem(models.Model):
    name = models.CharField(_('name'), max_length=255)
    parent = models.ForeignKey('self', related_name='children',
                               blank=True, null=True,
                               on_delete=models.CASCADE)
    url = models.CharField(max_length=2000, blank=True)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return self.url or reverse(self.name)

    def __str__(self):
        return self.name

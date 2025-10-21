from django.db import models


class PageVisit(models.Model):
    path = models.TextField(max_length=200, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.path)
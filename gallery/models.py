from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    group_id = models.CharField(
        unique=True,
        max_length=20,
        primary_key=True,
        default=None
    )
    group_name = models.CharField(max_length=60)

class Photo(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=20,
        default=None
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        default=None,
        related_name="photos"
        )
    owner = models.CharField(max_length=20, null=True, blank=True)
    secret = models.CharField(max_length=20, null=True, blank=True)
    server = models.CharField(max_length=20, null=True, blank=True)
    farm = models.IntegerField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    ispublic = models.IntegerField(null=True, blank=True)
    isfriend = models.IntegerField(null=True, blank=True)
    isfamily = models.IntegerField(null=True, blank=True)
    ownername = models.CharField(max_length=60, null=True, blank=True)
    dateadded = models.CharField(
        max_length=20,
        default=None,
        null=True,
        blank=True
        )

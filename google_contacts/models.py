from uuid import uuid4

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models

from picklefield import PickledObjectField

class ActionState(models.Model):
    """
    A temporary store for the state of a user form entry.

    The typical usage of this would be for an action where the user needs
    to leave and return to the page, for instance in an iframe-busting
    auth process.
    """
    uuid            = models.CharField(max_length=32, default=lambda: uuid4().hex, primary_key=True)
    action_type     = models.ForeignKey(ContentType, null=True)
    action_id       = models.PositiveIntegerField(null=True)
    action          = generic.GenericForeignKey('action_type', 'action_id')
    data            = PickledObjectField()
    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)

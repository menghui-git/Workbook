from django.db import models

from accounts.models import User
from vocab.models import Word


class UserWord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    word = models.ForeignKey(Word, on_delete=models.CASCADE, blank=False, null=False,
                             unique=True)  # TODO: remove the constrain after adding user feature
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['user', 'word']]

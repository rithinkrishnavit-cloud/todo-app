from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE


# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    # class meta used to add additional settings or configuaration in our model
    class Meta:
        # show all tasks in newses first /
        ordering = ["-created_at"]

    # show todo text
    def __str__(self):
        # send back  todo title
        return self.title

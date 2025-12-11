from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse

# getting user model object
# Create your models here.


class Post(models.Model):
    """
    a class to define posts for blog app
    """

    author = models.ForeignKey(
        "accounts.Profile", verbose_name=_("author"), on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    status = models.BooleanField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    image = models.ImageField(upload_to="./images", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_snippet(self):
        return self.content[0:5]

    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

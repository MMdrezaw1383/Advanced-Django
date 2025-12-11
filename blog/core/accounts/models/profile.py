from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from .users import User


class Profile(models.Model):
    user = models.ForeignKey("User", verbose_name=_("user"), on_delete=models.CASCADE)
    first_name = models.CharField(_("first_name"), max_length=50)
    last_name = models.CharField(_("last_name"), max_length=50)
    image = models.ImageField(
        _("image"),
        upload_to=None,
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True,
        null=True,
    )
    description = models.TextField(_("description"))

    created = models.DateTimeField(_("created at"), auto_now_add=True)
    updated = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

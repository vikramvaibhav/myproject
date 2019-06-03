import os
import random
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

LOCATION = (
	('IND','India'),
	('USA','United States of America')
)


def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,34567899)
    name, ext = get_file_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'profiles/{new_filename}/{final_filename}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True, choices=LOCATION)
    birth_date = models.DateField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

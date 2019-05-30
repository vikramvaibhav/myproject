import random
import os
from django.db import models
from django.contrib.auth.models import User


# def get_file_ext(filepath):
#     base_name = os.path.basename(filepath)
#     name, ext = os.path.splitext(base_name)
#     return name, ext
#
# def upload_image_path(instance, filename):
#     print(instance)
#     print(filename)
#     new_filename = random.randint(1,34567899)
#     name, ext = get_file_ext(filename)
#     final_filename = f'{new_filename}{ext}'
#     return f'profile/{new_filename}/{final_filename}'
#
# class UserProfile(models.Model):
#     user   = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
#
#     def __str__(self):
#         return self.user.username

from django.urls import path
from .views import ProfileListView,update_profile

app_name = 'profiles'

urlpatterns = [
        path('', ProfileListView.as_view(), name='profile'),
        path('update/', update_profile, name='update_profile'),
]

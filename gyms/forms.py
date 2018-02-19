from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from gyms.models import User, Gym, AdminUser

class AdminSignUpForm(UserCreationForm):
    gym_name_field = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        gym = Gym.objects.create(gym_name=self.cleaned_data.get('gym_name_field'))
        adminUser = AdminUser.objects.create(user=user)
        adminUser.gym.add(gym)
        return user

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Profile
from django import forms

# Define the user registration form
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

# Handle registration logic
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()  # Save the user first

            # Create a profile for the new user
            Profile.objects.create(user=user, is_normal_user=True)
            login(request, user)  # Log the user in automatically
            return redirect('home')  # Redirect to home page after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
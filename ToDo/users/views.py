from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth import login
from django.conf import settings
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            try:
                send_mail(
                    subject='Welcome to My Website',
                    message='Thank you for signing up for our platform. [user.email]',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user.email],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Error sending email: {e}")

            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            try:
                send_mail(
                    subject='Login Successful',
                    message='You have successfully logged in to your account. [user.email]',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user.email],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Error sending email: {e}")

            return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


@login_required
def delete_user(request, user_id):
    # Only admins or the user themselves can delete their account
    if request.user.id == user_id or request.user.is_superuser:
        user = get_object_or_404(User, id=user_id)
        
        # Delete the user
        user.delete()

        # Display a success message
        messages.success(request, "Your account has been deleted successfully.")

        # Redirect to homepage or login page
        return redirect('home')  # or 'login' if you want to redirect them to login
    else:
        # If the user is not the one trying to delete their own account or an admin
        messages.error(request, "You are not authorized to delete this account.")
        return redirect('home')

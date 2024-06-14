from django.contrib.sites.shortcuts import get_current_site
from django.db import IntegrityError
from django.forms import ValidationError
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate,get_user_model, logout
from .forms import RegistrationForm, LoginForm, LoginAdminForm
from .tokens import account_activation_token
from .models import User
from studentLife_system.models import studentInfo
from django.core.mail import send_mail,get_connection
from django.conf import settings


def index(request):
    form = RegistrationForm()
    form2 = LoginForm()
    return render(request, "application/signin.html", { "form":form, "form2":form2})

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            try:
                email = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(email=email, password=password)
                if user is not None:
                    if not user.is_active:
                        messages.error(request, "Your account is not activated. Please check your email and activate your account.")
                    else:
                        login(request, user)
                       
                        if user.is_staff:
                            return redirect('admin_dashboard')
                        else:
                            return redirect('studentLife_system:homepage')
                else:
                    messages.error(request, "Invalid email or password.")
            except ValidationError as e:
                messages.error(request, "Invalid email or password.")
            except Exception as e:
                messages.error(request, "An error occurred during login: {}".format(str(e)))
                # Log the exception or handle it in some other way
        else: 
            try:
                email = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(email=email, password=password)
                if user is not None:
                    if not user.is_active:
                        messages.error(request, "Your account is not activated. Please check your email and activate your account.")
                    else:
                        login(request, user)
                        
                        if user.is_staff:
                            return redirect('admin_dashboard')
                        else:
                            return redirect('studentLife_system:homepage')
                else:
                    messages.error(request, "Invalid email or password.")
            except ValidationError as e:
                messages.error(request, "Invalid email or password.")
            except Exception as e:
                messages.error(request, "An error occurred during login: {}".format(str(e)))
    else:
        form = LoginForm()

    return render(request, "application/signin.html", {"form2": form})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            # Get the student_id from the form
            student_id = form.cleaned_data.get('student_id')

            try:
                # Check if the student_id exists in the studentInfo model
                student_info = studentInfo.objects.get(studID=student_id)
            except studentInfo.DoesNotExist:
                messages.error(request, "The provided student ID does not exist in our records.")
                return redirect('custom_user:register')
            except Exception as e:
                messages.error(8)
                return redirect('custom_user:register')
            
            if User.objects.filter(email=form.cleaned_data.get('email')).exists():
                messages.error(request, "The email is already in use.")
                return redirect('custom_user:register')

            # Check if the passwords match
            if form.cleaned_data.get('password1') != form.cleaned_data.get('password2'):
                messages.error(request, "The passwords do not match.")
                return redirect('custom_user:register')
            
            # Create the user and save it
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            to_email = user.email
            current_site = get_current_site(request)
            domain = current_site.domain
            
            # Generate the email subject and body
            email_subject = 'Activate your account'
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            
            activation_link = f"http://{domain}{reverse('custom_user:activate', kwargs={'uidb64': uid, 'token': token})}"
            email_body = f"""
            <html>
            <body style='font-family: Arial, sans-serif; line-height: 1.6; color: #333;'>
                <div style='max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ccc; border-radius: 10px; background-color: #f9f9f9;'>
                    <h2 style='text-align: center; color: #0056b3;'>Thank you for registering with us.</h2>
                    <p>Dear <strong>{user.student_id.firstname} {user.student_id.lastname}</strong>,</p>
                    <p>To complete your registration, please click on the link below to confirm your account:</p>
                    <p><a href="{activation_link}" style="color: #0056b3;">Confirm Registration</a></p>
                    <p>If you did not request this registration, please ignore this email.</p>
                    <p>Best Regards,</p>
                    <p><strong>CTU Argao Student Affairs Office</strong></p>
                </div>
            </body>
            </html>
            """

             # Get the recipient email
            email_backend = get_connection(
                backend='django.core.mail.backends.smtp.EmailBackend',
                host="smtp.gmail.com",
                port=587,
                username="studentlifeargao@gmail.com",
                password="figwhgiznibwxhvz",
                use_tls=True
            )
        
            # Send the email
            send_mail(
                email_subject,
                '',  # Plain text version is empty since we are sending HTML content
                "studentlifeargao@gmail.com",  # From email
                [to_email],
                html_message=email_body,
                fail_silently=False,
                connection=email_backend,
            )

            
            # Inform the user
            messages.success(request, "Please check your email to complete the registration")
            return redirect("custom_user:index")
        
        else:
            # Add form errors to messages
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = RegistrationForm()
    
    return render(request, "application/signup.html", {"form": form})



def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        # Specify the backend
        backend = settings.AUTHENTICATION_BACKENDS[0]  # Use the first backend from settings
        login(request, user, backend=backend)
        
        messages.success(request, "Your account has been successfully activated!")
        return redirect(reverse("custom_user:index"))
    else:
        messages.error(request, "Activation link is invalid or expired")
        return redirect("custom_user:index")
    
import logging

def login_admin(request):
    if request.method == "POST":
        form = LoginAdminForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user_type = form.cleaned_data.get('user_type')
            user = authenticate(email=email, password=password)
            
            if user is not None:
                if not user.is_active:
                    messages.error(request, "Your account is not activated. Please check your email and activate your account.")
                else:
                    if user.user_type == user_type:
                        login(request, user)
                        if user_type == 'sao admin':
                            return redirect('studentLife_system:equipmentTrackerAdmin')
                        elif user_type == 'medical admin':
                            return redirect('medical:patient_profile')
                    else:
                        messages.error(request, "The provided user type does not match the user's account type.")
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid login form submission.")
            logging.debug("Form errors: %s", form.errors)
    else:
        form = LoginAdminForm()

    return render(request, "application/signin_admin.html", {"form": form})




def logout_user(request):
    logout(request)
    return redirect('studentLife_system:homepage')
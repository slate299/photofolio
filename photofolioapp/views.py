from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage, Photo  # Import the model for saving messages

# Create your views here.
def home(request):
    # Pass a range of numbers to the context
    context = {
        'range': range(1, 9),
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def photo_gallery(request):
    photos = Photo.objects.all()
    context = {
        'photos': photos,
    }
    return render(request, 'photo_gallery.html', context)

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Save the message to the database
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )

            # Send an email (make sure email settings are configured in settings.py)
            try:
                send_mail(
                    f"New Contact Message: {subject}",  # Subject of the email
                    f"From: {name} <{email}>\n\n{message}",  # Email body
                    email,    # Sender's email
                    ['your-email@example.com'],  # Recipient's email
                    fail_silently=False,
                )
                messages.success(request, "Your message has been sent successfully!")
            except Exception as e:
                # Log the error or handle it as needed
                messages.error(request, "There was an error sending the email. Please try again later.")

            # Redirect or display a success message
            return redirect('thank_you')  # Redirect to the contact page or a thank-you page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')

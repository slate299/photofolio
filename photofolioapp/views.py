from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def home(request):
    # Pass a range of numbers to the context
    context = {
        'range': range(1, 9),
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

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

            # Send an email (make sure email settings are configured in settings.py)
            send_mail(
                subject,  # Subject of the email
                message,  # Message body
                email,    # Sender's email
                ['your-email@example.com'],  # Recipient's email
                fail_silently=False,
            )

            # Optionally, redirect or display a success message
            return HttpResponse("Message sent successfully!")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
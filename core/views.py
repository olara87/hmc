from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from django.contrib import messages
from django.core.mail import send_mail
from hmc.settings import EMAIL_HOST_USER, EMAIL_HOST_COMPANY, COMPANY_WEBSITE

from .forms import ContactForm


def home(request):
    request_form = ContactForm()
    if request.method == "POST":
        request_form = ContactForm(request.POST)

        if request_form.is_valid():
            request_form.save()
            messages.success(
                request,
                "Thank you for your submission. A representative will reach out shortly.",
            )

            name: str = request_form.cleaned_data["name"]
            phone_number: str = request_form.cleaned_data["phone_number"]
            email: str = request_form.cleaned_data["email"]
            additional_notes: str = request_form.cleaned_data["additional_notes"]

            html: str = render_to_string(
                "core/email/contact_form.html",
                {
                    "name": name,
                    "phone_number": phone_number,
                    "email": email,
                    "additional_notes": additional_notes,
                    "company_website": COMPANY_WEBSITE
                },
            )

            subject: str = str(COMPANY_WEBSITE).join(" | New Order")

            recipient_list: list[str] = [str(EMAIL_HOST_USER), str(EMAIL_HOST_COMPANY)]

            send_mail(
                subject,
                "This is the message",
                EMAIL_HOST_USER,
                recipient_list,
                fail_silently=True,
                html_message=html,
            ) 

            return redirect("core:home")

    context: dict[str, ContactForm] = {"form": request_form}

    return render(request, "core/home.html", context)

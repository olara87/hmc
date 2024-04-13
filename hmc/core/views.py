from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from django.contrib import messages
from django.core.mail import send_mail
from hmc.settings import EMAIL_HOST_USER, EMAIL_HOST_COMPANY, COMPANY_WEBSITE

from .forms import ContactForm

from time import sleep


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def contact(request):
    request_form = ContactForm()
    if request.method == "POST":
        request_form = ContactForm(request.POST)

        if request_form.is_valid():
            request_form.save()
            messages.success(
                request,
                "Your form has been submitted. Thank you.",
            )

            name: str = (
                request_form.cleaned_data["first_name"]
                + " "
                + request_form.cleaned_data["last_name"]
            )
            phone_number: str = request_form.cleaned_data["phone_number"]
            email: str = request_form.cleaned_data["email"]
            additional_notes: str = request_form.cleaned_data["additional_notes"]
            company_website = str(COMPANY_WEBSITE)

            html: str = render_to_string(
                "core/email/contact_form.html",
                {
                    "name": name,
                    "phone_number": phone_number,
                    "email": email,
                    "additional_notes": additional_notes,
                    "company_website": company_website,
                },
            )

            subject: str = company_website + " | New Order"

            recipient_list: list[str] = [str(EMAIL_HOST_USER), str(EMAIL_HOST_COMPANY)]

            send_mail(
                subject,
                "This is the message",
                EMAIL_HOST_USER,
                recipient_list,
                fail_silently=True,
                html_message=html,
            )
            sleep(
                5
            )  # 5 seconds before redirect is executed if user does not click on "home" button on dialog tag.
            return redirect("core:home")

    context: dict[str, ContactForm] = {"form": request_form}
    return render(request, "core/contact.html", context)

from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib import messages
from django.core.mail import send_mail
from hmc.settings import (
    EMAIL_HOST_USER,
    EMAIL_HOST_COMPANY,
    COMPANY_WEBSITE,
    PORTFOLIO_LINK,
)

from .forms import ContactForm


def home(request):
    url = PORTFOLIO_LINK
    context = {"portfolio_link": url}
    return render(request, "core/home.html", context)


def about(request):
    url = PORTFOLIO_LINK
    context = {"portfolio_link": url}
    return render(request, "core/about.html", context)


def thank_you(request):
    if "form_submitted" in request.session:
        del request.session["form_submitted"]
    return render(request, "core/thank_you.html")


def contact(request):
    url: str | None = PORTFOLIO_LINK
    request_form = ContactForm()
    if request.method == "POST":
        request_form = ContactForm(request.POST)

        if request.session.get("form_submitted", False):
            messages.warning(request, "You already submitted this form.")
            return HttpResponseRedirect(reverse("core:thank_you"))

        if request_form.is_valid():
            request_form.save()
            messages.success(
                request,
                "Your form has been submitted. Thank you.",
            )
            request.session["form_submitted"] = True
            name = f"{request_form.cleaned_data['first_name']} {request_form.cleaned_data['last_name']}"
            phone_number = request_form.cleaned_data["phone_number"]
            email = request_form.cleaned_data["email"]
            additional_notes = request_form.cleaned_data["additional_notes"]

            html: str = render_to_string(
                "core/email/contact_form.html",
                {
                    "name": name,
                    "phone_number": phone_number,
                    "email": email,
                    "additional_notes": additional_notes,
                    "company_website": COMPANY_WEBSITE,
                },
            )

            subject = f"{COMPANY_WEBSITE} | New Order"

            recipient_list = [EMAIL_HOST_COMPANY]

            send_mail(
                subject,
                "This is the message",
                EMAIL_HOST_USER,
                recipient_list,  # type: ignore
                fail_silently=True,
                html_message=html,
            )
            return HttpResponseRedirect(reverse("core:thank_you"))
    else:
        request_form = ContactForm()

    context: dict[str, ContactForm] = {"form": request_form, "portfolio_link": url}  # type: ignore
    return render(request, "core/contact.html", context)

from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage, Profile,Certificate, PortfolioProject
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def index(request):
    projects = PortfolioProject.objects.all()
    profile = Profile.objects.prefetch_related("skills", "portfolio_items").first()
    context = {
        "profile": profile,
        "data": _("Hello, world! This is a multilingual site."),
        "projects": projects,
    }
    return render(request, "main/index.html", context)


def contact(request):
    context = {
        "data": _("Contact us at:)"),
    }
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        # بررسی کامل بودن فیلدها
        if not name or not email or not message:
            context["error"] = _("Please fill in all fields.")
        # بررسی دامنه ایمیل
        elif not email.endswith("@gmail.com"):
            context["error"] = _("Only @gmail.com emails are allowed.")
        else:

            ContactMessage.objects.create(name=name, email=email, message=message)

            subject = f"پیام جدید از {name}"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [settings.DEFAULT_FROM_EMAIL]

            # محتوای ساده متن
            text_content = f"پیام: {message}\n\nارسال شده توسط: {name} - {email}"

            # محتوای HTML (می‌تونی قالب دلخواه خودت رو بسازی)
            html_content = render_to_string(
                "main/contact_message.html",
                {
                    "name": name,
                    "email": email,
                    "message": message,
                },
            )

            email_msg = EmailMultiAlternatives(
                subject, text_content, from_email, to_email
            )
            email_msg.attach_alternative(html_content, "text/html")
            email_msg.send()

            context["success"] = _("Your message has been sent successfully.")
            # Redirect to index after successful submission
            # ارسال ایمیل تشکر به کاربر
            user_subject = _("Thank you for your message")
            user_text_content = _(
                f"Dear {name},\n\n"
                "Thank you for contacting us. We have received your message and will get back to you soon.\n\n"
                "Your message:\n"
                f"{message}\n\n"
                "Best regards,\n"
                "Arad Rezvaninejad"
            )

            # محتوای HTML برای کاربر
            user_html_content = render_to_string(
                "main/thank_you.html",
                {
                    "name": name,
                    "message": message,
                },
            )

            user_email = EmailMultiAlternatives(
                user_subject,
                user_text_content,
                from_email,
                [email],  # ارسال به ایمیل کاربر
            )
            user_email.attach_alternative(user_html_content, "text/html")

            try:
                user_email.send()

                context["success"] = _(
                    "Your message has been sent successfully. A confirmation email has been sent to you."
                )
                return redirect("index")

            except Exception as e:
                context["error"] = _(
                    "An error occurred while sending the email. Please try again later."
                )
                # برای دیباگ می‌توانید خطا را لاگ کنید
                print(f"Email sending error: {str(e)}")

        return redirect("index")

    return render(request, "main/contact.html", context=context)


def About(request):
    certificates = Certificate.objects.all()
    print(certificates)
    profile = Profile.objects.prefetch_related("skills", "portfolio_items").first()
    context = {
        "data": _("This is the About page."),
        "profile": profile,
        "certificates": certificates,
    }
    return render(request, "main/About.html", context=context)


def blog(request):
    context = {
        "data": _("This is the Blog page."),
    }
    return render(request, "main/Blog.html", context=context)


def portfolio(request):
    projects = PortfolioProject.objects.all()
    context = {
        "data": _("This is the Portfolio page."),
        "projects": projects,
    }
    return render(request, "main/portfolio.html", context=context)
from datetime import datetime

from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from monicasafarisapi.settings import EMAIL_USER, DOMAIN


current_year = datetime.now().year


def send_client_booking_email(booking):
    """
    A function to send a client booking email once the booking is made
    """
    try:
        tour_url = f"{DOMAIN}/tours/{booking.tour.reference}"
        booking_url = f"{DOMAIN}/bookings/{booking.reference}"
        email_body = render_to_string(
            "booking_email.html",
            {
                "booking": booking,
                "tour": booking.tour.title,
                "name": booking.name,
                "email": booking.email,
                "phone": booking.phone,
                "date": booking.date,
                "guests": booking.guests,
                "special_requests": booking.special_requests,
                "status": booking.status,
                "request_jeep": booking.request_jeep,
                "currency": booking.currency,
                "amount": booking.amount,
                "payment_method": booking.payment_method,
                "payment_status": booking.payment_status,
                "tour_url": tour_url,
                "booking_url": booking_url,
                "current_year": current_year,
            },
        )

        send_mail(
            subject="Your booking has been made",
            message="",
            from_email=EMAIL_USER,
            recipient_list=[booking.email],
            fail_silently=False,
            html_message=email_body,
        )
    except BadHeaderError:
        raise ValueError("Invalid header found")
    except Exception as e:
        raise ValueError(str(e))


def notify_owner_of_booking(booking):
    """
    Sends an email to the tour company owner when a booking is made
    """
    try:
        tour_url = f"{DOMAIN}/admin/tours/{booking.tour.slug}"
        booking_url = f"{DOMAIN}/admin/bookings/{booking.slug}"
        email_body = render_to_string(
            "notify_owner.html",
            {
                 "booking": booking,
                "tour": booking.tour.title,
                "name": booking.name,
                "email": booking.email,
                "phone": booking.phone,
                "date": booking.date,
                "guests": booking.guests,
                "special_requests": booking.special_requests,
                "status": booking.status,
                "request_jeep": booking.request_jeep,
                "currency": booking.currency,
                "amount": booking.amount,
                "payment_method": booking.payment_method,
                "payment_status": booking.payment_status,
                "tour_url": tour_url,
                "booking_url": booking_url,
                "current_year": current_year,
            }
        )

        send_mail(
            subject="A booking has been made",
            message="",
            from_email=EMAIL_USER,
            recipient_list=[booking.tour.user.email],
            fail_silently=False,
            html_message=email_body,
        )
    except BadHeaderError:
        raise ValueError("Invalid header found")
    except Exception as e:
        raise ValueError(str(e))

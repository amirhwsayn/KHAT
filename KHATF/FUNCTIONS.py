from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from django.core.exceptions import ObjectDoesNotExist
from KHAT.settings import EMAIL_HOST_USER
from .models import Token


def SendToken(email):
    subject = 'Subject'
    plain_message = ''
    from_email = EMAIL_HOST_USER
    to = [email, ]
    mcode = get_random_string(6, allowed_chars='123456789')
    html_message = render_to_string('send_code_mail.html', {'code': mcode})
    mtoken = get_random_string(50)
    Token.objects.create(
        email=email,
        token=mtoken,
        code=mcode
    )
    send_mail(subject=subject,
              message=plain_message,
              from_email=from_email,
              recipient_list=to,
              html_message=html_message
              )
    return mtoken


def token_isvalid(request):
    if 'token' in request.headers and 'code' in request.headers:
        code = request.headers['code']
        mtoken = request.headers['token']
        try:
            Token.objects.get(token=mtoken)
        except ObjectDoesNotExist:
            return False
        else:
            if Token.objects.get(token=mtoken).code == code:
                return True
            else:
                return False
    return False

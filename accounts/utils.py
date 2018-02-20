import requests
import datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.http import HttpResponse
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
import coffee.settings as st
from accounts.models import MyUser
from accounts.serializers import MyUserSerializer, MyUserSignupSerializer


def send_text_email(body, subject, to_address, from_address=os.environ['email_address']):
    """
        This will send the email.
    """
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(os.environ['email_address'], os.environ['email_password'])
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()


def send_verification_email(token, email):
    """
        This method will send the mail to verify the email.
        Caution : Don't remove \n from msg, else mail will go in spam, without body.
    """
    url = "http://127.0.0.1:8000/accounts/verify/email/"
    subject = "Welcome to BearStateCoffee. Verify Your Email."
    msg = "Click on the following url to verify your email address.\n "
    msg += url + token + '/'

    send_text_email(msg, subject, email)


def send_reset_password_email(email):
    """
        This method will send the mail to reset the password.
        Caution : Don't remove \n from msg, else mail will go in spam, without body.
    """
    user = MyUser.objects.filter(email=email).first()
    if user:
        user.generate_token()

        subject = "Reset Your Password"
        url = "http://127.0.0.1:8000/accounts/reset/password/"
        msg = "Click on the following url to reset your password.\n "
        msg += url + user.token + '/'

        send_text_email(msg, subject, email)
        return Response({'result': True, 'data': 'Email Sent'})
    else:
        return Response({'result': False, 'message': 'Invalid Email'})


def register_user(user_type, data):
    """
        Helper function to register user.
    """
    serialized_data = MyUserSignupSerializer(data=data)
    if not serialized_data.is_valid():
        response = {'result': False, 'message': 'User already exists'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    if user_type == 'super_user':
        MyUser.objects.create_superuser(**serialized_data.validated_data)
    elif user_type == 'user':
        user = MyUser.objects.create_user(**serialized_data.validated_data)
        user.generate_token()
        send_verification_email(user.email_token, user.email)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response({'result': True, 'data': 'User registered successfully.'})


def get_auth_token(email, password):
    """
        This methods sends the post request to fetch the access and refresh token.
    """
    url = 'http://localhost:8000/o/token/'
    auth = (st.CLIENT_ID, st.CLIENT_SECRET)
    payload = {
        'grant_type': 'password',
        'username': email,
        'password': password
    }
    return requests.post(url, data=payload, auth=auth)


def revoke_auth_token(token):
    """
        This methods sends the post request to revoke token.
    """
    url = 'http://localhost:8000/o/revoke_token/'
    auth = (st.CLIENT_ID, st.CLIENT_SECRET)
    payload = {
        'token': token
    }
    if requests.post(url, data=payload, auth=auth).status_code == 200:
        return Response({'result': True, 'data': 'Revoked'})
    return Response({'result': False, 'message': 'Some problem occurred'})


def login_user(email, password):
    """
        This will first confirm if user is already verified the email or not,
        if not then it wil send the email to verify the user.
    """
    user = MyUser.objects.filter(email=email).first()

    if user:
        if user.is_verified:
            response = get_auth_token(email, password)
            if 'error' in response.json():
                return Response({'result': False, 'message': 'Invalid Credentials'})
            payload = {
                'result': True,
                'data': {
                    'token': response.json(),
                    'user': MyUserSerializer(instance=user).data
                }
            }
            return Response(payload)
        else:
            user.generate_token()
            send_verification_email(user.email_token, user.email)
            return Response({'result': True, 'data': 'Verify Your Email First'})
    else:
        return Response({'result': False, 'message': 'Invalid Credentials'})


def check_within_time(original_date, time_period_allowed):
    """
    :param original_date: Time at which token was generated
    :param time_period_allowed: Link should be used in what period of time
    :return: True or False
    """
    checker_date = timezone.now() - datetime.timedelta(**time_period_allowed)

    if checker_date > original_date:
        return False

    return True


def verify_email(token):
    """
        This will help in verifying email.
    """
    user = MyUser.objects.filter(email_token=token).first()

    if user:
        if not check_within_time(user.email_token_created_on, {'days': 2}):
            response = HttpResponse("<h1>Link Expired</h1>")
        else:
            user.is_verified = True
            response = HttpResponse("<h1>Email Address Successfully Verified</h1>")

        user.email_token = ""
        user.save()

        return response

    return HttpResponse("<h1>Link Does not Exist </h1>")


def reset_password_form(token):
    """
        If the link is clicked within 2 days it will return password reset form.
    """
    user = MyUser.objects.filter(email_token=token).first()

    if user:
        if not check_within_time(user.email_token_created_on, {'days': 2}):
            response = HttpResponse("<h1>Link Expired</h1>")
        else:
            user.is_verified = True
            # TODO password reset form should be returned
            response = HttpResponse("<h1>You can verify your password</h1>")

        user.save()

        return response

    return HttpResponse("<h1>Link Does not Exist </h1>")


def reset_password(token, password):
    """
        It will help to reset the password, and also verifies email, if not verified.
    """
    user = MyUser.objects.filter(email_token=token).first()

    if user:
        if not check_within_time(user.email_token_created_on, {'days': 2}):
            response = {'result': False, 'message': 'Link expired.'}
            user.email_token = ""
        else:
            user.is_verified = True
            user.set_password(password)
            user.email_token = ""
            response = {'result': True, 'data': 'Password reset successful.'}

        user.save()

        return Response(response)

    return Response({'result': False, 'message': 'Link does not exists.'})

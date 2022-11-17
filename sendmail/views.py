# coding=utf-8
from django.shortcuts import render

from django.template.loader import get_template
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from email_sending.settings import DEFAULT_FROM_EMAIL
from .functions import handle_uploaded_file
import csv


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            html_apload = 'templates/html_upload/'  # address for html doc
            to_emails = 'templates/to_emails_upload/'  # address for csv doc
            subject = form.cleaned_data['subject']
            handle_uploaded_file(to_emails, request.FILES['to_email_list'])  # save csv doc
            handle_uploaded_file(html_apload, request.FILES['file1'])  # save html doc
            with open('templates/to_emails_upload/' + request.FILES['to_email_list'].name, 'r') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                contex = []
                for row in reader:
                    contex.append(row)
            try:
                for i in contex:
                    send_mail(subject, '',
                              DEFAULT_FROM_EMAIL, [i['Email']],
                              html_message=get_template('html_upload/' + request.FILES['file1'].name).render(i))
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
        return HttpResponseRedirect('/success/')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "email.html", {'form': form, 'DEFAULT_FROM_EMAIL': DEFAULT_FROM_EMAIL})


def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')

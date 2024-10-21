from django.shortcuts import render




def language_popup(request):
    return render(request,'language_popup.html')


def client_form(request):
    return render(request,'client_form.html')


def client_mobile_verification(request):
    return render(request,'client_mobile_verification.html')

def client_otp_verification(request):
    return render(request,'client_otp_verification.html')

def client_payment(request):
    return render(request,'client_payment.html')

def home_page(request):
    return render(request,'home_page.html')

def worker_login_page(request):
    return render(request,'worker_login_page.html')

def worker_registration_form(request):
    return render(request,'worker_registration_form.html')
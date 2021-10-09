from notingApp.models import NotingModel
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from random import randrange


def usignup(request):
    if request.method == "POST":
        usernameUsignup = request.POST.get("signupUsername")
        emailUsignup = request.POST.get("signupEmail")

        if len(usernameUsignup) < 2 or usernameUsignup is None:
            return render(request, "usignup.html", {"msg": "Username cannot be less than 2 characters"})

        try:
            usr = User.objects.get(username=usernameUsignup)
            return render(request, "usignup.html", {"msg": "Username taken"})
        except Exception as e:
            pass

        try:
            # username=usernameUsignup,
            usr = User.objects.get(email=emailUsignup)
            return render(request, "usignup.html", {"msg": "User with this email is already registered"})
        except User.DoesNotExist:
            pw = ""
            text = "abcdefghijklmnopqrstuvwxyz".upper(
            ) + "abcdefghijklmnopqrstuvwxyz" + "0123456789"
            for i in range(8):
                pw += text[randrange(len(text))]
            subject = "Welcome to Noting"
            msg = "The password for your Noting account is " + str(pw)
            host = "karkerakartik08@gmail.com"
            recipient = [emailUsignup, ]
            send_mail(subject, msg, host, recipient)
            usr = User.objects.create_user(
                username=usernameUsignup, password=pw, email=emailUsignup)
            usr.save()

            return redirect("ulogin")
    else:
        return render(request, "usignup.html")


def ulogin(request):
    if request.method == "POST":
        usernameUlogin = request.POST.get("loginUsername")
        passwordUlogin = request.POST.get("loginpassword")
        usr = authenticate(username=usernameUlogin, password=passwordUlogin)
        if usr is not None:
            login(request, usr)
            request.session["name"] = usernameUlogin
            return redirect("home")
        else:
            return render(request, "ulogin.html", {"msg": "Invalid Login"})
    else:
        return render(request, "ulogin.html")


def uresetPass(request):
    if request.method == "POST":
        usernameUresetPass = request.POST.get("resetPassUsername")
        emailUresetPass = request.POST.get("resetPassEmail")
        try:
            usr = User.objects.get(
                username=usernameUresetPass, email=emailUresetPass)
            pw = ""
            text = "abcdefghijklmnopqrstuvwxyz".upper(
            ) + "abcdefghijklmnopqrstuvwxyz" + "0123456789"
            for i in range(8):
                pw += text[randrange(len(text))]
            subject = "Welcome to Noting"
            msg = "The new password for your Noting account is " + str(pw)
            host = "karkerakartik08@gmail.com"
            recipient = [emailUresetPass, ]
            send_mail(subject, msg, host, recipient)
            usr.set_password(pw)
            usr.save()
            return redirect("ulogin")
        except User.DoesNotExist:
            return render(request, "uresetPass.html", {"msg": "User not registered"})
    else:
        return render(request, "uresetPass.html")


def ulogout(request):
    logout(request)
    request.session.flush()
    request.session.clear_expired()
    return redirect("ulogin")


def deleteNote(request, noteID):
    noteToDelete = NotingModel.objects.get(noteID=noteID)
    noteToDelete.delete()
    return redirect("home")

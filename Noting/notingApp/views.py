from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import NotingModel


def home(request):
    if request.method == "GET" and request.user.is_authenticated:
        notes = NotingModel.objects.filter(author=request.user)
        return render(request, "home.html", {"notes": notes})
    else:
        return redirect("ulogin")


def createNote(request):
    if request.method == "POST":
        noteTitle = request.POST.get('noteTitle')
        noteDesc = request.POST.get('noteDesc')

        if noteTitle == "":
            return render(request, "createNote.html", {"msg": "Note must contain title"})

        try:
            data = NotingModel(
                title=noteTitle, description=noteDesc, author=request.user)
            data.save()
        except Exception as e:
            return render(request, "createNote.html", {"msg": "Error: " + str(e)})

        return render(request, "createNote.html", {"msg": "Note created"})

    else:
        return render(request, "createNote.html")


def feedback(request):
    if request.method == "POST":
        feedbackMessage = request.POST.get("feedbackMessage")
        # feedbackEmail = request.POST.get("feedbackEmail")
        try:
            feedbackEmail = request.user.email
        except Exception as e:
            msg = "You need to be a authenticated user to provide feedback"
            return render(request, "feedback.html", {"msg": msg})
        subject = "Feedback regarding Noting Project"
        msg = feedbackMessage
        host = feedbackEmail
        recipient = ["karkerakartik08@gmail.com", ]
        send_mail(subject, msg, host, recipient)
        msg = "Email sent from your registered Email. Thanks for your feedback"
        return render(request, "feedback.html", {"msg": msg})
    else:
        try:
            feedbackEmail = request.user.email
        except AttributeError:
            msg = "You need to be a authenticated user to provide feedback"
            return render(request, "feedback.html", {"msg": msg})
        return render(request, "feedback.html")

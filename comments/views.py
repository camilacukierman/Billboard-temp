from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Message
from django.template import loader
from django.contrib.auth import authenticate


def index(request):
    latest_message = Message.objects.order_by('-pub_date')[:5]
    template = loader.get_template('comments/index.html')
    context = {
    'latest_message': latest_message,
}
    return HttpResponse(template.render(context, request))

def postcomment (request):
    myauthor= request.POST.get("author_text")
    mytitle = request.POST.get("title_text")
    mymessage = request.POST.get("message_text")
    newMsg = Message.objects.create(author_text=myauthor,title_text=mytitle,message_text=mymessage)
    newMsg.save()
    return redirect("/comments")



user = authenticate(username='john', password='secret')
if user is not None:
        # the password verified for the user
    if user.is_active:
        print("User is valid, active and authenticated")
    else:
        print("The password is valid, but the account has been disabled!")
else:
    # the authentication system was unable to verify the username and password
    print("The username and password were incorrect.")

def some_view(request):
    if request.user.is_authenticated():
        print('authenticated')
    # Do something for authenticated users.
    else:
    # Do something for anonymous users.
        print('not authenticated')

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
        login(request, user)
        # Redirect to a success page.
        else:
        # Return a 'disabled account' error message
    else:
        # Return an 'invalid login' error message.
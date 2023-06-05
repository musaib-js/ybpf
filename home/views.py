from django.shortcuts import render
from .models import Event, EventImages, Member, Blog, Query
from django.contrib import messages
# Create your views here.
def home(request):
    events = Event.objects.all().order_by("-timestamp")[0:4]
    members = Member.objects.all()
    posts = Blog.objects.all().order_by("-timestamp")[0:3]
    context = {"events": events, "team": members, "posts": posts}
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def events(request):
    events = Event.objects.all()
    context = {"events": events}
    return render(request, "events.html", context)

def eventspecific(request, pk):
    event = Event.objects.filter(pk = pk)[0]
    images = EventImages.objects.filter(event = event)
    context = {"event": event, "images": images}
    return render(request, "eventdetails.html", context)

def blog(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, "blog.html", context)

def blogspecific(request, pk):
    blog = Blog.objects.filter(pk = pk)[0]
    context = {"blog": blog}
    return render(request, "blog_details.html", context)

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        query = Query(name = name, email = email, subject = subject, phone = phone, message = message)
        query.save()
        messages.success(request, "Your message has been sent successfully. We'll get back to you soon. Thank you for contacting YBPF!")
    return render(request, "contact.html")
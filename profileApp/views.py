from django.shortcuts import redirect, render
from .models import contact,about,address
# Create your views here.
def index_view(request):
  abouts = about.objects.all()
  addresses = address.objects.all()
  context = {
    'about':abouts,
    'address':addresses
  }
  return render(request, 'index.html',context)
def contact_view(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    phone = request.POST.get('phone')
    subject = request.POST.get('subject')
    project = request.POST.get('project')
    contacts = contact.objects.create(name=name, email=email, message=message, phone=phone, subject=subject, project=project)
    contacts.save()
    return redirect(index_view)
  return redirect(index_view)
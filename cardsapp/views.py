from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PersonForm
from .models import Person

def index(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            receiver = Person.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                address=form.cleaned_data["address"],
                address_line_2=form.cleaned_data["address_line_2"],
                city=form.cleaned_data["city"],
                state=form.cleaned_data["state"],
                zip_code=form.cleaned_data["zip_code"],
                phone=form.cleaned_data["phone"]

            )
            receiver.save()
            return HttpResponseRedirect('thanks')
    else:
        form = PersonForm()
    return render(request, 'index.html', {'form': form })

def thanks(request):
    return render(request, 'thanks.html')

def about(request):
    return render(request, 'about.html')

def donate(request):
    return render(request, 'donate.html')
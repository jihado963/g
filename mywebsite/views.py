from django.shortcuts import render
from django.http import HttpResponse
from .forms import personMForm
from django.views.generic import ListView
# Create your views here.

def personview(request):
    form = personMForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'person_view.html', context)


from .models import personM

class ViewList(ListView):
    template_name = 'viewlist.html'
    queryset = personM.objects.all()

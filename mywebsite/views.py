from django.shortcuts import render
from django.http import HttpResponse
from .forms import personMForm
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
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

# class ViewList(ListView):
#     template_name = 'viewlist.html'
#     queryset = personM.objects.all()



@login_required
def vlist(request):

    filter = request.GET.get('filter', '')
    orderby = request.GET.get('orderby', 'id')

    context = {
        
        'object_list' : personM.objects.filter(
            Q(f_name__contains=filter)
            | Q(l_name__contains=filter)
            | Q(phone_num__contains=filter)
            | Q(email__contains=filter)
            ).order_by(orderby).all()
    }
    return render(request, 'viewlist.html', context)


    
import csv

def export(request):

    output = []
    response = HttpResponse (content_type='text/csv')
    writer = csv.writer(response)
    query_set = personM.objects.all()
    writer.writerow(['First Name', 'Last Name', 'E-mail', 'Phone number'])
    for user in query_set:
        output.append([user.f_name, user.l_name, user.email, user.phone_num])
    writer.writerows(output)
    return response

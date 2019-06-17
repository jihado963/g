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


#class MyView(ListView): #not ready yet 
#   model = personM
#  template_name = "viewlist.html"
#    paginate_by = 10
#
#    def get_queryset(self):
#        filter_val = self.request.GET.get('filter', 'id')
#        order = self.request.GET.get('orderby', 'id')
#            state=filter_val,
#        ).order_by(order)
#        return new_context
#
#    def get_context_data(self, **kwargs):
#        context = super(MyView, self).get_context_data(**kwargs)
#        context['filter'] = self.request.GET.get('filter', 'id')
#        context['orderby'] = self.request.GET.get('orderby', 'id

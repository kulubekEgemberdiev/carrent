from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from reservations.models import Reserve
import mimetypes
import os
from django.http.response import HttpResponse
from .forms import AgreementCreateForm
from .models import Agreement, Service


class AgreementListView(ListView):
    model = Agreement
    template_name = 'agreements/agreement_list.html'
    queryset = Agreement.objects.all()


class AgreementDetailView(DetailView):
    model = Agreement
    template_name = 'agreements/agreement_detail.html'


class AgreementCreateView(CreateView):
    model = Agreement
    template_name = 'agreements/agreement_create.html'
    form_class = AgreementCreateForm

    def get_context_data(self, **kwargs):
        context = super(AgreementCreateView, self).get_context_data(**kwargs)
        context['reserve_info'] = Reserve.objects.get(pk=self.kwargs['reserve_id'])
        return context

    def get_success_url(self):
        return reverse('agreement_detail', kwargs={'pk': self.object.pk})


def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'agreement.txt'
    filepath = BASE_DIR + '/CityRent/Files/' + filename
    path = open(filepath, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

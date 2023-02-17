from .models import Contact


def contact(request):
    return {'contact': Contact.objects.all()}

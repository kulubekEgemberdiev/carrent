from .models import Service


def service(request):
    return {'service': Service.objects.all()}

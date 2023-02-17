from .models import Reserve


def reservation(request):
    return {'reservation': Reserve.objects.all()}

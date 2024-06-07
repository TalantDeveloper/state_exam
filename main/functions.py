from .models import Student, Group, Title, Station, General


def contexts_func(request):
    stations = Station.objects.all()
    groups = Group.objects.all()
    generals = General.objects.all()
    context = {
        'stations': stations,
        'groups': groups,
        'generals': generals,
    }
    return context


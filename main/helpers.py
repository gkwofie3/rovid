from .models import Project,Service
def db(request):
    return {
        'name':"ROvid Smart...",
        'services': Service.objects.all(),
        'projects':Project.objects.all()
    }